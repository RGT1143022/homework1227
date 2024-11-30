import streamlit as st
import pandas as pd
from scrape_bwf_ranking import scrape_bwf_ranking  # 引入爬蟲腳本

# 設定頁面標題
st.title("BWF Men's Singles World Ranking")

# 當按下按鈕時，抓取資料並顯示
if st.button("Get Ranking"):
    try:
        # 執行爬蟲並取得排名資料
        df = scrape_bwf_ranking()

        # 顯示排名資料
        st.write("Below is the BWF Men's Singles World Ranking:", df)

        # 如果需要，還可以提供下載 CSV 檔案的功能
        st.download_button(
            label="Download CSV",
            data=df.to_csv(index=False),
            file_name="bwf_ranking.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"Error occurred: {e}")
