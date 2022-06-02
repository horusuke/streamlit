import pandas as pd
import time
import pydeck as pdk
import streamlit as st
import numpy as np
import folium
import plotly.express as px
from streamlit_folium import folium_static


df = pd.read_csv('../データ/ヤマップ.csv')

#高さを選んでください
height = st.slider('高さをえらんでください?', 0, 4000, 4000)
name = st.text_input('登りたい山を入力してください')
df = df[df['高さ２'] <= height]
if name=='':
    df = df
else:
    df = df[df['名前'] == name]

st.dataframe(df) 


map = folium.Map(location=[35.736489,139.746875], zoom_start=5)
 
for i, r in df.iterrows():
    try:
        folium.Marker(location=[r['lon'], r['lat']], popup=r['名前']).add_to(map)
    except:
        folium.Marker(location=[0, 0], popup=r['名前']).add_to(map)
    print(i)

folium_static(map) # 地図情報を表示
