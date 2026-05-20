#!/usr/bin/env python3
"""Compatibility wrapper: regenerate figures using generate_figures.py."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name("generate_figures.py")), run_name="__main__")
