# Aerial-image-Semi-supervision
The i2m model is trained (unet_train.py) on preprocessed labelled images (image-mask pairs).
The trained i2m is fed with the unlabelled images to give the soft-masks for the unlabelled images.
The m2i model (gan.py) is a combination of generator (unet_gen.py) and discriminator (discriminator(4).py).
The m2i is trained (main_script.py) on the pre-processed labelled images (image-mask pairs).
The trained m2i is fed with the soft-masks to reconstruct the unlabelled images.
The reconstructed images and original unlabelled images are compared using a reconstruction score (ssim_calculator.py) and those with a score higher than a threshold are selected as 'most-confident' image-mask pair.
The labelled images and the 'most-confident' image-mask pairs are utilised to train the i2m model.
