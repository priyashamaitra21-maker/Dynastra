import subprocess
from pathlib import Path


def calculate_sasa(
    tpr,
    xtc,
    output="sasa.xvg",
    group=1,
    dt=1000,
):

    command = (
        f'echo "{group}" | '
        f'gmx sasa '
        f'-s "{tpr}" '
        f'-f "{xtc}" '
        f'-dt "{dt}" '
        f'-o "{output}"'
    )

    subprocess.run(
        command,
        shell=True,
        check=True
    )

    print(f"SASA written to {output}")

    return Path(output)
