#!/usr/bin/env python
"""
Setup script for Colab environment.
"""
import os
from pathlib import Path

def setup_colab_environment():
    workspace = Path.cwd()
    print(f"Workspace: {workspace}")
    
    dirs_to_create = [
        "scripts/parsing_codes",
        "scripts/statistics_codes",
        "data/raw/pdfs",
        "data/raw/txts",
        "data/processed",
        "output",
        "reports"
    ]
    
    for dir_path in dirs_to_create:
        (workspace / dir_path).mkdir(parents=True, exist_ok=True)
    
    print("✅ Environment setup complete")
    return workspace

if __name__ == "__main__":
    setup_colab_environment()
