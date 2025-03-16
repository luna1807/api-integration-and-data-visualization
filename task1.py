import requests
import matplotlib.pyplot as plt
import pandas
import sqlalchemy
from PIL import Image
from io import BytesIO  

#api url
api_key="sr4bgaz6Nb8tbwtdU9qx6frbwkaVFeNoGq3yBjfK"
url=f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
#To fetch data
headers = {"Accept": "application/json"}
response = requests.get(url, headers=headers)
data = response.json()

#To print resonse date
print("Date:", data["date"])
print("Title:", data["title"])
print("Explantion:", data["explanation"])
print("Image:", data["url"])

# TO check if the photo is a image
if data["media_type"] == "image":
    img_url = data["url"]
#fetching and displaying th img
    img_response = requests.get(img_url)
    img = Image.open(BytesIO(img_response.content))
#Matplotlib
    plt.figure(figsize=(8, 6))
    plt.imshow(img)
    plt.axis("off")
    plt.title(data["title"])
    plt.show()

else:
    print("media is not an image. It may be a video")
