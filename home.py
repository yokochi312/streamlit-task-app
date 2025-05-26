import streamlit as st
import json
import os

st.set_page_config(page_title="ホーム", layout="centered")
st.title("🏠 ホーム画面")

DATA_FILE = "task_data.json"

# データ読み込み
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
else:
    data = {
        "subscription": [],
        "todo": [],
        "due_today": [],
        "job_hunting": []
    }

def count_undone(task_list):
    return sum(1 for t in task_list if not t.get("done", False))

st.header("📝 現在のタスク状況")

st.write(f"📦 サブスクリプション：{count_undone(data['subscription'])} 件の未完了")
st.write(f"✅ ToDoリスト：{count_undone(data['todo'])} 件の未完了")
st.write(f"⏰ 今日までにやること：{count_undone(data['due_today'])} 件の未完了")
st.write(f"💼 就活タスク：{count_undone(data['job_hunting'])} 件の未完了")

st.markdown("---")
st.page_link("pages/taskmanager.py", label="➡️ タスク管理ページへ", icon="🛠️")