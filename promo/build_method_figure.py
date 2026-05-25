from __future__ import annotations

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from neuromed_xai_benchmark.datasets.synthetic import make_synthetic_eeg
from neuromed_xai_benchmark.models.psd_baseline import fit_psd_baseline
from neuromed_xai_benchmark.xai.channel_importance import estimate_channel_importance

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial", "DejaVu Sans", "Liberation Sans"]
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["font.size"] = 8
plt.rcParams["axes.linewidth"] = 0.8

COLORS = {
    "ink": "#1F2933",
    "muted": "#667085",
    "line": "#D5DAE1",
    "bg": "#F7F9FC",
    "blue": "#2F6DB2",
    "cyan": "#35A6B8",
    "violet": "#7C6CCF",
    "amber": "#D98B2B",
    "green": "#3C8C5A",
    "red": "#B84A4A",
}


def clean(ax):
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


def panel_label(ax, label):
    ax.text(
        -0.03,
        1.04,
        label,
        transform=ax.transAxes,
        fontsize=11,
        fontweight="bold",
        ha="left",
        va="bottom",
        color=COLORS["ink"],
    )


def box(ax, xy, wh, title, body, fc="#FFFFFF", ec=None, title_color=None):
    x, y = xy
    w, h = wh
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.012,rounding_size=0.018",
        fc=fc,
        ec=ec or COLORS["line"],
        lw=1.0,
    )
    ax.add_patch(patch)
    ax.text(
        x + 0.025,
        y + h - 0.055,
        title,
        fontsize=9,
        fontweight="bold",
        color=title_color or COLORS["ink"],
        ha="left",
        va="top",
    )
    ax.text(
        x + 0.025,
        y + h - 0.125,
        body,
        fontsize=7.2,
        color=COLORS["muted"],
        ha="left",
        va="top",
        linespacing=1.25,
    )
    return patch


def arrow(ax, start, end, color=COLORS["muted"], rad=0.0):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=10,
            lw=1.1,
            color=color,
            connectionstyle=f"arc3,rad={rad}",
        )
    )


def draw_pipeline(ax):
    clean(ax)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.text(
        0.01,
        0.95,
        "NeuroMed-XAI Benchmark: leakage-aware EEG benchmark route with interpretable evidence",
        fontsize=15,
        fontweight="bold",
        color=COLORS["ink"],
        ha="left",
        va="top",
    )
    ax.text(
        0.01,
        0.855,
        "Research pain point: EEG medical AI is often hard to audit because leakage, preprocessing choices, metrics, and explanation evidence are not reported in one reproducible route.",
        fontsize=8.5,
        color=COLORS["muted"],
        ha="left",
        va="top",
    )
    stages = [
        ("1 EEG cohort", "samples x channels x time\nlabels + subject ids", COLORS["cyan"]),
        ("2 Split", "GroupShuffleSplit\nsubject-wise holdout", COLORS["blue"]),
        ("3 Features", "FFT power spectrum\nPSD / bandpower", COLORS["violet"]),
        ("4 Model", "RandomForest baseline\nfuture deep models", COLORS["amber"]),
        ("5 XAI report", "channel attribution\nmetrics + caveats", COLORS["green"]),
    ]
    xs = np.linspace(0.02, 0.82, len(stages))
    for idx, (title, body, color) in enumerate(stages):
        box(ax, (xs[idx], 0.29), (0.145, 0.34), title, body, fc="#FFFFFF", ec=color, title_color=color)
        if idx < len(stages) - 1:
            arrow(ax, (xs[idx] + 0.145, 0.46), (xs[idx + 1] - 0.01, 0.46), color=color)
    ax.text(
        0.02,
        0.13,
        "Literature anchors: EEG disease AI review; XAI for BCI review; SHAP seizure detection; interpretable seizure features; graph attention; prototype sleep staging; WaveSleepNet.",
        fontsize=7.5,
        color=COLORS["muted"],
        ha="left",
    )


