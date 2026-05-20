#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]; RESULTS=ROOT/"results"; OUT=RESULTS/"summary_tables"; OUT.mkdir(parents=True,exist_ok=True)
frames=[]
for p in (RESULTS/"metrics").glob("metrics_*.csv"):
    frames.append(pd.read_csv(p))
if frames:
    pd.concat(frames,ignore_index=True).to_csv(OUT/"all_metrics_collected.csv",index=False)
print("Summary tables are stored in", OUT)
