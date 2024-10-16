import joblib
import numpy as np
from django.shortcuts import render

poly_model, poly_transformer = joblib.load(r'C:\Users\Dell User\Desktop\Social-Media-adds\Social_app\myapp\poly_model.pkl')  # Adjust the path if needed

def predict_view(request):
    if request.method == 'POST':
        gender = 1 if request.POST.get('gender') == 'male' else 0
        age = int(request.POST.get('age'))
        estimated_salary = float(request.POST.get('estimated_salary'))
        click = 1 if request.POST.get('click') == 'yes' else 0

        input_data = np.array([[gender, age, estimated_salary, click]])

        # Transform the input data using the polynomial transformer
        input_data_poly = poly_transformer.transform(input_data)

        # Make predictions using the loaded model
        prediction = poly_model.predict(input_data_poly)

        # Optionally clip the prediction if necessary
        prediction = np.clip(prediction, 0, 1)

        return render(request, 'form.html', {'prediction': prediction[0]})

    return render(request, 'form.html')
