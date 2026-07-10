# Example Dataset

This folder is intended to contain example molecular dynamics files for testing Dynastra.

The original trajectory files are not included due to file size limitations.

Required files:

- md.tpr
- md.xtc (or md_NJ.xtc)

Users can place their own GROMACS trajectories in this directory and run:

```bash
python run_analysis.py
