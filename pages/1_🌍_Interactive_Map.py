import streamlit as st
import leafmap.foliumap as leafmap
from streamlit_folium import st_folium

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)


st.title("Interactive Map")

col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")

with col2:

    basemap = st.selectbox("Select a basemap:", options, index)


with col1:

    m = leafmap.Map(
        locate_control=True, latlon_control=True, draw_export=True, minimap_control=True
    )
    m.add_basemap(basemap)

    #m.to_streamlit(height=700)
    # 嵌入地圖到 Streamlit 並返回互動結果
    output = st_folium(m, height=700)

    # 如果用戶與地圖交互，獲取顯示邊界
    if output and "bounds" in output:
        st.write("地圖顯示邊界:", output["bounds"])



# # 建立地圖
# m=leafmap.Map(center=[40, -100], zoom=4)
# m.to_streamlit(height=700)
# # 獲取地圖的顯示邊界
# bounds = m.st_map_bounds()

# # 顯示地圖和邊界
# st.write("地圖範圍:", bounds)
import streamlit as st
from streamlit_folium import st_folium
import folium

# 建立 Folium 地圖
#m = folium.Map(location=[40, -100], zoom_start=4)
m = leafmap.Map(location=[40, -100], zoom_start=4)

# 嵌入地圖到 Streamlit 並返回互動結果
output = st_folium(m, height=700)

# 如果用戶與地圖交互，獲取顯示邊界
if output and "bounds" in output:
    st.write("地圖顯示邊界:", output["bounds"])

