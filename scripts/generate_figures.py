#!/usr/bin/env python3
"""Regenerate paper figures from the checked-in summary CSV files.

This script is intentionally offline: it does not call any LLM APIs and only
reads files already stored under results/summary_tables/.
"""
from pathlib import Path
import math
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SUMMARY = ROOT / "results" / "summary_tables"
FIG = ROOT / "figures"
FIG.mkdir(parents=True, exist_ok=True)

MODEL_ORDER = [
    "Falcon3-7B-Instruct",
    "ALLaM-7B-Instruct-preview",
    "AceGPT-v2-8B-Chat",
    "Gemini-2.5-Flash",
]
LABEL_ORDER = ["NUMBER", "LOCATION", "PERSON", "DESCRIPTION", "ENTITY", "ABBREVIATION"]
LANG_ORDER = ["English", "Arabic"]


def save_current(name: str):
    plt.tight_layout()
    plt.savefig(FIG / f"{name}.pdf")
    plt.savefig(FIG / f"{name}.png", dpi=200)
    plt.close()


def bar_by_language(df: pd.DataFrame, value_col: str, title: str, ylabel: str, name: str, ylim=None):
    pivot = df.pivot(index="model_display", columns="language", values=value_col).reindex(MODEL_ORDER)
    pivot = pivot[[c for c in LANG_ORDER if c in pivot.columns]]
    ax = pivot.plot(kind="bar", figsize=(7.2, 4.2), rot=15)
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel("Model")
    if ylim is not None:
        ax.set_ylim(*ylim)
    ax.legend(title="Language")
    ax.grid(axis="y", alpha=0.3)
    save_current(name)


def plot_progression():
    df = pd.read_csv(SUMMARY / "table2_falcon_prompt_progression.csv")
    x = np.arange(len(df))
    plt.figure(figsize=(6.8, 4.0))
    plt.plot(x, df["English"], marker="o", label="English")
    plt.plot(x, df["Arabic"], marker="o", label="Arabic")
    plt.xticks(x, df["Pilot"])
    plt.ylim(0.6, 1.03)
    plt.ylabel("Accuracy")
    plt.xlabel("Experiment")
    plt.title("Falcon3 Accuracy Across Prompt-Development Experiments")
    plt.grid(True, alpha=0.3)
    plt.legend()
    save_current("prompt_progression_accuracy")


def plot_cross_model_bars():
    df = pd.read_csv(SUMMARY / "table5_cross_model_validation_long.csv")
    bar_by_language(df, "accuracy", "Cross-model validation accuracy", "Accuracy", "cross_model_accuracy", (0.0, 1.05))
    bar_by_language(df, "average_sensitivity", "Average sensitivity", "Sensitivity", "cross_model_sensitivity", (0.0, max(0.045, df["average_sensitivity"].max() * 1.25)))
    bar_by_language(df, "average_consistency", "Average consistency", "Consistency", "cross_model_consistency", (0.80, 1.02))


def plot_class_heatmap():
    df = pd.read_csv(SUMMARY / "table6_cross_model_class_level_long.csv")
    df["row_label"] = df["language"] + "-" + df["label"]
    row_order = [f"{lang}-{label}" for lang in ["Arabic", "English"] for label in LABEL_ORDER]
    pivot = df.pivot_table(index="row_label", columns="model_display", values="accuracy", aggfunc="first")
    pivot = pivot.reindex(row_order).reindex(columns=MODEL_ORDER)
    data = pivot.to_numpy(dtype=float)
    plt.figure(figsize=(8.2, 5.4))
    im = plt.imshow(data, aspect="auto", vmin=0, vmax=1)
    plt.colorbar(im, label="Class accuracy")
    plt.xticks(np.arange(len(pivot.columns)), pivot.columns, rotation=25, ha="right")
    plt.yticks(np.arange(len(pivot.index)), pivot.index)
    plt.title("Class-level accuracy by model and language")
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if not math.isnan(data[i, j]):
                plt.text(j, i, f"{data[i, j]:.1f}", ha="center", va="center", fontsize=7)
    save_current("class_level_accuracy_heatmap")


def plot_pvalue_heatmap(language: str, name: str):
    df = pd.read_csv(SUMMARY / "pairwise_sign_test_pvalues.csv")
    df = df[df["language"].str.lower() == language.lower()].copy()
    if df.empty:
        return
    pivot = df.pivot(index="model_row", columns="model_col", values="p_value").reindex(index=MODEL_ORDER, columns=MODEL_ORDER)
    p = pivot.to_numpy(dtype=float)
    data = -np.log10(np.clip(p, 1e-12, 1.0))
    plt.figure(figsize=(6.2, 5.0))
    im = plt.imshow(data, aspect="auto")
    plt.colorbar(im, label="-log10(p)")
    plt.xticks(np.arange(len(pivot.columns)), pivot.columns, rotation=35, ha="right")
    plt.yticks(np.arange(len(pivot.index)), pivot.index)
    plt.title(f"Paired sign-test p-values ({language})")
    for i in range(p.shape[0]):
        for j in range(p.shape[1]):
            if not math.isnan(p[i, j]):
                plt.text(j, i, f"{p[i, j]:.3f}", ha="center", va="center", fontsize=7)
    save_current(name)


def plot_entity_accuracy():
    df = pd.read_csv(SUMMARY / "table6_cross_model_class_level_long.csv")
    df = df[df["label"] == "ENTITY"].copy()
    bar_by_language(df, "accuracy", "ENTITY accuracy by model", "ENTITY accuracy", "entity_accuracy_by_model", (0.0, 1.05))


def main():
    plot_progression()
    plot_cross_model_bars()
    plot_class_heatmap()
    plot_pvalue_heatmap("Arabic", "pairwise_pvalue_heatmap_arabic")
    plot_pvalue_heatmap("English", "pairwise_pvalue_heatmap_english")
    plot_entity_accuracy()
    print("Figures written to", FIG)


if __name__ == "__main__":
    main()
