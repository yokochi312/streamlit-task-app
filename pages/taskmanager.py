import streamlit as st
import json
import os
from datetime import date, datetime

st.set_page_config(page_title="タスク管理", layout="centered")
st.title("🛠️ タスク管理ページ")

DATA_FILE = "task_data.json"

# 初期化
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({
            "subscription": [],
            "todo": [],
            "due_today": [],
            "job_hunting": []
        }, f)

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

data = load_data()

# タスク操作

def add_task(category, task_text, deadline):
    if task_text:
        data[category].append({
            "task": task_text,
            "deadline": deadline.strftime("%Y-%m-%d"),
            "done": False
        })
        save_data(data)
        st.rerun()

def delete_task(category, index):
    del data[category][index]
    save_data(data)
    st.rerun()

def complete_task(category, index):
    data[category][index]["done"] = True
    save_data(data)
    st.rerun()

# 表示UI（期限付き＋絞り込み）
def task_ui_with_deadline(category, title):
    st.subheader(title)

    task_input = st.text_input(f"{title}に追加", key=f"{category}_input")
    deadline_input = st.date_input("締切日を選択", key=f"{category}_deadline", value=date.today())

    if st.button("追加", key=f"{category}_add"):
        add_task(category, task_input, deadline_input)

    # 🔍 絞り込み検索
    search_keyword = st.text_input("🔎 絞り込み（キーワード検索）", key=f"{category}_search")

    delete_index = None
    complete_index = None

    for i, item in enumerate(data[category]):
        task_text = item["task"]
        if search_keyword.lower() not in task_text.lower():
            continue

        done = item["done"]
        deadline_str = item.get("deadline", "")
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date() if deadline_str else None

        col1, col2, col3 = st.columns([6, 1, 1])
        with col1:
            st.markdown(f"- {'✅' if done else '🔲'} {task_text}（期限: {deadline}）")
        with col2:
            if not done and st.button("完了", key=f"{category}_done_{i}"):
                complete_index = i
        with col3:
            if st.button("削除", key=f"{category}_del_{i}"):
                delete_index = i

    if delete_index is not None:
        delete_task(category, delete_index)
    elif complete_index is not None:
        complete_task(category, complete_index)

    st.markdown("---")

# サブスクリプションUI（料金・更新日付き）
def subscription_ui():
    st.subheader("📦 サブスクリプションリスト")

    service = st.text_input("サービス名", key="sub_service")
    price = st.number_input("月額料金（円）", min_value=0, step=100, key="sub_price")
    renewal_date = st.date_input("次回更新日", key="sub_renewal", value=date.today())

    if st.button("追加", key="sub_add"):
        data["subscription"].append({
            "service": service,
            "price": int(price),
            "renewal_date": renewal_date.strftime("%Y-%m-%d")
        })
        save_data(data)
        st.rerun()

    # 表示
    st.markdown("### 📋 登録済みのサブスクリプション")
    delete_index = None

    for i, sub in enumerate(data["subscription"]):
        col1, col2, col3, col4 = st.columns([4, 2, 3, 1])
        with col1:
            st.write(f"📺 {sub['service']}")
        with col2:
            st.write(f"💰 ¥{sub['price']}")
        with col3:
            st.write(f"🗓 {sub['renewal_date']}")
        with col4:
            if st.button("削除", key=f"sub_del_{i}"):
                delete_index = i

    if delete_index is not None:
        del data["subscription"][delete_index]
        save_data(data)
        st.rerun()

    st.markdown("---")

# 📅 カレンダー風UI
def calendar_view_ui():
    st.subheader("📅 カレンダー風タスク一覧")

    combined = []
    for category in ["todo", "job_hunting"]:
        for item in data[category]:
            if "deadline" in item and not item["done"]:
                deadline = datetime.strptime(item["deadline"], "%Y-%m-%d").date()
                combined.append({
                    "task": item["task"],
                    "category": category,
                    "deadline": deadline
                })

    combined.sort(key=lambda x: x["deadline"])

    for item in combined:
        st.markdown(f"📆 `{item['deadline']}`｜{item['task']}（{item['category']}）")

# 🔁 表示処理
subscription_ui()
task_ui_with_deadline("todo", "✅ ToDoリスト")
calendar_view_ui()
task_ui_with_deadline("job_hunting", "💼 就活タスク")

st.page_link("home.py", label="⬅️ ホームに戻る", icon="🏠")