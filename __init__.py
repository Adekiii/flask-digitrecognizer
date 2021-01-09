from flask import Flask, render_template, request
from skimage import io as skio
from skimage.transform import resize
from io import BytesIO
import base64
import joblib 
import numpy as np
import tensorflow as tf 
from boundingbox import bounding_box


app = Flask(__name__)
model = tf.keras.models.load_model('Git/flask-digitrecognizer/olddigits.model')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    json_data = request.get_json()['image']
    img_data = base64.b64decode(json_data[22:])

    img = skio.imread(BytesIO(img_data))[:,:,3]

    img = bounding_box(img)
    img = resize(img, (28, 28), anti_aliasing=True)

    prediction = model.predict(img.reshape(1, -1))

    confidence = round(np.max(prediction) * 100, 1)
    predicted_number = np.argmax(prediction)
    

    return str(predicted_number) + " - Confidence: " + str(confidence) + "%"


if __name__ == '__main__':
    app.run()