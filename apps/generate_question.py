import streamlit as st
import pandas as pd
import numpy as np

# 質問を作成する
#質問と選択肢が入ったリストをもらい，選択肢を作成し，解答を返す
def app(question, key, index = 1):
    # question[0]は質問のため，inndexの位置がずれる．それを修正する必要がある
    index -= 1
    if index < 0:
        index = 0
    i = len(question)
    for j in question:
        if j == "":
            i -= 1
    if i == 0:
        print("質問に誤りあり")
        return 0
    elif i == 1:
        return st.checkbox(question[0], key=key)
    elif i == 2:
        print("質問に誤りあり")
        return 0
    elif i == 3:
        return st.selectbox(question[0],(question[1], question[2]), key = key, index = index)
    elif i == 4:
        return st.selectbox(question[0],(question[1], question[2], question[3]), key = key, index = index)
    elif i == 5:
        return st.selectbox(question[0],(question[1], question[2], question[3], question[4]), key = key, index = index)
    elif i == 6:
        return st.selectbox(question[0],(question[1], question[2], question[3], question[4], question[5]), key = key, index = index)
    elif i == 7:
        return st.selectbox(question[0],(question[1], question[2], question[3], question[4], question[5], question[6]), key = key, index = index)
    elif i == 8:
        return st.selectbox(question[0],(question[1], question[2], question[3], question[4], question[5], question[6], question[7]), key = key, index = index)
    elif i == 9:
        return st.selectbox(question[0],(question[1], question[2], question[3], question[4], question[5], question[6], question[7], question[8]), key = key, index = index)
    elif i == 10:
        return st.selectbox(question[0],(question[1], question[2], question[3], question[4], question[5], question[6], question[7], question[8], question[9]), key = key, index = index)
    elif i == 11:
        return st.selectbox(question[0],(question[1], question[2], question[3], question[4], question[5], question[6], question[7], question[8], question[9], question[10]), key = key, index = index)
    elif i == 12:
        return st.selectbox(question[0],(question[1], question[2], question[3], question[4], question[5], question[6], question[7], question[8], question[9], question[10], question[11]), key = key, index = index)
    elif i == 13:
        return st.selectbox(question[0],(question[1], question[2], question[3], question[4], question[5], question[6], question[7], question[8], question[9], question[10], question[11], question[12]), key = key, index = index)
    elif i == 14:
        return st.selectbox(question[0],(question[1], question[2], question[3], question[4], question[5], question[6], question[7], question[8], question[9], question[10], question[11], question[12], question[13]), key = key, index = index)
    elif i == 15:
        return st.selectbox(question[0],(question[1], question[2], question[3], question[4], question[5], question[6], question[7], question[8], question[9], question[10], question[11], question[12], question[13], question[14]), key = key, index = index)
    else:
        print("質問に誤りあり")
        return 0



if __name__ == '__main__':
    app()