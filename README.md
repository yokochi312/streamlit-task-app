# 🛠️ Streamlit Task Manager App

This is a custom task management web app built with Python and Streamlit.  
It allows you to manage tasks across multiple categories with enhanced UI features.

---

## 🚀 Features

- 📥 Add tasks with deadlines
- ✅ Mark tasks as complete
- 🗑️ Delete tasks individually
- 🔍 Search and filter tasks by keywords
- 🎨 Color-coded deadlines (past = red, today = orange, done = gray)
- 📦 Manage subscriptions with price and renewal dates
- 💾 Data persistence using JSON file
- 🖼️ Responsive, card-style layout using custom CSS

---

## 📂 File Structure
streamlit-task-app/
├── home.py                  # Main summary page
├── pages/
│   └── taskmanager.py       # Core task management logic
├── task_data.json           # Saved data (auto-created)
└── .streamlit/
└── config.toml          # Optional: custom theme config
---

## 💻 Getting Started

1. Clone this repository:
```bash
git clone https://github.com/your-username/streamlit-task-app.git
cd streamlit-task-app
---

## 💻 Getting Started

1. Clone this repository:
```bash
git clone https://github.com/your-username/streamlit-task-app.git
cd streamlit-task-app
2.	Create a virtual environment and install Streamlit:
conda create -n task_env python=3.10
conda activate task_env
pip install streamlit
3.	Run the app:
streamlit run home.py
✨ Screenshots

Add screenshots here if you like (optional)

⸻

📌 Future Plans
	•	Calendar-based UI
	•	Notification for approaching deadlines
	•	Tagging or categorizing tasks
	•	Save to SQLite or cloud

⸻

🧑‍💻 Author

Built by @yokochi312
For contact: Instagram @rui____49

⸻

📄 License

This project is licensed under the MIT License.
