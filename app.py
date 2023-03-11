import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px

st.set_page_config(page_title="Whisky Distilleries & Train Distances", layout="wide")

# st.balloons()

st.title("WHISKY DISTILLERIES AND THEIR CLOSEST TRAIN STOP DISTANCE")


@st.cache_data

def load_distrains():
    return gpd.read_file("output/distilleries_result.geojson", index_col=0)


ppl = load_distrains()


with st.sidebar:
    st.title("DISTRAINS")

    st.markdown(":+1: This dashboard visualizes the 'DISTRAINS' project")

    tech = st.selectbox(
        "Whisky Type",
        ppl.Description.unique(),
    )

    start, end = st.slider(
        "Range of commissioning years", 1900, 2022, (1900, 2022), step=1, help="Pick years!"
    )

st.warning(":building_construction: Sorry, this page is still under construction")

hover_data = {'Name': False,
              'Description': True, 
              'Trainstop': True, 
              'Distance in m': True,
              'lat': False,
              'lon': False,
              }

df = ppl.query("Description == @tech")
df['lon'] = df['geometry'].x
df['lat'] = df['geometry'].y

#df = ppl.query("Fueltype == @tech and DateIn >= @start and DateIn <= @end")

if not df.empty:
    fig = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lon",
        mapbox_style="carto-darkmatter",
        color="Distance in m",
        color_continuous_scale=[[0, '#00441b'], [0.5, '#72c375'], [1, 'white']],
        size="Distance in m",
        zoom=5,
        height=700,
        hover_data=hover_data,
        hover_name="Name",
        #range_color=(1900, 2022),
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("Sorry, no data to display!")
