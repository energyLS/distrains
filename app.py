import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px

st.set_page_config(page_title="Whisky Distilleries & Train Distances", layout="wide")

# st.balloons()

st.title("WHISKY DISTILLERIES AND THE DISTANCE TO THEIR CLOSEST TRAIN STOP")

@st.cache_data

def load_distrains():
    return gpd.read_file("output/distilleries_result.geojson", index_col=0)


ppl = load_distrains()


with st.sidebar:
    st.title("DISTRAINS")

    st.markdown("This dashboard visualizes the 'DISTRAINS' project.")

    st.header("Data Adjustments")

    tech = st.selectbox(
        "Whisky Type",
        ppl.Description.unique(),
    )

    dist_min, dist_max = st.slider(
        "Range of distance in m", 0, 130000, (0, 130000), step=1, help="Pick distance!"
    )

    st.header("Map Adjustments")

    size = st.slider(
        "Size of the bubbles", 5, 20, (10), step=1, help="Pick a size!"
    )

    color_custom = st.color_picker(
        "Color of the bubbles", '#00441b', help="Pick a color!"
    )

    st.header("Documentation")

    st.markdown("Find the code and some fun statistics on [GitHub](https://github.com/energyLS/distrains).")

#st.warning(":building_construction: Sorry, this page is still under construction")

hover_data = {'Name': False,
            'Description': True, 
            'Trainstop': True, 
            'Distance in m': True,
            'lat': False,
            'lon': False,
            'size': False,
            }

df = ppl.query("Description == @tech and `Distance in m` >= @dist_min and `Distance in m` <= @dist_max")
df['lon'] = df['geometry'].x
df['lat'] = df['geometry'].y
df['size'] = 20

#df = ppl.query("Fueltype == @tech and DateIn >= @start and DateIn <= @end")

if not df.empty:
    fig = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lon",
        mapbox_style="carto-darkmatter",
        color="Distance in m",
        color_continuous_scale= [[0, color_custom], [1, 'white']], #[[0, '#00441b'], [0.5, '#72c375'], [1, 'white']],
        #color_continuous_scale= [[0, '#00441b'], [0.5, '#72c375'], [1, 'white']],
        size="size",
        size_max=size,
        zoom=5,
        height=700,
        hover_data=hover_data,
        hover_name="Name",
        #range_color=(1900, 2022),
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("Sorry, no data to display!")
