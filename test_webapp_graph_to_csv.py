import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CSVデータ直線描画アプリ")
st.write("Excelの「散布図（直線・点なし）」を再現します。")

# 1. ファイルアップローダー
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])

if uploaded_file is not None:
    # 2. CSV読み込み（文字コード自動判別）
    try:
        df = pd.read_csv(uploaded_file, encoding='utf-8')
    except:
        df = pd.read_csv(uploaded_file, encoding='shift-jis')
    
    # プレビュー表示
    with st.expander("データの中身を確認する"):
        st.write(df)

    # 3. 列の選択
    columns = df.columns.tolist()
    col1, col2 = st.columns(2)
    with col1:
        x_col = st.selectbox("X軸（横軸）を選択", columns)
    with col2:
        y_col = st.selectbox("Y軸（縦軸）を選択", columns)

    # 並べ替えオプション
    if st.checkbox("X軸の値でデータを並べ替える"):
        df = df.sort_values(x_col)

    # 4. Matplotlibで描画
    # 日本語対応を外しているため、タイトル等に日本語を使うと文字化けします
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # 直線のみで描画
    ax.plot(df[x_col], df[y_col], linestyle='-', color='blue', linewidth=1.5)
    
    ax.set_title(f"Plot: {x_col} vs {y_col}") # 念のため英語表記を推奨
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.grid(True, linestyle='--', alpha=0.6)

    # Streamlitで表示
    st.pyplot(fig)

else:
    st.info("CSVファイルをアップロードしてください。")