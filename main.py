# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c76gtePo4fkTpqaZWVjhlidzya062H1l
"""

# main.py
from imports import *
from preprocessing import *
from I2m import *
from operations import *
from visualization import *
from unet_train import *

def main():
    # Uncomment the following line if you want to train the U-Net model
    # train_unet()

    # Load the trained U-Net model
    model_path = 'model path'
    my_new_model_with_resnet50 = load_model(model_path)

    # Define your directories
    GT_DIR = 'path of test masks'
    IMG_DIR = 'path of test images'

    # Assuming you have a test dataset (modify this based on your project)
    gt_test_paths = get_image_paths(GT_DIR )
    im_test_paths = get_image_paths(IMG_DIR)
    test_ds = tf.data.Dataset.zip((
        tf.data.Dataset.from_tensor_slices([load_and_preprocess_image(i) for i in im_test_paths]),
        tf.data.Dataset.from_tensor_slices([load_and_preprocess_mask(i) for i in gt_test_paths])
    ))
    test_ds = test_ds.cache().batch(1)

    # Visualize predictions on test data
    visualize_predictions(my_new_model_with_resnet50, test_ds, max_show=5)

    # Save predicted masks
    save_masks(test_ds)

if __name__ == "__main__":
    main()