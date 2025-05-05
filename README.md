# Diabetes Prediction Model with SVM  

## Description  
This project is a machine learning model that predicts the likelihood of diabetes using the Support Vector Machine (SVM) algorithm. It uses a dataset containing medical features such as glucose levels, blood pressure, BMI, and other health metrics. The model is trained to classify individuals as diabetic or non-diabetic based on these features.  

## Installation  
1. **Prerequisites**:  
   - Python 3.6 or higher.  
   - Required libraries: `numpy`, `pandas`, `scikit-learn`, `streamlit` (for the web app).  

2. **Install dependencies**:  
   ```bash  
   pip install numpy pandas scikit-learn streamlit  
   ```  

3. **Download the dataset**:  
   - Ensure the dataset `diabetes.csv` is in the project directory.  

## Usage  
### Training the Model  
Run the Jupyter notebook or Python script to train the model:  
```python  
python diabetes_prediction.py  
```  

### Making Predictions via Command Line  
Use the trained model to make predictions:  
```python  
# Example input format: [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]  
input_data = [5, 166, 72, 19, 175, 25.8, 0.587, 50]  
prediction = loaded_model.predict([input_data])  
print("Diabetic" if prediction[0] == 1 else "Not Diabetic")  
```  

### Web Application  
1. Run the Streamlit app:  
   ```bash  
   streamlit run app.py  
   ```  
2. Input the required health metrics in the web interface and click "Test your data" to get a prediction.  

## Contributing  
1. Fork the repository.  
2. Create a new branch for your feature:  
   ```bash  
   git checkout -b feature/your-feature-name  
   ```  
3. Commit your changes and push to the branch.  
4. Submit a pull request with a description of your changes.  

## License  
This project is licensed under the MIT License.  

---  
*Note: Replace `diabetes.csv` with your dataset. The model is for educational purposes and not intended for medical diagnosis.*
