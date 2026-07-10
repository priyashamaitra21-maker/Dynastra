from dynastra.sasa import calculate_sasa

calculate_sasa(
    "examples/test1/md.tpr",
    "examples/test1/md_NJ.xtc",
    output="sasa_python.xvg",
    dt=1000
)
