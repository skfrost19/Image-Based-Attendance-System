from retinaface import RetinaFace
import datetime
import cv2
import os, sys
from src.logger import logging
from src.exception import CustomException
from src.utils import rgb_to_gray


# Todays date
today = datetime.date.today().strftime("%d-%m-%Y")



# Function to extract faces and save them to a folder
def extract_faces(image_path: str) -> None:

    """
    Extracts faces from an image and saves them to a folder
    :param image_path: Path to image
    :return: String indicating success or failure
    """
    logging.info("Entered Face Extraction Phase")

    try:
        os.makedirs(today, exist_ok=True)
        # extract faces
        faces = RetinaFace.extract_faces(img_path=image_path, align=True)
        for i, face in enumerate(faces):
            # Save face to folder
            cv2.imwrite(f"{today}/face_{i+1}.jpg", face)
    except Exception as e:
        logging.error(f"Error Occured in Face Extraction")
        # remove the folder if it exists
        if os.path.exists(today):
            os.rmdir(today)
        raise CustomException(e, sys)

    logging.info("Face Extraction Successful")