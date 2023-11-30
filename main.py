""" # TEST all the functions here

from src.components.pipeline import pipeline

if __name__ == "__main__":
    pipeline() """

from src.components.pipeline import pipeline
from src.components.generate import extract_faces
from src.utils import plot_faces

if __name__ == "__main__":
    pipeline()
