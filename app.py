import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Whisky Distilleries & Train Distances", layout="wide")

st.title("WHISKY DISTILLERIES AND THE DISTANCE TO THEIR CLOSEST TRAIN STOPS")

@st.cache_data

def load_distrains():
    return gpd.read_file("output/distilleries_result.geojson", index_col=0)

distrains = load_distrains()

# Change Distance in m to Distance in km
distrains['Distance in m'] = distrains['Distance in m'] / 1000
distrains.rename(columns={'Distance in m': 'Distance in km'}, inplace=True)


with st.sidebar:
    st.title("DISTRAINS")

    st.markdown("This dashboard visualizes the 'DISTRAINS' project.")

    st.header("Data Adjustments")

    whisky_type = st.selectbox(
        "Whisky Type",
        np.insert(distrains.Description.unique(), 0, "All"),
    )

    dist_min, dist_max = st.slider(
        "Range of distance in km", 0, 130, (0, 130), step=1, help="Pick distance"
    )

    st.header("Map Adjustments")

    size = st.slider(
        "Size of the dots", 5, 15, (8), step=1, help="Pick a size"
    )

    color_custom = st.color_picker(
        "Color of the bubbles", '#00441b', help="Pick a color"
    )

    st.header("Documentation")

    st.markdown("Find the code and some fun statistics on [GitHub](https://github.com/energyLS/distrains).")
    # Placeholder
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

#st.warning(":building_construction: Sorry, this page is still under construction")

hover_data = {'Name': False,
            'Description': True, 
            'Trainstop': True, 
            'Distance in km': True,
            'lat': False,
            'lon': False,
            'size': False,
            }

if whisky_type == "All":
    df = distrains.query("`Distance in km` >= @dist_min and `Distance in km` <= @dist_max")
else:
    df = distrains.query("Description == @whisky_type and `Distance in km` >= @dist_min and `Distance in km` <= @dist_max")

df['lon'] = df['geometry'].x
df['lat'] = df['geometry'].y
df['size'] = 20

if not df.empty:
    fig = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lon",
        mapbox_style="carto-darkmatter",
        color="Distance in km",
        color_continuous_scale= [[0, color_custom], [1, 'white']], #[[0, '#00441b'], [0.5, '#72c375'], [1, 'white']],
        #color_continuous_scale= [[0, '#00441b'], [0.5, '#72c375'], [1, 'white']],
        size="size",
        size_max=size,
        zoom=5,
        height=700,
        hover_data=hover_data,
        hover_name="Name",
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("Sorry, no data to display. Please adjust your filters.")