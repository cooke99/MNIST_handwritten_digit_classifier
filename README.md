# MNIST_handwritten_digit_classifier
 
This repo demonstrates the training and (brief) analysis of various classifiers on the MNIST dataset. Included in the repo are 3 files (excluding the README and images used in the README):
 
`MNIST_classifier_training_and_analysis.ipynb` - Jupyter notebook detailing the process of model selection and training etc.
 
`requirements.txt` - Text file containing the libraries used in the repo.
 
`hand_drawn_digit_clf_app.py` - A very simple python app to demonstrate the classifier in action. Detailed instructions on using it are given below.

# Model Training, Analysis and Selection:

`MNIST_classifier_training_and_analysis.ipynb` details the process of model selection and training, presenting various classifiers and evaluating their scores using cross validation sets. A number of techniques to improve the accuracy of the model are presented and evaluated. You can download and run the notebook yourself, but some of the `cross_val_*` cells take up to an hour to run so be warned. The final model can be downloaded as shown below if you would like to play around with it yourself.
 
# Final Model Download:
 
The final pickled model was greater than 3 GB, so I zipped the file (~161 MB) and uploaded it to google drive.
 
**The final model can be downloaded at this link:** https://drive.google.com/file/d/1O5GU4cfaVN_ci4dA3YNrKaSFvw4Aswzk/view?usp=sharing
 
Simply download the zip file, extract it, and place the file `mnist_knn_clf_final.pkl` in the same directory as `hand_drawn_digit_clf_app.py`

# Hand-drawn Digit Classifier Application Instructions:

Follow the instructions for the final model download above. The app does not have a .exe or fancy UI, and requires a python IDE to execute it. Once the `.pkl` model file is located in the same directory as the `.py` file (explained above) simply open the `.py` file in your chosen IDE and run it.

Click on a point on the canvas to move the cursor to that position, and drag the cursor around to draw a line on the canvas. Pressing `Enter` will print the model prediction of the drawing to the console. Pressing `Del` or `Delete` will wipe the canvas for a new drawing. The app is not very robust and is only intended to demonstrate the final model. As the images drawn on the canvas are mapped to a 1x784 array before being input to the model, **it is recommended to draw the digits as big as possible** in order to increase the accuracy of the predictions.

For example, the left image shows the digit drawn on the canvas, while the right image shows the 28x28 array seen by the model. This drawing resulted in the model predicting a 9:

![](/comparison.png)

In comparison, the image below resulted in the model predicting an 8.

![](/correct_comparison.png)

# Errors in Hand-drawn Digit Classifier Application:

If you use the hand-drawn digit classifier app, chances are you'll find it's a lot less accurate than the 97.6% accuracy reported on the test set in the Jupyter notebook. There are a number of reasons for this:

## Data mismatch

Looking at the comparison images shown just above, the 28x28 matrix of the number 8 can be seen. The noise around the digit on the right is added artifically in an attempt to make the digit more like those seen during training in the MNIST dataset. Shown below is an example of an 8 from the MNIST dataset:

![](/MNIST_8.png)

Clearly there is some discrepancy between the actual training images and the artificially generated ones. This is a significant source of error in the model's predictions.

## Mapping of small digits:

As shown above, the mapping of the drawn digits to a 28x28 matrix presents a significant challenge to the model when the digits are too small.

## Error matrix:

The error matrix (generated in the Jupyter notebook) is shown here:

![](/error_matrix.png)

The errors shown in the error matrix  are evident in the app - the model will frequently misclassify 8s, and often confuses 4s and 9s. This becomes apparent after much use of the app.
