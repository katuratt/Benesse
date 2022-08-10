import streamlit as st
import plotly.express as px
import time
import numpy as np
from matplotlib import pyplot as plt


def main():
    st.title('業界・会社体験')

    # path_image = '../data/test.jpg'
    image = Image.open('test.jpg')
    st.image(image, caption = 'This is a picture', use_column_width = True)
    # グラフを書き出すためのプレースホルダを用意する
    plot_area = st.empty()
    fig = plt.figure()
    ax = fig.add_subplot()
    x = np.random.normal(loc=.0, scale=1., size=(100,))
    ax.plot(x)
    # プレースホルダにグラフを書き込む
    plot_area.pyplot(fig)

    # 折れ線グラフに 0.5 秒間隔で 10 回データを追加する
    for i in range(10):
        # グラフを消去する
        ax.clear()
        # データを追加する
        additional_data = np.random.normal(loc=.0, scale=1., size=(10,))
        x = np.concatenate([x, additional_data])
        # グラフを描画し直す
        ax.plot(x)
        # プレースホルダに書き出す
        plot_area.pyplot(fig)
        time.sleep(0.2)


if __name__ == '__main__':
    main()
