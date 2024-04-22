import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


def generate_twin_moons(n_points, separation=0.5, width=0.6, height=0.2):
    n_points_per_moon = n_points // 2

    outer_circ_x = np.cos(np.linspace(0, np.pi, n_points_per_moon))
    outer_circ_y = np.sin(np.linspace(0, np.pi, n_points_per_moon))
    inner_circ_x = 1 - np.cos(np.linspace(0, np.pi, n_points_per_moon))
    inner_circ_y = 1 - np.sin(np.linspace(0, np.pi, n_points_per_moon)) - 0.5

    x = np.vstack(
        [np.append(outer_circ_x, inner_circ_x), np.append(outer_circ_y, inner_circ_y)]
    ).T
    y = np.hstack(
        [np.zeros(n_points_per_moon, dtype=np.intp), np.ones(n_points_per_moon, dtype=np.intp)]
    )
    labels = np.array([0] * n_points_per_moon + [1] * n_points_per_moon)

    return x, y, labels

# Slider for number of points
num_points = st.slider("Number of points in dataset", 100, 2000, 1100)

# Generate data
x, y, labels = generate_twin_moons(num_points)

# Create a DataFrame
df = pd.DataFrame({
    "x": x[:, 0],
    "y": x[:, 1],
    "label": y
})

# Visualization
st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("label:N", legend=None),  # Use label for color encoding
        tooltip=['x', 'y', 'label']  # Optional: add tooltip for more interactivity
    ))
