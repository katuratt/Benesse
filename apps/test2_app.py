import streamlit as st

def app():
    # Streamlit が対応している任意のオブジェクトを可視化する (ここでは文字列)
    st.write('Hello, World!')
    st.title("hello")

    check = st.checkbox("チェックボックス") #引数に入れることでboolを返す

    if check:
        h = st.button("ボタン") #引数に入れるとboolで返す
        g = st.selectbox("メニューリスト", ("選択肢1", "選択肢2", "選択肢3")) #第一引数：リスト名、第二引数：選択肢
        f = st.multiselect("メニューリスト（複数選択可）", ("選択肢1", "選択肢2", "選択肢3")) #第一引数：リスト名、第二引数：選択肢、複数選択可
        e = st.radio("ラジオボタン", ("選択肢1", "選択肢2", "選択肢3")) #第一引数：リスト名（選択肢群の上に表示）、第二引数：選択肢

    # 以下をサイドバーに表示
    a = st.sidebar.text_input("文字入力欄") #引数に入力内容を渡せる
    d = st.sidebar.text_area("テキストエリア")

    # LaTeX テキスト
    st.latex(r'\bar{X} = \frac{1}{N} \sum_{n=1}^{N} x_i')

if __name__ == '__main__':
    app()