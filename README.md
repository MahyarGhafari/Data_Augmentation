# Data Augmentation

This project contains two scripts for image augmentation using the Albumentations library and okankop/vidaug. This is meant to be used with the following GitHub Repository: https://github.com/hjl20/issp3900-handwash-annotation 

## Files

### [flip_and_mirror_augmentation.py](flip_and_mirror_augmentation.py)

This script currently loads an image and its corresponding YOLO bounding box annotations, applies a sequence of augmentation techniques to the image and updates the bounding box annotations accordingly, and saves the augmented image and updated annotations to a new directory.

## Usage

To use this script, you need to have Python installed on your machine along with the `cv2` and `albumentations` libraries.

1. Replace the `label_file` and `image_file` variables with the paths to your YOLO bounding box annotations and image respectively.
2. Uncomment or add the augmentations you want to apply inside the `A.Compose([])` function.
3. Run the script. It will load the image and its annotations, apply the augmentations, update the annotations, and save the augmented image and updated annotations to the specified directory.

## Augmentations

Refer to this website for additional augmentations: https://albumentations.ai/docs/api_reference/augmentations/
The script available augmentations from the `albumentations` library. Note that some augmentations, like flips, crops, or resizes, may require changes to any bounding boxes associated with the image.

### [testaug.py](testaug.py)

This script loads a batch of images from a specified directory, applies a sequence of augmentation techniques to each image, and saves the augmented images to a new directory.

## Usage

To use this script, you need to have Python installed on your machine along with the `cv2`, `vidaug`, and `skimage` libraries.

1. Replace the `image_folder` variable with the path to your images.
2. Replace the `augmented_dir` variable with the path where you want to save the augmented images.
3. Uncomment or add the augmentations you want to apply inside the `va.Sequential([])` function.
4. Run the script. It will load each image, apply the augmentations, and save the augmented images to the specified directory.

## Augmentations

Refer to this website for augmentation implementation:https://github.com/okankop/vidaug 
The script includes a list of all available augmentations from the `vidaug` library. Note that some augmentations, like flips, crops, or resizes, may require changes to any bounding boxes associated with the image.

