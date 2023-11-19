from deepface import DeepFace
from src.logger import logging
from src.exception import CustomException
import sys
import multiprocessing
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
    


def verify_face_pair(face_pair):
    """
    Verifies if the two faces in the face_pair are the same person
    :param face_pair: Tuple of paths to a test face and a database face
    :return: Boolean indicating whether the two faces match
    """
    test_face, db_face = face_pair
    return verify_face(test_face, db_face)

def verify_faces_concurrently(test_faces: list, db_faces: list) -> dict:
    """
    Verifies if the faces in test_faces are the same person as the faces in db_faces
    :param test_faces: List of paths to faces to be tested
    :param db_faces: List of paths to faces in the database
    :return: Dictionary of verified faces
    """
    try:
        logging.info("Verifying faces concurrently")
        
        # Use multiprocessing to verify faces concurrently
        with multiprocessing.Pool() as pool:
            face_pairs = [(test_face, db_face) for test_face in test_faces for db_face in db_faces]
            results = pool.map(verify_face_pair, face_pairs)

        # Combine test_faces, db_faces, and results into a dictionary
        verified_faces = {f"{test_face}-{db_face}": result for ((test_face, db_face), result) in zip(face_pairs, results)}
        
        return verified_faces
    
    except Exception as e:
        logging.error(f"Error in verify_faces_concurrently: {e}")
        raise CustomException(e, sys)
        