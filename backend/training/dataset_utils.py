# backend/training/dataset_utils.py
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def create_generators(dataset_dir, img_size=(224,224), batch_size=32, val_split=0.2):
    # dataset_dir contains subfolders f0..f4
    datagen_train = ImageDataGenerator(
        rescale=1./255,
        rotation_range=15,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.05,
        zoom_range=0.1,
        horizontal_flip=True,
        validation_split=val_split
    )

    train_gen = datagen_train.flow_from_directory(
        dataset_dir,
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='training',
        shuffle=True
    )

    val_gen = datagen_train.flow_from_directory(
        dataset_dir,
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation',
        shuffle=False
    )

    # classes mapping, e.g. {'f0':0, 'f1':1,...}
    class_indices = train_gen.class_indices
    inv_class_map = {v:k for k,v in class_indices.items()}

    return train_gen, val_gen, inv_class_map
