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

    # First moon
    t = np.linspace(0, np.pi, n_points_per_moon)
    x1 = width * np.sin(t)
    y1 = height * np.cos(t) + separation

    # Second moon
    x2 = width * np.sin(t) + width
    y2 = -height * np.cos(t) - separation

    # Combine into arrays
    x = np.concatenate([x1, x2])
    y = np.concatenate([y1, y2])
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
