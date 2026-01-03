#!/usr/bin/env python
"""
Pipeline runner.
"""
import subprocess
from pathlib import Path

def main():
    workspace = Path.cwd()
    print(f"Workspace: {workspace}")
    
    scripts = [
        ("statim_parser.py", "Parsing STATIM TXT files"),
        ("ritter_pdf_to_txt.py", "Converting Ritter PDFs to text"),
        ("ritter_txt_to_csv.py", "Converting Ritter text to CSV"),
        ("merged2.py", "Statistical analysis"),
        ("report2.py", "Generating PDF report")
    ]
    
    for script_name, description in scripts:
        print(f"\n🚀 Running: {description}")
        script_path = workspace / "scripts" / ("parsing_codes" if "ritter" in script_name or "statim" in script_name else "statistics_codes") / script_name
        
        if script_path.exists():
            subprocess.run(["python", str(script_path)])
        else:
            print(f"⚠️  Script not found: {script_name}")

if __name__ == "__main__":
    main()
