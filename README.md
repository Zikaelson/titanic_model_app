
# Titanic Survival Prediction Web App

> A full-stack machine learning app that predicts whether a Titanic passenger survived, built using **Python**, **Flask**, **scikit-learn**, and **Bootstrap**.

## 🧠 Project Overview

This is a simple web application that:
- Trains a logistic regression model using the Titanic dataset
- Accepts user input (class, sex, age)
- Predicts whether the passenger would have survived
- Displays the result on a modern, styled web page

## 🗂️ Project Structure

```
titanic_model_app/
│
├── app.py                 # Main web application using Flask
├── train_model.py         # Trains and saves the ML model
├── requirements.txt       # All required Python libraries
├── README.md              # This file (full project guide)
│
├── model/
│   ├── __init__.py        # Marks 'model' as a Python package
│   ├── preprocess.py      # Function to clean & format user input
│   └── model.pkl          # Saved logistic regression model (auto-generated)
│
└── templates/
    └── index.html         # Web page (user interface)
```

## ⚙️ Setup Instructions (Step-by-Step)

> These steps assume you're using **VS Code** and a Windows or Unix terminal.

### 🧱 1. Clone or Create the Project Folder

Create and open a folder called:

```
titanic_model_app
```

Inside it, create:
- 2 folders: `model` and `templates`
- 4 files: `app.py`, `train_model.py`, `requirements.txt`, `README.md`

Inside `model/`, create:
- `preprocess.py`
- `__init__.py` (leave it empty)

Inside `templates/`, create:
- `index.html`

### 🐍 2. Set Up a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

- **Windows:**
  ```bash
  .\venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 📦 3. Install Required Libraries

```bash
pip install flask pandas seaborn scikit-learn joblib
```

Then save them:

```bash
pip freeze > requirements.txt
```

Or manually paste into `requirements.txt`:

```
flask
pandas
seaborn
scikit-learn
joblib
```

### 🤖 4. Train the Model

```bash
python train_model.py
```

If successful, you’ll see no error, and `model/model.pkl` will be created.

### 🧪 5. Test Your Input Preprocessing Script

```bash
python
>>> from model.preprocess import preprocess_input
>>> print(preprocess_input(2, 'female', 29))
>>> exit()
```

### 🌐 6. Start the Flask App

```bash
python app.py
```

Visit in browser: `http://127.0.0.1:5000`

### 🖼️ 7. Use the Web Form

Try:
- Class: `3`
- Sex: `female`
- Age: `22`

Then click **Predict**.

## 🔍 What Each File Does

| File/Folder | Purpose |
|-------------|---------|
| `train_model.py` | Trains and saves the logistic regression model |
| `model/preprocess.py` | Translates user form input into a DataFrame |
| `model/__init__.py` | Marks the model folder as a Python package |
| `model/model.pkl` | Saved trained ML model |
| `app.py` | Flask application logic |
| `templates/index.html` | Front-end web form |
| `requirements.txt` | Package list |
| `README.md` | Documentation guide |

## 🛠️ Common Troubleshooting

| Issue | Solution |
|-------|----------|
| `ImportError` on `preprocess_input` | Run from root folder and ensure `__init__.py` exists |
| Blank web page | Ensure `index.html` is inside `templates/` and not empty |
| Flask not installed | Run: `pip install flask` |
| Changes not showing | Press Ctrl+Shift+R in your browser |
| Python caching errors | Delete `__pycache__` folder |

## 🚀 Next Steps

- 🎨 Style the app using more Bootstrap or custom CSS
- 📊 Add more features to the model
- 🌍 Deploy online using platforms like Render, Replit, or Heroku

## 👏 Credits

- Titanic dataset: Seaborn
- ML framework: scikit-learn
- App styling: Bootstrap 5

---

## 📸 Demo Screenshot (Optional)

If you'd like to showcase what the app looks like:

1. Open your app in a browser: `http://127.0.0.1:5000`
2. Take a screenshot
3. Save it in your project folder as `screenshot.png`
4. Add this Markdown to display it:

```markdown
## 🖼️ Demo

![App Screenshot](screenshot.png)
