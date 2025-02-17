import requests
import datetime as dt
import os

USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
GRAPHID = "graph10"
TOKEN_HEADER_NAME = "X-USER-TOKEN"

USER_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{USER_ENDPOINT}/{USERNAME}/graphs"
PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPHID}"
UPDATE_PIXEL_ENDPOINT = f"{PIXEL_ENDPOINT}/20250216"

headers = {TOKEN_HEADER_NAME: TOKEN}

# Create User - Step One
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(url=USER_ENDPOINT, json=user_params)
# print(response.text)

# Create Graph - Step Two
# create_graph_request_body = {
#     "id": GRAPHID,
#     "name": "Commit Graph",
#     "unit": "commit",
#     "type": "int",
#     "color": "shibafu"
# }
#
# response = requests.post(
#     url=GRAPH_ENDPOINT,
#     json=create_graph_request_body,
#     headers=headers)

# Post Pixel To Graph - Step Three
# post_pixel_request_body = {
#     "date": dt.datetime.now().strftime("%Y%m%d"),
#     "quantity": "10"
# }
#
# response = requests.post(
#     url=PIXEL_ENDPOINT,
#     json=post_pixel_request_body,
#     headers=headers)

# Update a PIXEL
# update_pixel_request_body = {"quantity": "2"}
#
# response = requests.put(
#     url=UPDATE_PIXEL_ENDPOINT,
#     json=update_pixel_request_body,
#     headers=headers)

# Delete a PIXEl
# response = requests.delete(url=UPDATE_PIXEL_ENDPOINT, headers=headers)
# print(response.text)


