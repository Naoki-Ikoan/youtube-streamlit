import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("hello")

st.write("Progress bar view")
"start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)




left, right = st.columns(2) 
button = left.button("右カラムに文字を表示")

if button:
    right.write("ここは右カラム")

expander = st.expander("問い合わせ")
expander.write("問い合わせ内容を書く")

# text = st.text_input("あなたの趣味は")
# "あなたの趣味:", text


# condition = st.slider("あなたの今の調子は？",0,100,50)
# "コンディション:",  condition