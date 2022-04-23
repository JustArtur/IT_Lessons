import requests
import os
from PIL import Image
import io

def save_users():
    users = get_users_from_url(2)
    for user in users:
        fp = f"users_data/{user['id']}"
        os.mkdir(fp)
        f = open(f"users_data/{user['id']}/user_info.txt", "w")
        f.write(user['first_name'] + '\n')
        f.write(user['last_name'] + '\n')
        f.write(user['email'] + '\n')
        save_avatar_from_url(user["avatar"], fp)

def get_users_from_url(pages):
    users = []
    for i in range(1, pages+1):
        users = users + requests.get(f"https://reqres.in/api/users?page={i}").json()["data"]
    return users

def save_avatar_from_url(image_url, fp):
    r = requests.get(image_url)
    with Image.open(io.BytesIO(r.content)) as image:
        image.save(fp+"/avatar.jpeg")

save_users()






