import streamlit as st

st.title("📋 はじめてのStreamlitアプリ")
st.write("👋 こんにちは！これはタスク管理のはじまりです。")

task = st.text_input("📝 タスクを入力")
if st.button("追加"):
    st.success(f"追加されました: {task}")