"""
This module contains a function to query the Fritz API in a responsible way.
Please consider copying it.
"""
import requests
import time
import json
import simplejson
import backoff

TOKEN = "some-fritz-api-token"


class TooManyRequests(requests.exceptions.RequestException):
    """Too many API calls by user"""


@backoff.on_exception(  # Handle HTTP errors
    backoff.expo,  # Exponentially longer intervals between retries
    requests.exceptions.HTTPError,  # HTTP errors
    max_time=300  # 5 minutes is max timeout
)
@backoff.on_exception(  # Handle various timeouts
    backoff.expo,  # Exponentially longer intervals between retries
    (
            requests.exceptions.Timeout,  # Timeout errors
            json.decoder.JSONDecodeError,  # Fritz gives these error when it's overloaded
            simplejson.errors.JSONDecodeError,
            requests.exceptions.SSLError,
            requests.exceptions.ConnectionError,
    ),
    max_time=300 # 5 minutes is max timeout
)
@backoff.on_exception(  # Handle excessive API calls
    backoff.expo,  # Exponentially longer intervals between retries
    TooManyRequests,  # If we are personally making too many requests
    max_time=600  # 10 minutes is max timeout
)
def api(method, endpoint, data=None, params=None, timeout=300):
    """
    This is a wrapper for the requests.request function. It will automatically add the
    Fritz API token to the header and retry the request if it fails.

    The coding style is inspired by Churchill's quotes:

        "To improve is to change. To be perfect is to change often"

    And:

        "The price of greatness is responsibility."

    :param method: The HTTP method to use (e.g. GET, POST, etc.)
    :param endpoint: The API endpoint to query (e.g. /api/sources)
    :param data: The data to send to the API
    :param params: The parameters to send to the API
    :param timeout: The timeout for the request in seconds (default 300)

    :return: The response from the API in JSON format
    """

    headers = {"Authorization": f"token {TOKEN}"}

    time.sleep(10)  # Always wait 10s between API calls, to avoid overloading the API

    response = requests.request(
        method,
        endpoint,
        json=data,
        headers=headers,
        params=params,
        timeout=timeout,
    )
    re_dict = response.json()

    # If the Fritz API is still provisioning, it will return a 500 error
    if json.loads(response.text)["message"] == "System provisioning":
        print("System provisioning...")
        time.sleep(30)  # wait 30 seconds
        raise requests.exceptions.HTTPError  # We will then try again

    # If we are just querying the Fritz API too much, it will return a 429 error
    if "429 Too Many Requests" in response.text:
        time.sleep(60)  # wait 60 seconds
        raise TooManyRequests("Too many requests")  # We will then try again

    return response.status_code, re_dict