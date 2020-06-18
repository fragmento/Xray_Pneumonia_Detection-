#!/usr/bin/env python
# coding: utf-8

# In[1]:


def getImageSizes(folder_path):
    '''
    Takes in a specified folder path and returns a list of sizes for each file in the folder
    '''
    file_size = []

    for dirpath, dirnames, filenames in os.walk(folder_path):
        for file in filenames:
            if file == '.DS_Store':
                continue
                
            f = os.path.join(dirpath, file)
            
            im = Image.open(f)
            width, height = im.size
            
            file_size.append((width, height))
    return file_size
 


# In[2]:


def convertImages(tr_dir,val_dir,test_dir, size=(256,256)):
    '''
    returns scaled numpy arrays of images and their labels
    like so (train_images, train_labels), (val_images, val_labels), (test_images, test_labels)
    '''
    
    val_generator = ImageDataGenerator(rescale=1./255).flow_from_directory(
            val_dir, batch_size=16, target_size=size)

    train_generator = ImageDataGenerator(rescale=1./255).flow_from_directory(
            tr_dir,batch_size=5216, target_size=size)

    test_generator = ImageDataGenerator(rescale=1./255).flow_from_directory(
            test_dir, batch_size=624, target_size=size)

    train_images, train_labels = next(train_generator)
    val_images, val_labels = next(val_generator)
    test_images, test_labels = next(test_generator)
    
    
    return train_images, train_labels, val_images, val_labels, test_images, test_labels


# In[3]:


import itertools
    
import matplotlib.pyplot as plt
import numpy as np

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    import itertools
    
    import matplotlib.pyplot as plt
    import numpy as np 
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()


# In[4]:


def predict_X_ray(full_image_path):
    '''
    This function takes in the path to a chest x-ray image and returns a 
    classification of 0 or 1, healthy or pneumonia respectively
    '''
    import cv2
    image = cv2.imread(full_image_path)
    
    pred = cnn2.predict(image[np.newaxis,:,:,0,np.newaxis],batch_size=1)
    
    if pred == 1:
        return 'Pneumonia'
    if pred ==0:
        return 'Healthy'


# In[ ]:




