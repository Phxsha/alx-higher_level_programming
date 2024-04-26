#!/usr/bin/python3
"""
Module: 0-hbtn_status

Python script that fetches https://alx-intranet.hbtn.io/status.
"""

if __name__ == "__main__":
    import urllib.request

    """
    Fetches https://alx-intranet.hbtn.io/status
    and displays the body response in a specific format.
    """
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
