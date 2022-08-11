import streamlit as st

# app画面の表示を担当する
def app():
    if 'personally_identifiable_information_licensing' not in st.session_state:
        st.session_state['personally_identifiable_information_licensing'] = 0
    # 以下をサイドバーに表示
    personally_identifiable_information_licensing = st.sidebar.radio("あなたの就職情報を将来の就活生に使用しても良いですか？", ("使用しない", "使用して良い"),index=st.session_state['personally_identifiable_information_licensing'])
    if personally_identifiable_information_licensing == "使用しない":
        st.session_state['personally_identifiable_information_licensing'] = 0
    elif personally_identifiable_information_licensing == "使用して良い":
        st.session_state['personally_identifiable_information_licensing'] = 1
    st.sidebar.write("個人情報は匿名化され，特定は不可能なように扱われます．")

    st.title("就活での「本質的な評価軸」を個人最適化する就活支援サービスです．")
    st.write('個人最適化された自己分析手法をもとに，あなたをカテゴライズし，あなたに近い就活生がどの企業を対象に就活していたかをお伝えします．')
    st.write('個人最適化された自己分析，過去の事例からの情報，VRやゲーム，インターンシップの体験を通じて，企業への理解だけでなく，あなた自身を理解することをお手伝いします．')
    st.write('このサービスを続け，自分を深く知り，「本質的な評価軸」を得て，就活を成功させましょう！')

if __name__ == '__main__':
    app()