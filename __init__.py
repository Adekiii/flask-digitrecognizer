from flask import Flask, render_template, request
from skimage import io as skio
from skimage.transform import resize
from io import BytesIO
import base64
import joblib 
import numpy as np
import tensorflow as tf 
import matplotlib.pyplot as plt 


app = Flask(__name__)
model = tf.keras.models.load_model('Git/flask-digitrecognizer/digits.model')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    json_data = request.get_json()['image']
    img_data = base64.b64decode(json_data[22:])

    img = skio.imread(BytesIO(img_data))[:,:,3]

    img = resize(img, (28, 28), anti_aliasing=False)

    predicted_number = model.predict(img.reshape(1, -1))
    predicted_number = np.argmax(predicted_number)

    return str(predicted_number)


if __name__ == '__main__':
    app.run()