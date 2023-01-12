import requests
import datetime
import os

date = datetime.date.today().strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
MEDITATION_GRAPH_ID = "graph1"
CODE_CONSISTENCY_ID = "graph2"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN,
}

graph1_params = {
    "id": MEDITATION_GRAPH_ID,
    "name": "Meditation Tracker",
    "unit": "commit",
    "type": "float",
    "color": "ajisai"
}

graph2_params = {
    "id": CODE_CONSISTENCY_ID,
    "name": "Code",
    "unit": "commit",
    "type": "int",
    "color": "ajisai"
}


# response = requests.post(url=graph_endpoint, json=graph1_params, headers=headers)
# print(response.text)
# response = requests.post(url=graph_endpoint, json=graph2_params, headers=headers)
# print(response.text)

add_pixel_meditation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{MEDITATION_GRAPH_ID}"
add_pixel_code_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{CODE_CONSISTENCY_ID}"

add_pixel_meditation_params = {
    "date": f"{date}",
    "quantity": "1.0",
}
add_pixel_code_params = {
    "date": f"{date}",
    "quantity": "1",
}
# add_response = requests.post(url=add_pixel_meditation_endpoint, json=add_pixel_meditation_params, headers=headers)
# print(add_response.text)
# add_response = requests.post(url=add_pixel_code_endpoint, json=add_pixel_code_params, headers=headers)
# print(add_response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{MEDITATION_GRAPH_ID}/{date}"

new_pixel_params = {
    "quantity": "1.0"
}

# response = requests.put(url=update_endpoint, json=new_pixel_params, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{MEDITATION_GRAPH_ID}/{date}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
