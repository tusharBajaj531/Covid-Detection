from keras.models import load_model
import numpy as np
from keras.preprocessing import image

model = load_model("static/model.h5")
model.load_weights("static/best2.h5")


def pred_img(image_path):
    testimg = image.load_img(image_path,target_size=(224,224))
    testimg = image.img_to_array(testimg)
    testimg=testimg/255.0
    testimg = np.array([testimg])
    pred = np.round(model.predict(testimg))
    if pred == 0:
        return "positive"
    return "negative"