import base64
from io import BytesIO

import matplotlib.pyplot as plt


def plot_attribution_by_value_distribution(
    data,
    enum_class,
    x_label,
    y_label,
    title,
):
    labels = [level.name for level in enum_class]
    counts = [data.get(level.value, 0) for level in enum_class]

    plt.figure(figsize=(10, 6))
    plt.bar(labels, counts, color="#107c54", hatch="|", edgecolor="black", width=0.5)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    return base64.b64encode(image_png).decode("utf-8")
