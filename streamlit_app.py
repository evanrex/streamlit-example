import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

"""
# Welcome to the Two Moons visualisation with Streamlit!


Explore the Two Moons dataset by adjusting the noise and number of points.

This follows the [sci-kit learn implemention](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#sklearn-datasets-make-moons).

"""


def generate_twin_moons(n_points, noise=0.1, separation=0.5, width=0.6, height=0.2):
    n_points_per_moon = n_points // 2

    outer_circ_x = np.cos(np.linspace(0, np.pi, n_points_per_moon))
    outer_circ_y = np.sin(np.linspace(0, np.pi, n_points_per_moon))
    inner_circ_x = 1 - np.cos(np.linspace(0, np.pi, n_points_per_moon))
    inner_circ_y = 1 - np.sin(np.linspace(0, np.pi, n_points_per_moon)) - 0.5

    # Combine and add random noise
    x = np.concatenate([outer_circ_x, inner_circ_x])
    x += np.random.normal(0, noise, len(x))
    y = np.concatenate([outer_circ_y, inner_circ_y]) 
    y += np.random.normal(0, noise, len(y))
    labels = np.array([0] * n_points_per_moon + [1] * n_points_per_moon)

    return x, y, labels

# Slider for number of points
num_points = st.slider("Number of points per moon in dataset", 100, 2000, 1100)

# Slider for noise level
noise_level = st.slider("Noise level", 0.0, 0.5, 0.1)

# Generate data
x, y, labels = generate_twin_moons(num_points, noise=noise_level)

# Create DataFrame
df = pd.DataFrame({
    "x": x,
    "y": y,
    "label": labels
})

# Visualization
st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("label:N", legend=None),
        tooltip=['x', 'y', 'label']  # Optional: add tooltip for more interactivity
    ))
