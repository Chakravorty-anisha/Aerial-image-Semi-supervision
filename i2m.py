# -*- coding: utf-8 -*-
"""I2m.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18zdLZT1fqyVfoBKIYJliIKXeFL4RcSAT
"""

# model_definition.py
from tensorflow.keras import Input, Model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, UpSampling2D, concatenate
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.optimizers import Adam

def dice_coefficient(y_true, y_pred):
    y_true = tf.cast(y_true, tf.float32)
    intersection = K.sum(y_true * y_pred, axis=[1, 2, 3])
    union = K.sum(y_true, axis=[1, 2, 3]) + K.sum(y_pred, axis=[1, 2, 3])
    return K.mean((2. * intersection + 1.) / (union + 1.))

def dice_loss(y_true, y_pred):
    return 1 - dice_coefficient(y_true, y_pred)

def combined_loss(y_true, y_pred):
    cat_cross_loss = categorical_crossentropy(y_true, y_pred)
    dice_loss_value = dice_loss(y_true, y_pred)
    alpha = 0.5
    beta = 0.5
    combined = alpha * cat_cross_loss + beta * dice_loss_value
    return combined

def new_model_with_resnet50_encoder():
    resnet50_encoder = ResNet50(weights='imagenet', include_top=False, input_shape=(IMG_SIZE1, IMG_SIZE2, 3))
    for layer in resnet50_encoder.layers:
        layer.trainable = False

    resnet50_output = resnet50_encoder.output

    x6 = UpSampling2D(size=(2, 2))(resnet50_output)
    x6 = concatenate([resnet50_encoder.get_layer("conv4_block6_out").output, x6])
    x6 = Conv2D(1024, 3, activation="relu", padding="same")(x6)
    x6 = Conv2D(512, 3, activation="relu", padding="same")(x6)

    x7 = UpSampling2D(size=(2, 2))(x6)
    x7 = concatenate([resnet50_encoder.get_layer("conv3_block4_out").output, x7])
    x7 = Conv2D(512, 3, activation="relu", padding="same")(x7)
    x7 = Conv2D(128, 3, activation="relu", padding="same")(x7)

    x8 = UpSampling2D(size=(2, 2))(x7)
    x8 = concatenate([resnet50_encoder.get_layer("conv2_block3_out").output, x8])
    x8 = Conv2D(256, 3, activation="relu", padding="same")(x8)
    x8 = Conv2D(128, 3, activation="relu", padding="same")(x8)

    x9 = UpSampling2D(size=(2, 2))(x8)
    x9 = concatenate([resnet50_encoder.get_layer("conv1_relu").output, x9])
    x9 = Conv2D(128, 3, activation="relu", padding="same")(x9)
    x9 = Conv2D(64, 3, activation="relu", padding="same")(x9)
    x9 = Conv2D(32, 3, activation="relu", padding="same")(x9)

    x9 = UpSampling2D(size=(2, 2))(x9)
    x9 = Conv2D(128, 3, activation="relu", padding="same")(x9)
    x9 = Conv2D(64, 3, activation="relu", padding="same")(x9)
    x9 = Conv2D(17, 3, activation="softmax", padding="same")(x9)

    model = Model(inputs=resnet50_encoder.input, outputs=x9)
    opt = Adam(learning_rate=0.0001)
    model.compile(optimizer=opt, loss=combined_loss, metrics=[MeanIoU(num_classes=17)])
    return model