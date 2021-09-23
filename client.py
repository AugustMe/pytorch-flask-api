import requests
import os

# image = open(r"E:\pycharm_project\Data-proessing\model_flask\timg.jpg", 'rb').read()
# payload = {'file': image}
#
# r = requests.post("http://localhost:5000/predict", files=payload).json()
# print(r)

for i in os.listdir("testimg/"):
    image = open("testimg/"+i,'rb')
    payload = {'file':image}
    r = requests.post("http://localhost:5000/predict", files=payload).json()
    print(r)
