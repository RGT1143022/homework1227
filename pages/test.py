import folium
import streamlit as st
from streamlit_folium import st_folium


# 創建地圖
m = folium.Map(location=[0, 0], zoom_start=2)

# 在 Streamlit 中顯示地圖
output = st_folium(m, width=700, height=500, key="map1")

st.write(output['center'])
