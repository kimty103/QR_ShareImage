import requests

import json

API_KEY = "generated api key"


def image_request(img_file:bytes, expiration:int=300):
    url = f"https://api.imgbb.com/1/upload?key={API_KEY}"

    payload = {'expiration': expiration}
    files=[
    ('image',('0.png',img_file,'image/png'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    #print(response.text)
    #convert to json
    data = json.loads(response.text)
    
    return data['data']['url']

if __name__ == "__main__":
    print(image_request(open('dasf.png','rb')))