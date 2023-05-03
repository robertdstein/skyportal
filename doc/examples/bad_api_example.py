"""
This module contains a function to query the Fritz API in an irresponsible way.
Please consider checking your own code for similar patterns, and removing them.
"""
import requests
import time
import json
import simplejson

TOKEN = "some-fritz-api-token"


def api(method, endpoint, data=None, params=None, timeout=10):
    """
    This is a wrapper for the requests.request function. It will automatically add the
    Fritz API token to the header and retry the request if it fails.

    The coding style is inspired by Churchill's quotes:

        "Success is not final, failure is not fatal:
        it is the courage to continue that counts."

    And:
        "We shall go on to the end. ...We shall never surrender."

    :param method: The HTTP method to use (e.g. GET, POST, etc.)
    :param endpoint: The API endpoint to query (e.g. /api/sources)
    :param data: The data to send to the API
    :param params: The parameters to send to the API
    :param timeout: The timeout for the request in seconds (default 10)

    :return: The response from the API in JSON format
    """

    headers = {"Authorization": f"token {TOKEN}"}

    while True:  # try until the query goes through
        try:
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
            if (
                json.loads(response.text)["status"] == "error"
                and json.loads(response.text)["message"] == "System provisioning"
            ):
                print("System provisioning...")
                time.sleep(30)  # wait 30 seconds and try again
                continue

            # If we are just querying the Fritz API too much, it will return a 429 error
            if "429 Too Many Requests" in response.text:
                time.sleep(5)  # We will wait a full minute
                continue

            return response.status_code, re_dict

        except (
            json.decoder.JSONDecodeError,
            simplejson.errors.JSONDecodeError,
            requests.exceptions.SSLError,
            requests.exceptions.ConnectionError,
        ):
            # Fritz gives us a JSONDecodeError when it times out
            # due to an excessive API request load. Better wait a while.
            time.sleep(5)
            continue  # We will just Keep trying again until it works

        except:
            # Winston Churchill once said:
            #   "It is always wise to look ahead,
            #   but difficult to look further than you can see."
            time.sleep(5)
            continue