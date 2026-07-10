import pandas as pd
import matplotlib.pyplot as plt


def read_xvg(filename):
    data = []

    with open(filename) as f:
        for line in f:
            if line.startswith("#"):
                continue

            if line.startswith("@"):
                continue

            values = line.split()
            data.append([float(v) for v in values])

    return pd.DataFrame(data)


def plot_xvg(
    xvg_file,
    output_png,
    xlabel,
    ylabel,
    title,
):
    df = read_xvg(xvg_file)

    plt.figure(figsize=(8, 5))
    plt.plot(df[0], df[1], linewidth=2)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    plt.tight_layout()
    plt.savefig(output_png, dpi=300)
    plt.close()

    print(f"Plot saved: {output_png}")
