import streamlit as st
from apps import test_app, test2_app

def main():
    # Streamlit が対応している任意のオブジェクトを可視化する (ここでは文字列)
    st.write('Hello, World!')
    st.title("hello")

    check = st.checkbox("チェックボックス", key="1") #引数に入れることでboolを返す
    st.button("ボタン", key="2") #引数に入れるとboolで返す
    # st.selectbox("メニューリスト", ("選択肢1", "選択肢2", "選択肢3")) #第一引数：リスト名、第二引数：選択肢
    # st.multiselect("メニューリスト（複数選択可）", ("選択肢1", "選択肢2", "選択肢3")) #第一引数：リスト名、第二引数：選択肢、複数選択可
    # st.radio("ラジオボタン", ("選択肢1", "選択肢2", "選択肢3")) #第一引数：リスト名（選択肢群の上に表示）、第二引数：選択肢
    # st.text_input("文字入力欄") #引数に入力内容を渡せる


    test_app.app()
    test2_app.app()

if __name__ == '__main__':
    main()