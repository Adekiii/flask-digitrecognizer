# flask-digitrecognizer
A digit recognizer web app in Flask, using the sklearn MNIST dataset. 

This is a simple web application that allows the user to draw a digit on a canvas, which will then be predicted by a machine learning model.
The model uses random forest classification to predict the user's drawn digits.


Below is an example:

![Sample](https://github.com/Adekiii/flask-digitrecognizer/blob/master/sample.png)

Currently, for best results, the user is required to draw the digit in the middle of the canvas in full size. This is due to the fact that the drawing is passed to the model as the whole canvas, and not segmented to just the drawn part.
