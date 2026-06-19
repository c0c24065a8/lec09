import streamlit as st

# タイトル
st.title("社会情報プロジェクト実習I")

# 見出し
st.subheader("データ分析関連")
# CSVファイルの読み込み
import pandas as pd
df = pd.read_csv("data/iris.csv",encoding="utf-8")
# データフレームを表示（ブラウザでスクロール可能）
st.subheader("データフレーム（ブラウザでスクロール可能）") # 見出し 
st.dataframe(df)
# データフレームをテーブルで表示（ブラウザでスクロール不可）
st.subheader("テーブル（スクロール不可）") # 見出し 
st.table(df)
# Streamlitを使ってグラフ表示（散布図）
st.subheader("散布図") # 見出し 
st.scatter_chart(df, x="petal_length", y="petal_width")

# matplotlibを使ってグラフ表示(1個)
import matplotlib.pyplot as plt 
import matplotlib_fontja

st.subheader("matplotlibを使ってグラフ表示(1)") # 見出し

fig, ax = plt.subplots() # figureオブジェクトとaxesオブジェクトの作成
ax.scatter(df["petal_length"], df["petal_width"])
ax.set_title("散布図", fontsize=20)
ax.set_xlabel("petal_length", fontsize=15)
ax.set_ylabel("petal_width", fontsize=15)
st.pyplot(fig) # figureオブジェクトをStreamlitに表示
