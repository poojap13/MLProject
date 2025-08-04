
  # 🎯 Student Exam Performance Predictor

  ## 🚀 Live Demo
  🔗 **[Click here to try the app](https://mlproject-exoa.onrender.com)**

  A **Machine Learning Web Application** that predicts a student's **Math score** based on demographic and academic details.  
  This project uses **Flask** for the backend, **scikit-learn** for the machine learning pipeline, and is deployed on **Render** for public access.

  ---

  ## 📌 Features
  - 📊 **Machine Learning Model** – Trained with scikit-learn using a clean preprocessing pipeline.
  - 🖥 **Interactive Web App** – Easy-to-use form for entering student details.
  - 📈 **Regression Prediction** – Outputs predicted Math score instantly.
  - 🌐 **Online Deployment** – Hosted publicly on Render.
  - 🎨 **Clean UI** – Minimal, responsive, and user-friendly design.

  ---

  ## 🛠 Tech Stack
  **Backend:** Python, Flask  
  **Machine Learning:** scikit-learn, Pandas, NumPy, CatBoost, XGBoost  
  **Frontend:** HTML5, CSS3  
  **Deployment:** Render  
  **Other Tools:** Matplotlib, Seaborn for data visualization & analysis  

  ---

  ## 📂 Project Structure
```

MLProject/
│
├── src/                     # Data processing and ML pipeline
├── templates/               # HTML templates (home.html, etc.)
├── artifacts/               # Saved model and preprocessor files
├── application.py           # Flask app entry point
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── ...

````

---

## 📷 Screenshot
![App Screenshot](screenshot.png)

*(Replace `screenshot.png` with an actual screenshot of your deployed app — form visible with a sample prediction.)*

---

## ⚡ How It Works
1. **Data Input** – User fills out the form with student info (gender, race/ethnicity, parental education, lunch type, test prep status, reading & writing scores).
2. **Preprocessing** – Input data is transformed using the saved preprocessing pipeline.
3. **Model Prediction** – Trained regression model outputs predicted Math score.
4. **Result Display** – The predicted score is shown on the same page in a styled result box.

---

## 🖥 Running Locally

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/MLProject.git
cd MLProject
````

### **2️⃣ Create and Activate a Virtual Environment**

```bash
# Create venv
python -m venv venv

# Activate venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Application**

```bash
python application.py
```

### **5️⃣ Open in Browser**

Visit:

```
http://127.0.0.1:5000
```

---

## 📊 Model Details

* **Algorithm Used:** Linear Regression
* **Training Library:** scikit-learn
* **Metrics Evaluated:** R² Score, MAE, RMSE
* **Dataset:** Student Performance dataset (custom processed)
* **Target Variable:** Math Score

---

## 📬 Contact

If you have any questions or feedback, feel free to reach out:

* **Name:** Pooja Pathare
* **GitHub:** [poojap13](https://github.com/poojap13)
* **Live Demo:** [mlproject-exoa.onrender.com](https://mlproject-exoa.onrender.com)

+
