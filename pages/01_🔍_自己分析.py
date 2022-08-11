import streamlit as st

def main():
    st.title('自己分析をしよう!')
    st.write('自分の当てはまる項目を選んでください．途中で簡単に抜けることもできます')

    #TODO: 質問を増やす

    # アンケートの結果を格納する
    if 'option_list' not in st.session_state:
        st.session_state['option_list'] = [0,0,0,0]

    # i問目の質問
    i = 0
    option0_list = ["未選択", "尊敬されたとき", "頼りにされたとき"]
    option0 = (st.selectbox('どれが嬉しいか？',(option0_list[0], option0_list[1], option0_list[2]), key=i, index=st.session_state['option_list'][i]))
    st.write('You selected:', option0)
    st.session_state['option_list'][i] = option0_list.index(option0)
    print(option0)

    i = 1
    option_list = ["未選択", "尊敬されたとき", "頼りにされたとき"]
    option = (st.selectbox('どれが嬉しいか？',(option_list[0], option_list[1], option_list[2]), key=i, index=st.session_state['option_list'][i]))
    st.session_state['option_list'][i] = option_list.index(option)

    i = 2
    option_list = ["未選択", "尊敬されたとき", "頼りにされたとき"]
    option = (st.selectbox('どれが嬉しいか？',(option_list[0], option_list[1], option_list[2]), key=i, index=st.session_state['option_list'][i]))
    st.session_state['option_list'][i] = option_list.index(option)




if __name__ == '__main__':
    main()