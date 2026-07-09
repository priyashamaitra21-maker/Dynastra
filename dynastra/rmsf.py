import subprocess
from pathlib import Path


def calculate_rmsf(
    tpr,
    xtc,
    output="rmsf.xvg",
    group=1,
):

    command = (
        f'echo "{group}" | '
        f'gmx rmsf '
        f'-s "{tpr}" '
        f'-f "{xtc}" '
        f'-o "{output}"'
    )

    subprocess.run(
        command,
        shell=True,
        check=True
    )

    print(f"RMSF written to {output}")

    return Path(output)
