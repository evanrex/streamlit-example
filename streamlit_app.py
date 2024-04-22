import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from sklearn.datasets import make_moons

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


# Slider for number of points
num_points = st.slider("Number of points in dataset", 100, 10000, 1100)

# Load the twin moons dataset
x, y = make_moons(n_samples=num_points, noise=0.1)

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
