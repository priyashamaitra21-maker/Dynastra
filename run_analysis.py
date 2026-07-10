from pathlib import Path

from dynastra.rmsd import calculate_rmsd
from dynastra.rmsf import calculate_rmsf
from dynastra.rg import calculate_rg
from dynastra.sasa import calculate_sasa
from dynastra.plotting import plot_xvg

tpr = "examples/test1/md.tpr"
xtc = "examples/test1/md_NJ.xtc"

# Create outputs directory
Path("outputs").mkdir(exist_ok=True)

print("Running RMSD...")
calculate_rmsd(
    tpr,
    xtc,
    output="outputs/rmsd.xvg"
)

plot_xvg(
    "outputs/rmsd.xvg",
    "outputs/rmsd.png",
    "Time (ps)",
    "RMSD (nm)",
    "Protein RMSD"
)

print("Running RMSF...")
calculate_rmsf(
    tpr,
    xtc,
    output="outputs/rmsf.xvg"
)

plot_xvg(
    "outputs/rmsf.xvg",
    "outputs/rmsf.png",
    "Residue",
    "RMSF (nm)",
    "Protein RMSF"
)

print("Running Radius of Gyration...")
calculate_rg(
    tpr,
    xtc,
    output="outputs/rg.xvg"
)

plot_xvg(
    "outputs/rg.xvg",
    "outputs/rg.png",
    "Time (ps)",
    "Rg (nm)",
    "Radius of Gyration"
)

print("Running SASA...")
calculate_sasa(
    tpr,
    xtc,
    output="outputs/sasa.xvg",
    dt=500
)

plot_xvg(
    "outputs/sasa.xvg",
    "outputs/sasa.png",
    "Time (ps)",
    "SASA (nm²)",
    "Solvent Accessible Surface Area"
)

print("Analysis completed.")
