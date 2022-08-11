import streamlit as st
import plotly.express as px
import time
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.datasets import load_boston
import csv
import plotly.graph_objects as go
import altair as alt
from vega_datasets import data
import random

def main():
    if 'radar_list' not in st.session_state:
        st.session_state['radar_list'] = []

    st.title('カテゴライズ')
    st.write('個人最適化された自己分析手法をもとに，あなたをカテゴライズしました．')
    st.write('あなたの円の中に入っている企業が，個人最適化された評価軸で最適とされた企業です．')
    st.write('あなたの円が大きい場合は，自己分析を進めて，あなたの円を小さくしていきましょう．')

    # 会社データの読み込み
    path_company_data = 'data/company_data.csv'
    df = pd.read_csv(path_company_data)

    # 自身のデータを表示
    #Takuyaはユーザ名
    user_data = {'industry':'you','company_name':'Takuya','x':300,'y':200,'employee_number':0,'sales':0,'recommendation':350}


    #TODO:業種選択画面作成
    # st.write('検索')
    # industry_list = ['Education', 'Agricultural','Mining','Manufacturing','Construction','Finance']
    # company_name = st.selectbox('業界選択',("未選択",industry_list[0], industry_list[1],industry_list[2], industry_list[3],industry_list[4], industry_list[5]), key="3", index=0)


    # company_name=st.text_input('会社名')
    # personal_name = st.text_input('産業', '教育')


    # TODO:業種・会社選択用
    # company_name = 'ukf'
    # df_user_ano=df_user[df_user['company_name'] == company_name]#表示するバブルの指定
    # print(df_user_ano)
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


    st.sidebar.title('軸の設定')
    xmin = 0
    xmax = 1000
    ymin = 0
    ymax = 1000

    # 本来は多次元空間の情報を2次元に落とすことで，ユーザの円の位置，半径の大きさを決定する
    # ここでは，それっぽい機能だけ作成する
    # フィードバックのデータの数を調べる
    feedbacked_info_number = 0
    # 自己分析からのフィードバック数を調べる
    if 'user_questionnaire_results' in st.session_state:
        for i in st.session_state['user_questionnaire_results']:
            print(i)
            if i != 1 and i != 0:
                feedbacked_info_number += 1
        print("aaaaaaaaaa")
        print(feedbacked_info_number)
    # 会社体験からのフィードバック数を調べる
    if 'additional_user_questionnaire_results' in st.session_state:
        for i in st.session_state['additional_user_questionnaire_results']:
            if i != 0 and i != 1:
                feedbacked_info_number += 1
        print("bbbbbbbbbb")
        print(feedbacked_info_number)
    print("cccccccccc")
    print(feedbacked_info_number)

    #TODO:大きさの調節
    user_data['x'] = 350
    user_data['y'] = 400
    user_data["recommendation"] = 300
    df_user = df.append(user_data, ignore_index=True)
    fig=px.scatter(df_user, x="x", y="y", size="recommendation", color="industry",hover_name="company_name",range_x=[xmin,xmax],range_y=[ymin,ymax],size_max=user_data['recommendation'])
    st.plotly_chart(fig, use_container_width=True)


    #レーダーチャートの表示
    st.title('個人最適化された評価軸')
    st.write('値が大きな軸があなたが就職する会社を決める際の最適な評価軸です．')
    radar_list = []
    theta_list = ['やりがい','裁量権','成長環境','社会貢献', '福利厚生']
    for i in theta_list:
        if i == "福利厚生":
            radar_list.append(0.5)
        else:
            radar_list.append(random.randint(1,4))
    # 企業体験からのフィードバックを反映させる
    for i in st.session_state['radar_list']:
        for j in range(len(theta_list)):
            if theta_list[j] in i:
                radar_list[j] = 5.0

    df = pd.DataFrame(dict(r=radar_list, theta=theta_list))
    fig_radar = px.line_polar(df, r='r', theta='theta', line_close=True)
    st.plotly_chart(fig_radar, use_container_width=True)

if __name__ == '__main__':
    main()