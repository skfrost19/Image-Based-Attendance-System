from deepface import DeepFace
import time
from src.logger import logging
from src.exception import CustomException
import sys

def verify_face(face_1: str, face_2: str) -> bool:
    """
    Verifies if two faces are the same person
    :param face_1: Path to first face
    :param face_2: Path to second face
    :return: True if the faces are the same person, False otherwise
    """
    try:
        logging.info("Verifying faces")
        result = DeepFace.verify(face_1, face_2, distance_metric='euclidean_l2', enforce_detection=False, model_name="Facenet512")
        return result["verified"]
        
    except Exception as e:
        logging.error(f"Error in verify_face: {e}")
        raise CustomException(e, sys)
    

def verify_faces_concurrently(test_faces: list, db_faces: list) -> dict:
    """
    Verifies if the faces in test_faces are the same person as the faces in db_faces
    :param test_faces: List of paths to faces to be tested
    :param db_faces: List of paths to faces in the database
    :return: Dictionary of verified faces
    """
    try:
        logging.info("Verifying faces concurrently")
        # keys will be name of db_faces (excluding the path and extension)
        verified_faces = {}.fromkeys([face.split("\\")[-1].split(".")[0] for face in db_faces], False)

        start = time.time()
        # implementing without threading
        for face in test_faces:
            for db_face in db_faces:
                verified_faces[db_face.split("\\")[-1].split(".")[0]] = verify_face(face, db_face)
        end = time.time()

        logging.info(f"Time taken: {end-start}")
        return verified_faces
        
    except Exception as e:
        logging.error(f"Error in verify_faces_concurrently: {e}")
        raise CustomException(e, sys)