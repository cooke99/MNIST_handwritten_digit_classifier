# -*- coding: utf-8 -*-
"""
User-drawn digit classifier.

This is a simple program based on the turtle module that allows the user to draw a digit and use the classifier trained on the MNIST
dataset to make a prediction on what digit was drawn. Once the turtle window appears, click on the canvas to move the pen to that location,
then drag the pen to draw a line. Pressing enter will print the classifier's prediction to the console. Pressing Del or delete will reset
the canvas.

"""

import numpy as np
import turtle as trt
import tkinter as tk
import matplotlib.pyplot as plt
import joblib
from sklearn.neighbors import KNeighborsClassifier

global img_arr

def on_drag_event(x,y):
    # Moves the turtle/pen with the mouse cursor as long as the left mouse button is held, drawing a line on the canvas
    # while simultaneously filling in the corresponding elements in the 28x28 array.
    
    global img_arr
    
    pen.ondrag(None)    # Prevent a stack overflow.
    pen.goto(x,y)
    x_idx = int(round(x))
    y_idx = int(round(y))
    
    if x_idx < 0:   # Prevents out of bounds index on array.
        x_idx = 0
        
    elif x_idx > 28:    # Prevents out of bounds index on array.
        x_idx = 28
    
    if y_idx < 0:   # Prevents out of bounds index on array.
        y_idx = 0
        
    elif y_idx > 28:    # Prevents out of bounds index on array.
        y_idx = 28
    
    img_arr[y_idx,x_idx] = 255
    img_arr[y_idx,x_idx+1] = 255    # Fills in adjacent elements in matrix, effectively making the black line thicker.
    img_arr[y_idx+1,x_idx] = 255    # Same as above.
    add_noise(x_idx,y_idx)  # Add noise to the surrounding pixels (explained in the function)
    pen.ondrag(on_drag_event)
    
    return None

def on_click_event(x,y):
    # Moves the turtle to whichever position on the canvas the user clicked on.
    
    trt.onscreenclick(None) # Prevent a stack overflow.
    pen.up()    # Prevents turtle from drawing.
    pen.goto(x,y)
    pen.down()  # Enable drawing with the turtle.
    trt.onscreenclick(on_click_event)
    
    return None

def add_noise(x,y):
    # This function adds noise to the pixels around each drawn pixel - to the left, right,
    # above and below the pixel - ONLY if those pixels are not already drawn on.
    # The purpose of this is to make the drawn digits look like those from the MNIST dataset.
    
    global img_arr
    
    for i in [1,-1]:
        if img_arr[y,x+i] != 255:
            img_arr[y,x+i] = np.random.normal(150,25)   # Noise sampled from a normal distribution with mean 150 and SD of 25.
        
    for j in [1,-1]:
        if img_arr[y+j,x] != 255:
            img_arr[y+j,x] = np.random.normal(150,25)
        
    return None
    
def reset_window():
    # Clears the window for a new drawing.
    
    global img_arr
    img_arr = np.zeros((28,28))
    pen.reset()
    pen.ondrag(on_drag_event)
    pen.pensize(2)
    pen.speed('fastest')
    plt.close('all')    # Close any matplotlib figures.
    
    return None

def predict_digit():
    # Prints model prediction of drawing.
    
    global img_arr
    print('This number is:', int(knn_digit_clf.predict(img_arr.reshape(1,784))))
    #show_digit()
    
    return None  
    
def show_digit():
    # Disabled by default. If enabled it produces a matplotlib bitmap of 
    # the 28x28 matrix before it is reshaped to a 1x784 array and input to the model.
    
    global img_arr
    plt.imshow(img_arr, cmap='binary')
    plt.axis('on')
    plt.grid()
    plt.show()
    
    return None

# Load kNN classifier for MNIST dataset:
knn_digit_clf = joblib.load('mnist_knn_clf_final.pkl')

# Set up 28x28 array of zeros to be input to the classifier:
img_arr = np.zeros((28,28))

# Intialise settings for turtle canvas:
wn = trt.Screen()
wn.screensize(28,28)
trt.setworldcoordinates(0,28,28,0)

# Initialise turtle:
pen = trt.Turtle()
pen.shape('circle')
pen.pensize(2)
pen.resizemode('user')
pen.shapesize(outline=1)
pen.speed('fastest')

# Bind functions to events:
trt.listen()    # Listen for user commands e.g. pressing a key.
pen.ondrag(on_drag_event)   # Binds on_drag_event function to the event of user clicking on the turtle and dragging it to a new location.
trt.onscreenclick(on_click_event)   # Binds on_click_event function to the event of user clicking on a part of the canvas or window.
trt.onkeypress(predict_digit,key='Return') # Binds  show_digit function to the press of 'Enter' or return key.
trt.onkeypress(reset_window,key='Delete')   # Binds  reset_window function to the press of delete key (not backspace).

wn.mainloop()

