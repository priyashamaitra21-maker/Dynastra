import subprocess
from pathlib import Path


def calculate_rg(
    tpr,
    xtc,
    output="rg.xvg",
    group=1,
):

    command = (
        f'echo "{group}" | '
        f'gmx gyrate '
        f'-s "{tpr}" '
        f'-f "{xtc}" '
        f'-o "{output}"'
    )

    subprocess.run(
        command,
        shell=True,
        check=True
    )

    print(f"Radius of Gyration written to {output}")

    return Path(output)
