from flask import Flask, render_template, request
from skimage import io as skio
from skimage.transform import resize
from io import BytesIO
import base64
import joblib 
import numpy as np


app = Flask(__name__)
model = joblib.load('digits_model')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    json_data = request.get_json()['image']
    img_data = base64.b64decode(json_data[22:])

    img_matrix = skio.imread(BytesIO(img_data))[:,:,3]

    matrix_resized = resize(img_matrix, (8, 8), anti_aliasing=False)
    matrix_resized = np.array(matrix_resized * 50)

    predicted_number = model.predict(matrix_resized.reshape(1, -1))[0]

    return str(predicted_number)


if __name__ == '__main__':
    app.run()