import streamlit as st

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

    st.title('自己分析をしよう!')
    st.write('自分の当てはまる項目を選んでください．途中で抜けることも簡単にできます．')

    #TODO: 質問を増やす

    # i問目の質問
    # 希望条件に関する質問
    i = 0
    option_list = ["未選択", "北海道", "東北", "関東", "中部", "近畿", "中国", "四国", "九州", "沖縄"]
    option = (st.selectbox('勤務地はどこを希望しますか？',(option_list[0], option_list[1], option_list[2], option_list[3], option_list[4], option_list[5], option_list[6], option_list[7], option_list[8], option_list[9]), key=i, index=st.session_state['user_questionnaire_results'][i]))
    st.session_state['user_questionnaire_results'][i] = option_list.index(option)

    # 経験に関する質問
    i = 1
    option_list = ["未選択", "研究", "勉学", "ゼミ活動", "アルバイト", "サークル活動", "留学"]
    option = (st.selectbox('大学生活で最も力を入れたものは，この中では何ですか？',(option_list[0], option_list[1], option_list[2], option_list[3], option_list[4], option_list[5], option_list[6]), key=i, index=st.session_state['user_questionnaire_results'][i]))
    st.session_state['user_questionnaire_results'][i] = option_list.index(option)

    # パーソナリティに関する質問
    i = 0
    option_list = ["未選択", "一人で過ごすことが多い", "どちらかというと一人で過ごすことが多い", "どちらかというと友達と過ごすことが多い", "友達と過ごすことが多い"]
    option = (st.selectbox('休日はどのように過ごすことが多いですか？',(option_list[0], option_list[1], option_list[2], option_list[3], option_list[4]), key=i, index=st.session_state['user_questionnaire_results'][i]))
    st.session_state['user_questionnaire_results'][i] = option_list.index(option)

    i = 1
    option_list = ["未選択", "待てない", "10分まで", "30分まで", "1時間まで", "1時間以上"]
    option = (st.selectbox('友達が遅刻した時，何分までなら待てますか？',(option_list[0], option_list[1], option_list[2], option_list[3], option_list[4], option_list[5]), key=i, index=st.session_state['user_questionnaire_results'][i]))
    st.session_state['user_questionnaire_results'][i] = option_list.index(option)

    i = 2
    option_list = ["未選択", "未経験", "2年以下","2年以上5年以下","5年以上8年以下","8年以上"]
    option = (st.selectbox('どの程度のプログラミング歴がありますか？',(option_list[0], option_list[1], option_list[2], option_list[3], option_list[4], option_list[5]), key=i, index=st.session_state['user_questionnaire_results'][i]))
    st.session_state['user_questionnaire_results'][i] = option_list.index(option)

    i = 3
    option_list = ["未選択", "全く話せない", "日常会話レベル","ビジネス会話程度","ネイティブレベル"]
    option = (st.selectbox('どの程度の英語力がありますか？',(option_list[0], option_list[1], option_list[2], option_list[3], option_list[4]), key=i, index=st.session_state['user_questionnaire_results'][i]))
    st.session_state['user_questionnaire_results'][i] = option_list.index(option)

    i = 4
    option_list = ["未選択", ""]
    option = (st.selectbox('？',(option_list[0], option_list[1], option_list[2]), key=i, index=st.session_state['user_questionnaire_results'][i]))
    st.session_state['user_questionnaire_results'][i] = option_list.index(option)

    i = 5
    option_list = ["未選択", "600点以下", "600点以上700点以下", "700点以上800点以下", "800点以上900点以下", "900点以上"]
    option = (st.selectbox('TOIECの点数は何点ですか？',(option_list[0], option_list[1], option_list[2], option_list[3], option_list[4], option_list[5]), key=i, index=st.session_state['user_questionnaire_results'][i]))
    st.session_state['user_questionnaire_results'][i] = option_list.index(option)



if __name__ == '__main__':
    main()