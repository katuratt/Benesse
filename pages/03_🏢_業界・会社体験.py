import streamlit as st
import plotly.express as px
import time
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import csv


from apps import generate_question

def main():
    #csvファイルから，追加の質問のデータを読み込み
    path_additional_questions = "data/additional_questions.csv"
    with open(path_additional_questions, 'r', encoding='utf_8') as csv_file:
        csv_reader = csv.reader(csv_file)
        additional_question_list = list(csv_reader)
    # print(additional_question_list)
    # print(additional_question_list[0])
    # print(additional_question_list[0][0])


    # アンケートの結果を格納する
    if 'user_questionnaire_results' not in st.session_state:
        st.session_state['user_questionnaire_results'] = np.zeros(15, dtype=int)
    if 'personalized_user_information' not in st.session_state:
        st.session_state['personalized_user_information'] = {"x": 0, "y": 0, "size": 0}
    if 'num' not in st.session_state:
        st.session_state['num'] = 0
    #  アンケート結果を格納する
    if 'additional_user_questionnaire_results' not in st.session_state:
        st.session_state['additional_user_questionnaire_results'] =  np.zeros(len(additional_question_list), dtype=int)
    if 'submit_results' not in st.session_state:
        st.session_state['submit_results'] = False
    if 'display_times' not in st.session_state:
        st.session_state['display_times'] = 0
    if 'radar_list' not in st.session_state:
        st.session_state['radar_list'] = []


    industry_list = ['Education', 'Agricultural','Mining','Manufacturing','Construction','Finance']
    experience = "未選択"

    # 体験のフィードバックを送信後に表示する
    if st.session_state['submit_results']:
        st.title('提出しました．あなたの評価軸がさらに個人最適化されています．確認してみてください．')

    if st.session_state['submit_results'] == False:
        st.title('業界・会社体験！')
        st.write('ここでは，業界の実際の様子をゲームを通じて体験したり，企業の実際の様子をインターンシップを通じて体験することができます')
        st.write('どの手段で体験しますか？')
        experience= st.selectbox('どの手段で体験しますか',("未選択", "業界の実際の様子をゲームを通じて体験する", "業界の実際の様子をVRを通じて体験する", "企業の実際の様子をインターンシップを通じて体験する"), key="30", index=0)

        if experience == "業界の実際の様子をゲームを通じて体験する":
            st.write('業界の実際の様子をゲームを通じて体験しよう！')
            st.write('業界を選択してください．あなたに個人最適化された評価軸順に業界は並んでいます')
            #TODO: 業界を個人最適化して並べ替える
            personalized_industry_list = industry_list

            industry = st.selectbox('業種選択',("未選択",personalized_industry_list[0], personalized_industry_list[1],personalized_industry_list[2], personalized_industry_list[3],personalized_industry_list[4], personalized_industry_list[5]), key="31", index=0)

            if industry != "未選択":
                message = "ゲームを通じて" + industry + "業界の体験をしよう"
                st.write(message)
                #TODO: 写真の差し替え
                # 注：全て使用しても良い写真を使っています．
                if industry == "Education":
                    image = Image.open('data/education.png')
                elif industry == "Construction":
                    image = Image.open('data/construction.png')
                elif industry == "Manufacturing":
                    image = Image.open('data/education.png')
                elif industry == "Agricultural":
                    image = Image.open('data/education.png')
                elif industry == "Mining":
                    image = Image.open('data/construction.png')
                elif industry == "Finance":
                    image = Image.open('data/education.png')
                else:
                    st.write('その他の業界には，現在対応していません．対応するまでお待ちください．')
                st.image(image, caption='業界体験ゲーム',use_column_width=True)

        #TODO: VRを作成し，体験できるようにする
        elif experience == "業界の実際の様子をVRを通じて体験する":
            st.write('業界の実際の様子をVRを通じて体験しよう！')
            st.write('業界を選択してください．あなたに個人最適化された評価軸順に業界は並んでいます')
            #TODO: 業界を個人最適化して並べ替える
            personalized_industry_list = industry_list

            industry = st.selectbox('業種選択',("未選択",personalized_industry_list[0], personalized_industry_list[1],personalized_industry_list[2], personalized_industry_list[3],personalized_industry_list[4], personalized_industry_list[5]), key="32", index=0)
            if industry != "未選択":
                message = "ゲームを通じて" + industry + "業界の体験をしよう"
                st.write(message)
                #TODO: 写真を動画に差し替える
                # 注：全てインターンシップなどで使用しても良い写真を使っています．
                if industry == "Education":
                    image = Image.open('data/education.png')
                elif industry == "Construction":
                    image = Image.open('data/construction.png')
                elif industry == "Manufacturing":
                    image = Image.open('data/education.png')
                elif industry == "Agricultural":
                    image = Image.open('data/education.png')
                elif industry == "Mining":
                    image = Image.open('data/construction.png')
                elif industry == "Finance":
                    image = Image.open('data/education.png')
                else:
                    st.write('その他の業界には，現在対応していません．対応するまでお待ちください．')
                st.image(image, caption='業界体験ゲーム',use_column_width=True)


        elif experience == "企業の実際の様子をインターンシップを通じて体験する":
            st.write('企業の実際の様子をインターンシップを通じて体験しよう！')
            st.write('企業を選択してください．あなたに個人最適化された評価軸順に企業は並んでいます')
            #TODO: 企業を個人最適化して並べ替える
            company_list = ["Beness","Aeness","Ceness","Deness","Eeness","Feness"]

            company_name = st.selectbox('企業選択',("未選択",company_list[0], company_list[1],company_list[2], company_list[3],company_list[4], company_list[5]), key="33", index=0)
            if company_name != "未選択":
                message = company_name + "のインターンシップに応募しますか？"
                option_internship = st.radio(message, ("応募しない", "応募する"), index=0, key= 34, horizontal=True)
                if option_internship == "応募する":
                    #csvよりデータを取得
                    path_user_data = "data/user_data.csv"
                    with open(path_user_data, newline='', encoding='utf_8') as f:
                        reader = csv.DictReader(f)
                        user_data_list = [row for row in reader]
                    # print(user_data_list[0])
                    # print("sssss")
                    # print(type(user_data_list[0]))
                    # print(user_data_list[0].keys())
                    # print(user_data_list[0]['last_name'])

                    # インターンシップの応募
                    #TODO: もっとイケてるUIにして，情報を増やす
                    internship_name = company_name + "  User-Based Digital Competition"
                    st.title(internship_name)
                    st.write('お名前')
                    st.write('漢字氏名  姓: ' + user_data_list[0]['last_name'] + ' 名: ' + user_data_list[0]['first_name'])
                    st.write('カナ氏名  セイ: ' + user_data_list[0]['last_name_katakana'] + ' メイ: ' + user_data_list[0]['first_name_katakana'])
                    st.write('生年月日・性別')

                    st.write('メールアドレス: ' + user_data_list[0]['email'])
                    st.write('電話番号: ' + user_data_list[0]['phone_number'])

                    st.write('最終学歴')
                    st.write('大学名: ' + user_data_list[0]['university'])
                    st.write('学部名: ' + user_data_list[0]['faculty'])
                    st.write('学科名: ' + user_data_list[0]['department'])


    # 体験のフィードバック
    if experience != "未選択":
        # print("1false1")
        quit_experience = st.checkbox("体験を途中でやめる", key="35")
        # 体験のフィードバックを得る
        if quit_experience:
            st.title('業界・会社体験を評価しよう')
            st.write('以下の質問に答え，個人最適化の精度を高めよう．')

            i = 0
            option = generate_question.app(additional_question_list[i], i + 300, 1)
            st.session_state['additional_user_questionnaire_results'][i] = additional_question_list[i].index(option)

            if st.session_state['additional_user_questionnaire_results'][0] == 4 or st.session_state['additional_user_questionnaire_results'][0] == 5:
                i = 3
                option = generate_question.app(additional_question_list[i], i + 300, 1)
                st.session_state['additional_user_questionnaire_results'][i] = additional_question_list[i].index(option)
                st.session_state['radar_list'].append(option)
            else:
                i = 1
                option = generate_question.app(additional_question_list[i], i + 300, 1)
                st.session_state['additional_user_questionnaire_results'][i] = additional_question_list[i].index(option)
            if st.session_state['additional_user_questionnaire_results'][1] == 4 or st.session_state['additional_user_questionnaire_results'][1] == 5:
                i = 2
                option = generate_question.app(additional_question_list[i], i + 300, 1)
                st.session_state['additional_user_questionnaire_results'][i] = additional_question_list[i].index(option)
                st.session_state['radar_list'].append(option)

            st.session_state['submit_results'] = st.checkbox("上記内容で自己分析を提出する", key="36")


    if st.session_state['submit_results']:
        # streamlitでは，毎回，最初からプログラムが再実行されます．プログラムの下から上に影響を与えることは困難と考えたため，session_stateを使用し，以下のようにしています．
        message = "本当に提出してよろしいですか"
        if st.session_state['display_times'] == 0:
            st.session_state['display_times'] = 1
            display = False
        else:
            st.session_state['display_times'] = 0
            display = True

        change_to_false = st.checkbox(message, key="37", disabled=display)
        if change_to_false:
            st.session_state['submit_results'] = False

if __name__ == '__main__':
    main()
