import joblib
import numpy as np

model = joblib.load("C:\Users\saumy\ML lab 25, 26 deploy\app.py")
model = joblib.load("student_pass_model.pkl")
st.title("Student Pass/Fail Prediction System")
study_hours = st.number_input("Study Hours per Week", min_value=0.0, max_value=40.0, value=10.0)
attendance = st.number_input("Attendance Percentage", min_value=0.0, max_value=100.0, value=75.0)

if prediction[0] == 1:
st.success("Prediction: PASS")
else:
        st.error("Prediction: FAIL")


        st.error("Prediction: FAIL")
