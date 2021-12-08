import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": 'video_1', "views": 200, "likes": 50},
        {"name": 'video_2', "views": 300, "likes": 80},
        {"name": 'video_3', "views": 400, "likes": 90}]

for i in range(len(data)):
    response = requests.put(BASE + "/video/" + str(i), data[i])
    print(response.json())

# it'll wait for user to press enter
input()

response = requests.get(BASE + "/video/2")
print(response.json())

input()

response = requests.patch(BASE + "/video/2", {"views":900})
print(response.json())

input()

response = requests.delete(BASE + "/video/2")
print(response.json())

input()
response = requests.get(BASE + "/video/2")
print(response.json())

