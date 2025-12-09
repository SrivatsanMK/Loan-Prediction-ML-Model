# 💼 Loan Eligibility Prediction System (Machine Learning + Flask Web App)

A professional **Loan Prediction Web Application** that uses a Machine Learning model (Decision Tree Classifier) to determine whether a loan application should be **Approved** or **Rejected** based on financial and employment-related inputs.

This system includes:

- A trained ML model (`Loan_Model.pkl`)
- A corporate-grade web interface (HTML + CSS)
- Flask backend integration for prediction
- A separate **Result Page** with dynamic color feedback

---

# 🚀 Features

- 🧠 **Machine Learning-based Loan Classification**
- 🌐 **Flask-powered Web Application**
- 🎨 **Professional and clean UI (FinTech style)**
- ⌨️ **ENTER key automatically moves to next field**
- 🧹 **No number input arrows (spinner removed)**
-  ⚡ Real-time prediction with instant result page redirect
- 📊 Uses 5 key applicant features
- 🔥 Perfect for portfolios, ML projects, and academic submissions

---

# 📘 Model Report (Detailed)

### **🔍 Objective**
To automate loan approval decisions using a trained ML model based on structured applicant data.

### **📊 Dataset Overview**
The dataset contains applicant details such as:

| Feature | Description |
|--------|-------------|
| income | Applicant annual income |
| credit_score | Applicant credit score value |
| loan_amount | Requested loan amount |
| years_employed | Total years of employment |
| points | Internal scoring mechanism |

Target Variable:
- `loan_approved` → 1 (Approved), 0 (Rejected)

### **🧠 Model Used**
`DecisionTreeClassifier` from Scikit-learn  
Reason for choosing:
- Handles tabular data well  
- Easy to interpret  
- Fast training and prediction  
- Performs well with categorical/numerical mix  

### **📈 Workflow**

### 🏗️ System Architecture

```
User Input → Flask Backend → ML Model (.pkl) → Prediction Output
```

---

### 📂 Project Structure

```
Loan_Prediction_App/
│
├── app.py # Flask backend
├── Loan_Model.pkl # Trained ML model
├── Model.ipynb # Notebook used for model training
│
├── templates/
│ ├── index.html # Input page with modern UI
│ └── result.html # Clean result display page
│
└── static/
└── style.css # Additional CSS
```

---

### 🖥️ How to Run the Project

Follow the steps below to run this project on your local machine.

---

#### **1️⃣ Clone the Repository**
```
git clone https://github.com/SrivatsanMK/Loan-Prediction-ML-Model.git
```

```
cd Loan-Prediction-ML-Model/Loan_Prediction_App
```

---

#### **2️⃣ Install Required Dependencies**
Make sure Python is installed.  
Then run:

```
pip install flask numpy scikit-learn
```

---

#### **3️⃣ Run the Flask Application**
```
python app.py
```

---

#### **4️⃣ Open the Application in Your Browser**
Once the server starts, open:

```
http://127.0.0.1:5000/
```

Your Loan Prediction web app will now be running locally.

---

#### **5️⃣ Enter the Required Input Fields**
- Income  
- Credit Score  
- Loan Amount  
- Years Employed  
- Points  

Click **Check Eligibility** to get the prediction.

---

### 📊 Output Preview

The system returns:

- ✔ **Loan Approved** (Green)  
- ❌ **Loan Rejected** (Red)
---

### 🔮 Future Enhancements

- Add login/authentication system  
- Add admin dashboard with charts  
- Deploy online (Render / Railway / AWS)  
- Improve model accuracy using RandomForest / XGBoost  
- Add user database to store application history  
- Add REST API endpoint for mobile integration  

---

### 🛠️ Technologies Used

- Python  
- Flask  
- NumPy  
- Scikit-learn  
- HTML5  
- CSS3  

---

### 📄 License

This project is open-source and available under the **MIT License**.

