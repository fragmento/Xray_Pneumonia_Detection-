=============
### Mod 4 project
=============

by: Mendel Oster, Andres Chaves

This project was used as Mod 4 project for Flatiron School Data Science program. 

================================================================================

    ├── Data                 <- The original, immutable data dump.
    |
    ├── Notebooks            <- Jupyter notebooks.
    |
    ├── Reports              <- Generated analysis as HTML, PDF, Slides, etc.
    |
    ├── README.md            <- The top-level README for developers using this project.
    |
    └── src                  <- Source code for use in this project.
        |
        └── example.py


===============================================================================

## About
When it comes to diagnosing Pneumonia, chest X-rays are generally the way to go. They are quick, easy, and accessible almost anywhere. In this project we will be using a convolutional neural network to classify chest X-ray images into two classes, healthy and infected patients. 

The dataset we used is from https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia <br>
- 5216 training images, 3875 instances of pneumonia and 1341 instances of healthy lungs
- 624 testing images, 390 instances of pneumonia and 234 instances of healthy lungs
- 16 validation images, 8 of each class

__________
## Visuals

To the left we can see lungs with Pneumonia, notice the opacity and lesser apparent edges versus the healthy lungs on the right<br>
<img src='Reports/Sick_lungs.png' align="left"/> 
<img src='Reports/Healthy_lungs.png' align="right"/> 

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

## Models

>For scoring the models the main metric we used is 'Recall' - for this project that means out of all sick patients how many were we able to predict correctly.

For the first model we trained a CNN over a subset of training images (250 for each class)  
This ended with a recall score of 57.95%. Since 62.5% of the testing set is patients with pneumonia the base model of always predicting pneumonia is better. 

For the second model we used Alexnet CNN architecture. At first when trained on the subset, it predicted every test image as healthy. <br> But when training it over the entire training set, it proved to be very valuable with a recall of 99%! (Precision of 74%)


Transfer learning 
We used 7 layers from the pre-trained Xeception model, with the first five layers frozen (not updating  weights).


conclusion

