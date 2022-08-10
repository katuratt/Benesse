import streamlit as st

def main():
    st.title('自己分析をしよう!')
    st.write('自分の当てはまる項目を選んでください．途中で簡単に抜けることもできます')
    a1 = st.radio("どちらの方が嬉しいか？", ("褒められるとき", "尊敬されたとき", "頼りにされたとき"), key="1") #第一引数：リスト名（選択肢群の上に表示）、第二引数：選択肢
    a1 = st.radio("どちらの方が悲しいか？", ("貶されたとき", "怒られたとき", "一人になったとき"), key="5", index=2, horizontal=True) #第一引数：リスト名（選択肢群の上に表示）、第二引数：選択肢

    print(a1)
    # print(a2)


    # アンケートの結果を格納する
    option = []

    option1 = (st.selectbox('どちらの方が嬉しいか？',("未設定", "尊敬されたとき", "頼りにされたとき"), key="2"))
    st.write('You selected:', option1)
    option.append(option1)

    option2 = st.selectbox('どちらの方が嬉しいか？',("未設定", "貶されたとき","尊敬されたとき", "頼りにされたとき"), key="3", index=1)
    st.write('You selected:', option2)
    option.append(option2)


    print("aaaaaaaaaa")
    # print(option2)
    print(option)





if __name__ == '__main__':
    main()