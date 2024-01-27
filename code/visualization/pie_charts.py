import plotly.graph_objects as go


def plot_attribution_by_value_distribution(
    data,
    title,
):
    categories = list(data.keys())
    values = list(data.values())

    fig = go.Figure(
        data=[
            go.Pie(
                labels=categories,
                values=values,
                marker_colors=["#107c54", "#ecb13c", "blue"],
            ),
        ],
    )
    fig.update_layout(title=title)

    pie_chart_html = fig.to_html(full_html=False)

    return pie_chart_html
