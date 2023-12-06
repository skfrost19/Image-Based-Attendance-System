import os
import sys
from datetime import datetime
from src.logger import logging
from src.exception import CustomException
from src.components.generate import extract_faces
from src.components.verify import verify_faces_concurrently, verify_faces_sequentially
from src.utils import get_images_name
from src.components.attendance import mark_attendance


def pipeline(image_path: str) -> None:
    """
    Pipeline to perform face recognition
    :return: None
    """
    try:
        logging.info("Starting pipeline")
        # check if image exists
        if not os.path.exists(image_path):
            logging.error("Image does not exist")
            raise CustomException("Image does not exist", sys)
        logging.info(f"Image path: {image_path}")

        # Extract faces from the images
        extract_faces(image_path)

        # Get the date
        date = datetime.now().strftime("%d-%m-%Y")
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
