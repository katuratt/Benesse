import streamlit as st
import csv
import numpy as np

from apps import generate_question

def main():
    #csvファイルから，質問のデータを読み込みquestion_listに格納
    path_questions = "data/questions.csv"
    with open(path_questions, 'r', encoding='utf_8') as csv_file:
        csv_reader = csv.reader(csv_file)
        questions = list(csv_reader)
    question_list = []
    for question in questions:
        question_ = []
        for j in question:
            if len(j) > 0:
                question_.append(j)
        question_list.append(question_)

    # アンケートの結果を格納する場所を準備
    if 'user_questionnaire_results' not in st.session_state:
        user_questionnaire_results_ = np.zeros(len(question_list), dtype=int)
        user_questionnaire_results = []
        for i in user_questionnaire_results_:
            user_questionnaire_results.append(i.item())
        st.session_state['user_questionnaire_results'] = user_questionnaire_results

    st.title('自己分析をしよう!')
    st.write('自分の当てはまる項目を選んでください．途中で抜けることも簡単にできます．')

    # 希望条件・経験・パーソナリティ・スキルに関する質問をメインに行う
    for i in range(len(question_list)):
        option = generate_question.app(question_list[i], i, st.session_state['user_questionnaire_results'][i])
        st.session_state['user_questionnaire_results'][i] = question_list[i].index(option)

if __name__ == '__main__':
    main()