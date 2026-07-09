import subprocess
from pathlib import Path


def calculate_rmsd(
    tpr,
    xtc,
    output="rmsd.xvg",
    fit_group=1,
    rms_group=1,
):

    command = (
        f'echo "{fit_group} {rms_group}" | '
        f'gmx rms '
        f'-s "{tpr}" '
        f'-f "{xtc}" '
        f'-o "{output}"'
    )

    subprocess.run(
        command,
        shell=True,
        check=True
    )

    print(f"RMSD written to {output}")

    return Path(output)
