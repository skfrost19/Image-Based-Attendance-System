import os


def clean_faces(folder_path: str) -> None:
    """
    This function will remove all the faces from the folder
    """
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        os.remove(file_path)
    os.rmdir(folder_path)
    return None


def clean_images(folder_path: str) -> None:
    """
    This function will remove all the images from the folder
    """
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        os.remove(file_path)
    return None


def clean_logs(folder_path: str) -> None:
    """
    This function will remove all the logs from the folder
    """
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        os.remove(file_path)
    return None
