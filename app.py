import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="Nassau Candy Factory Dashboard",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 Factory Location and Geographical Analysis")

st.write(
    "This dashboard displays the geographical locations "
    "of Nassau Candy manufacturing factories."
)

# -----------------------------------
# FACTORY DATA
# -----------------------------------

factory_data = {
    "Factory": [
        "Lot's O' Nuts",
        "Wicked Choccy's",
        "Sugar Shack",
        "Secret Factory",
        "The Other Factory"
    ],

    "Latitude": [
        32.881893,
        32.076176,
        48.11914,
        41.446333,
        35.1175
    ],

    "Longitude": [
        -111.768036,
        -81.088377,
        -96.18115,
        -90.565487,
        -89.971107
    ]
}

factory_df = pd.DataFrame(factory_data)

# -----------------------------------
# KPI CARDS
# -----------------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Factories",
    len(factory_df)
)

col2.metric(
    "Latitude Available",
    factory_df["Latitude"].notna().sum()
)

col3.metric(
    "Longitude Available",
    factory_df["Longitude"].notna().sum()
)

st.divider()

# -----------------------------------
# INTERACTIVE FACTORY MAP
# -----------------------------------

st.subheader("1. Interactive Factory Location Map")

fig = px.scatter_geo(
    factory_df,
    lat="Latitude",
    lon="Longitude",
    hover_name="Factory",
    hover_data={
        "Latitude": ':.6f',
        "Longitude": ':.6f'
    },
    text="Factory",
    scope="usa",
    projection="albers usa",
    title="Geographical Distribution of Nassau Candy Factories"
)

fig.update_traces(
    marker=dict(
        size=13,
        color="red",
        line=dict(width=1, color="black")
    ),
    textposition="top center"
)

fig.update_layout(
    height=600,
    margin=dict(l=20, r=20, t=60, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------
# FACTORY DETAILS TABLE
# -----------------------------------

st.subheader("2. Factory Coordinates Details")

st.dataframe(
    factory_df,
    use_container_width=True,
    hide_index=True
)

# -----------------------------------
# FACTORY LOCATION BAR CHART
# -----------------------------------

st.subheader("3. Factory Latitude Comparison")

fig2 = px.bar(
    factory_df,
    x="Factory",
    y="Latitude",
    color="Factory",
    title="Latitude of Each Factory",
    text="Latitude"
)

fig2.update_layout(
    xaxis_title="Factory Name",
    yaxis_title="Latitude",
    showlegend=False
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------------
# FACTORY LOCATION FILTER
# -----------------------------------

st.subheader("4. Individual Factory Details")

selected_factory = st.selectbox(
    "Select a Factory",
    factory_df["Factory"]
)

selected_data = factory_df[
    factory_df["Factory"] == selected_factory
]

st.write("Selected Factory Information")

st.dataframe(
    selected_data,
    use_container_width=True,
    hide_index=True
)

# -----------------------------------
# PROJECT ANALYSIS
# -----------------------------------

st.subheader("5. Geographical Analysis Summary")

st.write("""
- Five factory locations are included in this analysis.
- Latitude and longitude coordinates identify
  the geographical positions of the factories.
- The interactive map helps visualize factory distribution.
- This information can support further geographical,
  customer-region and distribution analysis.
""")

st.success("Factory Location Dashboard Loaded Successfully!")