def draw_eeg(ax, dataset):
    panel_label(ax, "a")
    ax.set_title("Synthetic multichannel EEG task", loc="left", fontsize=10, fontweight="bold")
    t = np.arange(dataset.signals.shape[-1]) / dataset.sampling_rate
    sample_0 = dataset.signals[dataset.labels == 0][0]
    sample_1 = dataset.signals[dataset.labels == 1][0]
    for ch in range(4):
        ax.plot(t, sample_0[ch] * 0.18 + ch, color="#B8C1CC", lw=0.8)
        ax.plot(t, sample_1[ch] * 0.18 + ch + 4.5, color=COLORS["cyan"], lw=0.85)
    ax.text(0.02, 3.35, "class 0", color=COLORS["muted"], fontsize=7)
    ax.text(0.02, 7.85, "class 1 with 10-Hz pattern in Ch3/Ch4", color=COLORS["cyan"], fontsize=7)
    ax.set_xlabel("time (s)")
    ax.set_ylabel("channels")
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def draw_split(ax, dataset):
    panel_label(ax, "b")
    ax.set_title("Subject-wise split prevents leakage", loc="left", fontsize=10, fontweight="bold")
    clean(ax)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    subjects = np.unique(dataset.subjects)
    train = subjects[:9]
    test = subjects[9:]
    for i, subject in enumerate(subjects):
        x = 0.06 + (i % 6) * 0.145
        y = 0.72 - (i // 6) * 0.28
        color = COLORS["blue"] if subject in train else COLORS["amber"]
        ax.add_patch(FancyBboxPatch((x, y), 0.105, 0.13, boxstyle="round,pad=0.01,rounding_size=0.015", fc=color, ec=color, alpha=0.16))
        ax.text(x + 0.052, y + 0.066, f"S{subject+1}", fontsize=8, color=color, ha="center", va="center", fontweight="bold")
    ax.text(0.06, 0.18, "train subjects", color=COLORS["blue"], fontsize=8, fontweight="bold")
    ax.text(0.47, 0.18, "held-out subjects", color=COLORS["amber"], fontsize=8, fontweight="bold")
    ax.text(0.06, 0.08, "Groups, not epochs, define the split.", color=COLORS["muted"], fontsize=7.5)


def draw_model(ax, result):
    panel_label(ax, "c")
    ax.set_title("PSD baseline and benchmark metrics", loc="left", fontsize=10, fontweight="bold")
    clean(ax)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    metrics = [("accuracy", result.accuracy, COLORS["green"]), ("macro F1", result.macro_f1, COLORS["blue"])]
    for idx, (name, value, color) in enumerate(metrics):
        x = 0.12 + idx * 0.43
        ax.add_patch(Circle((x + 0.12, 0.56), 0.115, fc=color, ec="none", alpha=0.14))
        ax.text(x + 0.12, 0.58, f"{value:.3f}", fontsize=18, color=color, fontweight="bold", ha="center", va="center")
        ax.text(x + 0.12, 0.38, name, fontsize=8, color=COLORS["muted"], ha="center")
    box(ax, (0.12, 0.08), (0.76, 0.18), "model path", "FFT -> mean power per channel -> RandomForestClassifier", fc="#FFFFFF", ec=COLORS["line"])


def draw_attribution(ax, attribution):
    panel_label(ax, "d")
    ax.set_title("Channel attribution surface", loc="left", fontsize=10, fontweight="bold")
    names = list(attribution.channel_scores)
    scores = np.array([attribution.channel_scores[n] for n in names])
    order = np.argsort(scores)
    ax.barh(np.array(names)[order], scores[order], color=COLORS["violet"], alpha=0.85, height=0.55)
    top = attribution.top_channels[0]
    ax.text(scores.max() * 0.98, list(np.array(names)[order]).index(top), f"top: {top}", ha="right", va="center", color="white", fontsize=7, fontweight="bold")
    ax.set_xlabel("absolute class-mean difference")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def draw_report(ax, dataset, result, attribution):
    panel_label(ax, "e")
    ax.set_title("Reportable benchmark artifact", loc="left", fontsize=10, fontweight="bold")
    clean(ax)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    rows = [
        ("task", dataset.task_name),
        ("samples / channels", f"{dataset.signals.shape[0]} / {dataset.signals.shape[1]}"),
        ("sampling rate", f"{dataset.sampling_rate:.0f} Hz"),
        ("accuracy / macro F1", f"{result.accuracy:.3f} / {result.macro_f1:.3f}"),
        ("top channels", ", ".join(attribution.top_channels[:3])),
    ]
    for idx, (k, v) in enumerate(rows):
        y = 0.82 - idx * 0.15
        ax.text(0.05, y, k, fontsize=7.5, color=COLORS["muted"], ha="left", va="center")
        ax.text(0.42, y, v, fontsize=7.8, color=COLORS["ink"], ha="left", va="center", fontweight="bold" if idx in (3, 4) else "normal")
        ax.plot([0.05, 0.95], [y - 0.065, y - 0.065], color=COLORS["line"], lw=0.7)
    ax.text(0.05, 0.04, "Research benchmark only; no clinical diagnosis claim.", fontsize=7.3, color=COLORS["red"])


def draw_method_matrix(ax):
    panel_label(ax, "f")
    ax.set_title("Reference algorithms mapped to benchmark modules", loc="left", fontsize=10, fontweight="bold")
    clean(ax)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    rows = [
        ("EEG reviews", "cohort metadata", "subject split", "PSD/RF", "report caveats"),
        ("SHAP seizure", "feature evidence", "leakage notes", "feature reduction", "channel rank"),
        ("prototype sleep", "signal snippets", "session split", "deep encoder", "prototype tiles"),
        ("this repo", "EEGDataset", "SplitIndices", "BaselineResult", "BenchmarkRun"),
    ]
    cols = ["status", "data", "split", "model", "XAI/report"]
    x0 = [0.02, 0.19, 0.40, 0.59, 0.76]
    widths = [0.14, 0.18, 0.16, 0.14, 0.20]
    for x, w, col in zip(x0, widths, cols):
        ax.text(x, 0.86, col, fontsize=7.5, fontweight="bold", color=COLORS["ink"], ha="left")
        ax.plot([x, x + w], [0.82, 0.82], color=COLORS["line"], lw=1)
    for r, row in enumerate(rows):
        y = 0.70 - r * 0.17
        color = [COLORS["cyan"], COLORS["violet"], COLORS["amber"], COLORS["green"]][r]
        for x, w, text in zip(x0, widths, row):
            ax.add_patch(FancyBboxPatch((x, y), w, 0.105, boxstyle="round,pad=0.007,rounding_size=0.012", fc="#FFFFFF", ec=COLORS["line"], lw=0.7))
            ax.text(x + 0.008, y + 0.053, text, fontsize=6.4, color=color if x == x0[0] else COLORS["muted"], va="center", ha="left")


def main():
    dataset = make_synthetic_eeg()
    result = fit_psd_baseline(dataset)
    attribution = estimate_channel_importance(dataset)
    out = Path(__file__).with_name("cover-neuromed-xai-benchmark-v6.svg")
    fig = plt.figure(figsize=(16, 9), facecolor="white", constrained_layout=False)
    gs = fig.add_gridspec(
        nrows=3,
        ncols=4,
        height_ratios=[1.05, 1.25, 1.1],
        width_ratios=[1.2, 1.0, 1.05, 1.22],
        left=0.045,
        right=0.985,
        top=0.94,
        bottom=0.08,
        wspace=0.40,
        hspace=0.62,
    )
    draw_pipeline(fig.add_subplot(gs[0, :]))
    draw_eeg(fig.add_subplot(gs[1, 0]), dataset)
    draw_split(fig.add_subplot(gs[1, 1]), dataset)
    draw_model(fig.add_subplot(gs[1, 2]), result)
    draw_attribution(fig.add_subplot(gs[1, 3]), attribution)
    draw_report(fig.add_subplot(gs[2, 0:2]), dataset, result, attribution)
    draw_method_matrix(fig.add_subplot(gs[2, 2:]))
    fig.text(
        0.047,
        0.025,
        "Original methods figure. Literature anchors: EEG disease AI review, explainable BCI review, SHAP seizure detection, prototype sleep staging. Research benchmark only.",
        fontsize=7.5,
        color=COLORS["muted"],
    )
    fig.savefig(out, format="svg")
    print(out)


if __name__ == "__main__":
    main()
