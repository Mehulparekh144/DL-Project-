from django.core.files.storage import FileSystemStorage
from django.shortcuts import  render
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import pickle
import joblib
import openpyxl
import datetime



import cv2
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model

# Create your views here.
def form(request):
    return render(request, 'form.html')

def predict_img(img):
    model = load_model('C:\\Users\\mehul\\Desktop\\DLProject\\model.h5')

    test_img = load_img(img, target_size=(50, 50))
    test_img_arr = np.array(test_img)
    test_img_arr = test_img_arr.reshape(-1,50,50,3)
    plt.imshow(test_img)
    predictions = np.argmax(model.predict(test_img_arr),axis=-1)
    print(predictions)


    
    if(predictions == 1):
        return f'Breast IDC Cancer is present  | Prediction = {predictions}'
    
    else:
        return f'Breast IDC Cancer not present | Prediction = {predictions}'

    
    



def result(request):
    if request.method == 'POST' and request.FILES['myimage']:
        upload = request.FILES['myimage']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        file_url = file_url[1:]

        result = predict_img(file_url)
        

    return render(request, 'result.html', {'myresult': result , 'myimage' : file_url})





