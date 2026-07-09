from dynastra.rmsd import calculate_rmsd

calculate_rmsd(
    "examples/test1/md.tpr",
    "examples/test1/md_NJ.xtc",
    output="rmsd_python.xvg"
)
