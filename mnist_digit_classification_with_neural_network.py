# -*- coding: utf-8 -*-
"""MNIST Digit Classification with Neural Network.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yMOhb2c9TmXcmibufrO0sNIwvG8kJVVC

MNIST hand written digit classification using Deep Learning (Neural Network)

Importing the neccessary libraries and or dependencies.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
import tensorflow as tf
from google.colab.patches import cv2_imshow ## google collab does not allow
                                      #imshow in cv2, you will have to use this
from PIL import Image
from tensorflow import keras
from tensorflow.math import confusion_matrix
from keras.datasets import mnist

tf.random.set_seed(3)

"""***Loading the MNIST data from keras available dataset***"""

(x_train, y_train),(x_test, y_test) = mnist.load_data() # this data is available
                                          # on the keras website for public use.

type(x_train)
type(y_train)

# checking the shape  of the dataset

print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)

print(x_train[5].shape) # checking the size of the 5th images from the dataset.
print(x_train[5]) # Displaying the 5th images from the tarining data

"""###### Training data = 60000
###### Testing data = 10000 images
###### Image dimension = 28 X 28
###### Grayscale Image with only on channel.
###### All images have the same size and dimensions

"""

## Displaying the 5th image

plt.imshow(x_train[5])
plt.show()

## Printing the corresponding test data

print(y_train[5])

# checking the size and unique values in the labels

print(y_train.shape, y_test.shape)

# unique

print(np.unique(y_train))
print(np.unique(y_test))

"""**Data Normalization**"""

## Scalling the data by 255 to have scaled values between 0 and 1 for ease of
#  the Neaural Network.

x_train = x_train / 255
x_test = x_test / 255

print(x_train.shape)
print(x_test.shape)

"""**Building the Neural Network**"""

# Setting up the Model

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(40, activation="relu"),
    keras.layers.Dense(40, activation="relu"),
    keras.layers.Dense(10,  activation="sigmoid")
])

# Complie the Neural Network

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy" , metrics=["accuracy"] )

# Training the scaled data with the built and compiled model

model.fit(x_train, y_train, epochs=5)

"""**Model Evalation**"""

loss, accuracy = model.evaluate(x_test , y_test)

print(x_test.shape)

# Display 1st data in x test


print("the corresponding label in the test data is:",y_test[0])
plt.imshow(x_test[0])
plt.show()

prediction = model.predict(x_test)

print(prediction.shape)
print(prediction[0])

arg_max = np.argmax(prediction[0]) # getting the maximum probabilty of the prediction

print(arg_max)

## Lopping through the predicted label probalities for all the test data

pred_labels = [np.argmax(i) for i in prediction]

print(pred_labels)

"""**Confusion Metrics**"""

## Seeing how well the model is predicting the labels of the test data.

con_matrix = confusion_matrix (y_test, pred_labels)

print(con_matrix)

## Plotting the confusion matrix

plt.figure(1,figsize=(15, 7))
sns.heatmap(con_matrix,annot=True, fmt='d', cmap="Blues")
plt.ylabel("Actual Labels")
plt.xlabel("Predicted Labels")

"""**Building a Predictive system**"""

new_img_path = "/content/MNIST_digit.png"

new_img = cv2.imread(new_img_path)

## displayimg the new image

cv2_imshow(new_img)

print(type(new_img))
print(new_img.shape)

# from the above, it is obvious that the testing image has a different dimension
# with that which the model is trained on. therefor it neeed to be reshaped and
# resized and converted to a gray scale image


## converting to GrayScale

gray_scale = cv2.cvtColor(new_img, cv2.COLOR_RGB2GRAY)

# checking if successfully converted

print(gray_scale.shape)

cv2_imshow(gray_scale)

## Resizing the image

gray_scale_resz = cv2.resize(gray_scale, (28,28))
cv2_imshow(gray_scale_resz )
print(gray_scale_resz.shape)

## Normalizing the image by 255

image_norm = gray_scale_resz / 255

## Reshaping the image data to fit into 1 instance

image = np.reshape(image_norm,[1,28,28])

## Loading the new image into the model for prediction


new_pred = model.predict(image)

print(new_pred)

pred = np.argmax(new_pred)

##
print(pred)

"""**Predictive System**"""

new_img_path = input("kindly put the path of the image to be predicted:")

new_img = cv2.imread(new_img_path)
## displayimg the new image
cv2_imshow(new_img)

gray_scale_resz = cv2.resize(gray_scale, (28,28))

cv2_imshow(gray_scale_resz )
print(gray_scale_resz.shape)

## converting to GrayScale
gray_scale = cv2.cvtColor(new_img, cv2.COLOR_RGB2GRAY)

# checking if successfully converted
print(gray_scale.shape)


## Resizing the image
gray_scale_resz = cv2.resize(gray_scale, (28,28))
print(gray_scale_resz.shape)

## Normalizing the image by 255
image_norm = gray_scale_resz / 255

## Reshaping the image data to fit into 1 instance
image = np.reshape(image_norm,[1,28,28])

## Loading the new image into the model for prediction
new_pred = model.predict(image)
print(new_pred)

pred = np.argmax(new_pred)

##
print("The Handwritten Digit is recognised as",pred)