# TODO
# 1.- Will take image
# 2 - Extract faces
# 3 - Save faces to folder
# 4 - Get the faces
# 5 - Get the database faces
# 6 - Verify the faces
# 7 - Get the roll numbers of the verified faces
# 8 - Mark attendance

import os
import sys
from datetime import datetime
from src.logger import logging
from src.exception import CustomException
from src.components.generate import extract_faces
from src.components.verify import verify_faces_concurrently, verify_faces_sequentially
from src.utils import get_images_name
from src.components.attendance import mark_attendance


def pipeline()->None:
    """
    Pipeline to perform face recognition
    :return: None
    """
    try:
        logging.info("Starting pipeline")

        # Get the images
        date = datetime.now().strftime("%d-%m-%Y")
        # get image name (todays date.extension) 
        image_path = os.path.join(os.getcwd(), "images", f"{date}.png")   
        # check if image exists
        if not os.path.exists(image_path):
            logging.error("Image does not exist")
            raise CustomException("Image does not exist", sys)
        logging.info(f"Image path: {image_path}")
    
        # Extract faces from the images
        extract_faces(image_path)


        # Get the faces
        faces = get_images_name(os.path.join(os.getcwd(), date))

        # Get the database faces
        db_faces = get_images_name(os.path.join(os.getcwd(), "records/MRH"))

        # Verify the faces
        verified_faces = verify_faces_sequentially(faces, db_faces)

        # Mark attendance
        mark_attendance(list(verified_faces.keys()))

        logging.info("Pipeline completed successfully")

    except Exception as e:
        logging.error(f"Error in pipeline: {e}")
        raise CustomException(e, sys)