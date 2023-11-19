import requests
import requests
import datetime

today = datetime.date.today().strftime("%d-%m-%Y")

def upload_image(image_path, upload_url):
    with open(image_path, 'rb') as file:
        files = {'image': file}
        response = requests.post(upload_url, files=files)
        if response.status_code == 200:
            print("Image uploaded successfully.")
        else:
            print("Failed to upload image.")


def get_image(url, save_path):
        response = requests.get(url)
        if response.status_code == 200:
                with open(save_path, 'wb') as file:
                        file.write(response.content)
                        print("Image downloaded successfully.")
        else:
                print("Failed to download image.")
# Example usage
image_path = '../test/test1.jpg'
save_path = '../images/f{today}.png'

upload_url = 'https://example.com/upload'
upload_image(image_path, upload_url)
image_url = 'https://example.com/image.jpg'
get_image(image_url, save_path)