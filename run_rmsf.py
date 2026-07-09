from dynastra.rmsf import calculate_rmsf

calculate_rmsf(
    "examples/test1/md.tpr",
    "examples/test1/md_NJ.xtc",
    output="rmsf_python.xvg"
)
