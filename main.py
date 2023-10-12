# TEST all the functions here

from src.components.verify import verify_face, verify_faces_concurrently
import time
from src.utils import get_images_name, plot_faces
import os, sys
from src.components.generate import extract_faces

if __name__ == "__main__":
    test_image = get_images_name("test")
    extract_faces(test_image[0])
    plot_faces("03-10-2023")