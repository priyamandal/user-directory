# Simple Web-Based User Directory with Search Filter

This is a beginner-friendly Python + Flask web app that fetches random user data from an API and displays it in an HTML table. The user list can be filtered by name or email.

---

## 💻 Tech Stack
- Python 3
- Flask
- Jinja2 (HTML templating)
- Bootstrap (for styling)
- RandomUser API

---

## 📁 Folder Structure
```
user-directory/
├── app.py                   # Flask server
├── templates/
│   └── index.html           # Jinja2 HTML template
└── requirements.txt         # (optional) Python dependencies
```

---

## 🔧 Setup Instructions

### 1. Clone or Download the Project
You can download the folder or clone it from GitHub (if hosted).

### 2. Install Python Packages
Open your terminal and run:

```bash
pip install flask requests
```

Alternatively, use `requirements.txt` if available:
```bash
pip install -r requirements.txt
```

### 3. Run the Flask Server
```bash
python app.py
```

You will see:
```
Running on http://127.0.0.1:5000/
```

### 4. Open Your Browser
Go to: `http://localhost:5000`

---

## 🧠 How It Works

- `app.py` fetches user data from [randomuser.me](https://randomuser.me/api/?results=10)
- Passes the data to `templates/index.html`
- HTML uses `{% for user in users %}` to loop and render rows
- A simple input field + JavaScript lets you filter results in real-time

---

## ✅ Features

- View 18 random users
- Display full name, email, and country
- Real-time search filter
- Mobile-responsive using Bootstrap

---

## 📸 Screenshot

(You can add a screenshot of the table here)

---

## 🙋‍♀️ Author
Priya Mandal Saha
