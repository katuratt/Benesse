import streamlit as st
import plotly.express as px
import time
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.datasets import load_boston
# import seaborn as sns
import csv

import plotly.graph_objects as go



def main():
    st.title('カテゴライズ')

    path_company_data = 'company_data.csv'
    df = pd.read_csv(path_company_data)

    print(df)
    print(type(df))


    # 自身のデータを表示
    #Takuyaはユーザ名
    you = {'industry':'you','company_name':'Takuya','x':0,'y':0,'employee_number':0,'sales':0,'recommendation':350}

    #TODO:大きさをを変化させる
    # you["recommendation"] = 100

    df_user = df.append(you, ignore_index=True)
    print("aaaaaaaaa")
    print(df_user)



    #TODO: データの書き換え
    # for j in range(100):
    #     # 0.1 秒間隔で データを書き換える
    #     you["x"] = 10 * j
    #     you["y"] = 10 * j
    #     df_user = df.append(you, ignore_index=True)
    #     time.sleep(0.1)






    #TODO:業種選択画面作成
    # st.write('検索')
    # industry_list = ['Education', 'Agricultural','Mining','Manufacturing','Construction','Finance']
    # company_name = st.selectbox('業界選択',("未選択",industry_list[0], industry_list[1],industry_list[2], industry_list[3],industry_list[4], industry_list[5]), key="3", index=0)


    # company_name=st.text_input('会社名')
    # personal_name = st.text_input('産業', '教育')



    st.sidebar.title('軸の設定')
    # xmin=st.sidebar.number_input('x最小値：',0,500,300)
    # xmax=st.sidebar.number_input('x最大値：',0,1000,400)
    # ymin=st.sidebar.number_input('y最小値：',0,500,200)
    # ymax=st.sidebar.number_input('y最大値：',0,1000,300)
    xmin = you['x']-500
    xmax = you['x']+500
    ymin = you['y']-500
    ymax = you['y']+500

    fig=px.scatter(df_user, x="x", y="y", size="recommendation", color="industry",hover_name="company_name",range_x=[xmin,xmax],range_y=[ymin,ymax],size_max=you['recommendation'])




    company_name = 'ukf'
    df_user_ano=df_user[df_user['company_name'] == company_name]#表示するバブルの指定
    print(df_user_ano)

    # TODO:業種・会社選択用
    # fig.add_annotation(
    #     x=df_user_ano.iloc[0,2],
    #     y=df_user_ano.iloc[0,3],
    #     xref="x",
    #     yref="y",
    #     text=company_name,
    #     showarrow=True,
    #     font=dict(
    #         family="Courier New, monospace",
    #         size=22,
    #         color="#ffffff"
    #         ),
    #     align="center",
    #     arrowhead=2,
    #     arrowsize=1,
    #     arrowwidth=2,
    #     arrowcolor="#636363",
    #     ax=20,
    #     ay=-30,
    #     bordercolor="#c7c7c7",
    #     borderwidth=2,
    #     borderpad=4,
    #     bgcolor="#ff7f0e",
    #     opacity=0.8
    #     )

    st.plotly_chart(fig, use_container_width=True)






    #TODO 時系列変化するグラフの参考
    # 折れ線グラフ (初期状態)
    x = np.random.random(size=(10, 2))
    line_chart = st.line_chart(x)

    for i in range(10):
        # 折れ線グラフに 0.5 秒間隔で 10 回データを追加する
        additional_data = np.random.random(size=(5, 2))
        line_chart.add_rows(additional_data)
        time.sleep(0.5)
    # #TODO 時系列変化するグラフの参考2
    # # 折れ線グラフに 0.5 秒間隔で 10 回データを追加する
    # for i in range(10):
    #     # グラフを消去する
    #     ax.clear()
    #     # データを追加する
    #     additional_data = np.random.normal(loc=.0, scale=1., size=(10,))
    #     x = np.concatenate([x, additional_data])
    #     # グラフを描画し直す
    #     ax.plot(x)
    #     # プレースホルダに書き出す
    #     plot_area.pyplot(fig)
    #     time.sleep(0.2)





    #レーダーチャートの表示
    #TODO: フィードバックにより，変化させる
    st.title('個人最適化された評価軸')
    st.write('値が大きな軸があなたに最適な評価軸です．')
    df = pd.DataFrame(dict(r=[3, 2, 2, 4, 1], theta=['やりがい','裁量権','成長環境','企画力', '福利厚生']))
    fig_radaer = px.line_polar(df, r='r', theta='theta', line_close=True)
    st.plotly_chart(fig_radaer, use_container_width=True)





if __name__ == '__main__':
    main()