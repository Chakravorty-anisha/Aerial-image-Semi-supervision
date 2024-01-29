# Aerial-image-Semi-supervision
The i2m model is trained (unet_train.py) on preprocessed labelled images (image-mask pairs)
The m2i model (gan.py) is a combination of generator (unet_gen.py) and discriminator (discriminator(4).py)
The m2i is trained (main_script.py) on the pre-processed labelled images (image-mask pairs)
