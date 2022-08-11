import streamlit as st
import plotly.express as px
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import csv
from datetime import date

from apps import generate_question

def main():
    #csvファイルから，追加の質問のデータを読み込み
    path_additional_questions = "data/additional_questions.csv"
    with open(path_additional_questions, 'r', encoding='utf_8') as csv_file:
        csv_reader = csv.reader(csv_file)
        additional_question_list = list(csv_reader)

    #  アンケート結果を格納する
    if 'additional_user_questionnaire_results' not in st.session_state:
        additional_user_questionnaire_results_ =  np.zeros(len(additional_question_list), dtype=int)
        additional_user_questionnaire_results = []
        for i in additional_user_questionnaire_results_:
            additional_user_questionnaire_results.append(i.item())
        st.session_state['additional_user_questionnaire_results'] = additional_user_questionnaire_results
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

        elif experience == "業界の実際の様子をVRを通じて体験する":
            st.write('業界の実際の様子をVRを通じて体験しよう！')
            st.write('業界を選択してください．あなたに個人最適化された評価軸順に業界は並んでいます')
            #TODO: 業界を個人最適化して並べ替える
            personalized_industry_list = industry_list

            industry = st.selectbox('業種選択',("未選択",personalized_industry_list[0], personalized_industry_list[1],personalized_industry_list[2], personalized_industry_list[3],personalized_industry_list[4], personalized_industry_list[5]), key="32", index=0)
            if industry != "未選択":
                message = "ゲームを通じて" + industry + "業界の体験をしよう"
                st.write(message)
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
                #csvよりデータを取得
                path_user_data = "data/user_data.csv"
                with open(path_user_data, newline='', encoding='utf_8') as f:
                    reader = csv.DictReader(f)
                    user_data_list = [row for row in reader]
                # print(user_data_list)

                # インターンシップの応募
                internship_name = company_name + "  User-Based Digital Competition"
                st.title(internship_name)
                st.text_input(label='漢字氏名', value=user_data_list[0]['last_name'] + user_data_list[0]['first_name'])
                st.text_input(label='カナ指名', value=user_data_list[0]['last_name_katakana'] + user_data_list[0]['first_name_katakana'])
                st.date_input('生年月日',min_value=date(1900, 1, 1),max_value=date.today(),value=date(int(user_data_list[0]['birth_year']), int(user_data_list[0]['birth_month']), int(user_data_list[0]['birth_day']),))
                st.radio("性別", ("男", "女", "その他"), index=int(user_data_list[0]['gender']), key= 34, horizontal=True)
                st.text_input(label='メールアドレス', value=user_data_list[0]['email'])
                st.text_input(label='電話番号', value=user_data_list[0]['phone_number'])
                st.text_input(label='郵便番号', value=user_data_list[0]['postal_code'])
                st.text_input(label='住所', value=user_data_list[0]['address'])
                st.text_input(label='最終学歴', value=user_data_list[0]['university'] + user_data_list[0]['faculty'] + user_data_list[0]['department'])

                option_internship = st.button("応募する", key = 36)
                if option_internship:
                    st.session_state['submit_results'] = True
                    st.session_state['additional_user_questionnaire_results'].append(company_name)

    # 体験のフィードバック
    if experience != "未選択" and experience != "企業の実際の様子をインターンシップを通じて体験する":
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
