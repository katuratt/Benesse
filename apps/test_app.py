import streamlit as st
import pandas as pd
import numpy as np


def app():
    # 東京のランダムな経度・緯度を生成する
    data = {
        'lat': np.random.randn(100) / 100 + 35.68,
        'lon': np.random.randn(100) / 100 + 139.75,
    }
    map_data = pd.DataFrame(data)
    # 地図に散布図を描く
    st.map(map_data)


if __name__ == '__main__':
    app()