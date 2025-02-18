import datetime
import requests
import os

# Constants
TOKEN = os.environ.get("TOKEN")
TOKEN_HEADER_NAME = "X-USER-TOKEN"
ENDPOINT = "https://pixe.la/v1/users"
HEADERS = {TOKEN_HEADER_NAME: TOKEN}


def create_user(
        username: str,
        agree_terms_of_service: bool,
        not_minor: bool):
    create_user_request_body = {
        "token": TOKEN,
        "username": username,
        "agreeTermsOfService": "yes" if agree_terms_of_service else "no",
        "notMinor": "yes" if not_minor else "no"
    }

    response = requests.post(
        url=ENDPOINT,
        json=create_user_request_body)

    response.raise_for_status()
    return response


def create_graph(
        graph_id: str,
        graph_name: str,
        graph_unit: str,
        graph_type: str,
        graph_color: str,
        username: str):
    create_graph_request_body = {
        "id": graph_id,
        "name": graph_name,
        "unit": graph_unit,
        "type": graph_type,
        "color": graph_color
    }

    response =  requests.post(
        url=f"{ENDPOINT}/{username}/graphs",
        json=create_graph_request_body,
        headers=HEADERS)

    response.raise_for_status()
    return response


def create_pixel(
        date: datetime.date,
        quantity: str,
        graph_id: str,
        username: str):
    post_pixel_request_body = {
        "date": date.strftime("%Y%m%d"),
        "quantity": quantity
    }

    response = requests.post(
        url=f"{ENDPOINT}/{username}/graphs/{graph_id}",
        json=post_pixel_request_body,
        headers=HEADERS)

    response.raise_for_status()
    return response


def update_pixel(
        quantity: str,
        username: str,
        graph_id: str,
        date: datetime.date):
    response = requests.put(
        url=f"{ENDPOINT}/{username}/graphs/{graph_id}/{date.strftime("%Y%m%d")}",
        json={"quantity": quantity},
        headers=HEADERS)

    response.raise_for_status()
    return response


def delete_pixel(
        date: datetime.date,
        username: str,
        graph_id: str):
    response = requests.delete(
        url=f"{ENDPOINT}/{username}/graphs/{graph_id}/{date.strftime("%Y%m%d")}",
        headers=HEADERS)

    response.raise_for_status()
    return response
