from django.shortcuts import render
from django.http import HttpResponse, response
from keras.models import model_from_json
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import json

from numpy.core.numeric import False_

# Create your views here.


def det_pneumonia(request):
    # test_data_var = request.FILES
    predict = get_class_activation_map('../diagnomatic_api/pneumonia/uploads/3.jpg')
    response_data = {}
    response_data['Normal'] = False
    response_data['Pneumonia'] = False
    
    if (predict[0] >= 0.6):
        response_data['Normal'] = True
    else:
        response_data['Pneumonia'] = True
    # print(test_data_var)
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def get_class_activation_map(path) :
    # load json and create model
    img_size = 150
    json_file = open('../diagnomatic_api/pneumonia/model/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights("../diagnomatic_api/pneumonia/model/model.h5")
    model.compile(optimizer = "rmsprop" , loss = 'binary_crossentropy' , metrics = ['accuracy'])
    print("Loaded model from disk")
    img_arr = cv2.imread(os.path.join(path), cv2.IMREAD_GRAYSCALE)
    resized_arr = cv2.resize(img_arr, (img_size, img_size))
    img = resized_arr.reshape(-1, img_size, img_size, 1)
    predict = model.predict(img)
    return predict
