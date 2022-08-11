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
    # アンケートの結果を格納する
    if 'user_questionnaire_results' not in st.session_state:
        st.session_state['user_questionnaire_results'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if 'personalized_user_information' not in st.session_state:
        st.session_state['personalized_user_information'] = {"x": 0, "y": 0, "size": 0}
    if 'num' not in st.session_state:
        st.session_state['num'] = 0
    #  アンケート結果を格納する
    if 'additional_user_questionnaire_results' not in st.session_state:
        st.session_state['additional_user_questionnaire_results'] =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if 'submit_results' not in st.session_state:
        st.session_state['submit_results'] = False
    if 'display_times' not in st.session_state:
        st.session_state['display_times'] = 0

    st.title('カテゴライズ')

    # 会社データの読み込み
    path_company_data = 'company_data.csv'
    df = pd.read_csv(path_company_data)

    # 自身のデータを表示
    #Takuyaはユーザ名
    user_data = {'industry':'you','company_name':'Takuya','x':0,'y':0,'employee_number':0,'sales':0,'recommendation':350}

    #TODO:大きさをを変化させる
    # you["recommendation"] = 100

    df_user = df.append(user_data, ignore_index=True)
    # print("aaaaaaaaa")
    # print(df_user)



    #TODO: データの書き換え







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
    xmin = user_data['x']-500
    xmax = user_data['x']+500
    ymin = user_data['y']-500
    ymax = user_data['y']+500

    fig=px.scatter(df_user, x="x", y="y", size="recommendation", color="industry",hover_name="company_name",range_x=[xmin,xmax],range_y=[ymin,ymax],size_max=user_data['recommendation'])






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

    user_data['x'] += 10
    user_data['y'] += 10
    df_user = df.append(user_data, ignore_index=True)
    user_data["recommendation"] -= 10
    if user_data['recommendation'] < 20:
        user_data["recommendation"] = 20
    fig=px.scatter(df_user, x="x", y="y", size="recommendation", color="industry",hover_name="company_name",range_x=[xmin,xmax],range_y=[ymin,ymax],size_max=user_data['recommendation'])
    st.plotly_chart(fig, use_container_width=True)


    #レーダーチャートの表示
    st.title('個人最適化された評価軸')
    st.write('値が大きな軸があなたが就職する会社を決める際の最適な評価軸です．')
    radar_list = []
    theta_list = ['やりがい','裁量権','成長環境','企画', '福利厚生']
    for i in theta_list:
        if i == "福利厚生":
            radar_list.append(1)
        else:
            radar_list.append(random.randint(1,5))
    df = pd.DataFrame(dict(r=radar_list, theta=theta_list))
    fig_radar = px.line_polar(df, r='r', theta='theta', line_close=True)
    st.plotly_chart(fig_radar, use_container_width=True)


if __name__ == '__main__':
    main()