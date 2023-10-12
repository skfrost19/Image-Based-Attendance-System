import cv2
import os, sys
from src.logger import logging
from src.exception import CustomException
from matplotlib import pyplot as plt

# Function to get all the images name(all possible extensions) (complete name) in the current folder.
def get_images_name(folder_path: str) -> list:
    """
    Get all the images name(all possible extensions) (complete name) in the current folder.
    :param folder_path: Path to folder
    :return: List of image names
    """
    logging.info("Entered Image Name Extraction Phase")

    try:
        images_name = []
        for file in os.listdir(folder_path):
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
                images_name.append(os.path.join(folder_path, file))
    except Exception as e:
        logging.error(f"Error Occured in Image Name Extraction")
        raise CustomException(e, sys)

    logging.info("Image Name Extraction Successful")
    return images_name



# RGB to Gray
def rgb_to_gray(image_paths: list) -> None:
    """
    Converts RGB images to grayscale
    :param image_paths: List of image paths
    :return: None
    """
    for image_path in image_paths:
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(image_path, gray)


def plot_faces(folder_path: str) -> None:
    """
    Plots all the faces in the folder
    :param folder_path: Path to folder
    :return: None
    """
    # Plot all images in a single figure (only row wise)
    images_name = get_images_name(folder_path)
    fig = plt.figure(figsize=(20, 20))
    columns = len(images_name)
    rows = 1
    for i in range(1, columns * rows + 1):
        img = cv2.imread(images_name[i - 1])
        fig.add_subplot(rows, columns, i)
        plt.imshow(img)
    plt.show()