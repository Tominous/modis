import requests
import lxml.html as html
import io

import datetime

url = 'https://kakko.pandorabots.com/pandora/talk?botid=f6a012073e345a08&amp;skin=chat'


def get_botcust2():
    """Gets a botcust2, used to identify a speaker with Mitsuku

    Returns:
        botcust2 (str): The botcust2 identifier
    """

    from ._constants import pipe_api_mitsuku
    tree_item = pipe_api_mitsuku.insert("", "end", text="get_botcust2()", values=(str(datetime.datetime.now()).split('.')[0]))

    # Set up http request packages
    params = {
        'botid': 'f6a012073e345a08',
        'amp;skin': 'chat'
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Host': 'kakko.pandorabots.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.36'
    }

    # Get response from http POST request to url
    pipe_api_mitsuku.insert(tree_item, "end", text="HTTP POST", values=(str(datetime.datetime.now()).split('.')[0]))
    response = requests.post(
        url,
        params=params,
        headers=headers
    )

    # Try to extract Mitsuku response from POST response
    pipe_api_mitsuku.insert(tree_item, "end", text="Parse", values=(str(datetime.datetime.now()).split('.')[0]))
    try:
        return response.headers['set-cookie'][9:25]
    except IndexError:
        return False


def query(botcust2, message):
    """Sends a message to Mitsuku and retrieves the reply

    Args:
        botcust2 (str): The botcust2 identifier
        message (str): The message to send to Mitsuku

    Returns:
        reply (str): The message Mitsuku sent back
    """

    from ._constants import pipe_api_mitsuku
    tree_item = pipe_api_mitsuku.insert("", "end", text="query()", values=(str(datetime.datetime.now()).split('.')[0]))

    # Set up http request packages
    params = {
        'botid': 'f6a012073e345a08',
        'amp;skin': 'chat'
    }
    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': str(len(message) + 34),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'botcust2=' + botcust2,
        'DNT': '1',
        'Host': 'kakko.pandorabots.com',
        'Origin': 'https://kakko.pandorabots.com',
        'Referer': 'https://kakko.pandorabots.com/pandora/talk?botid=f6a012073e345a08&amp;skin=chat',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.36'
    }
    data = {
        'botcust2': botcust2,
        'message': message
    }

    # Get response from http POST request to url
    pipe_api_mitsuku.insert(tree_item, "end", text="HTTP POST", values=(str(datetime.datetime.now()).split('.')[0]))
    response = requests.post(
        url,
        params=params,
        headers=headers,
        data=data
    )

    # Parse response
    pipe_api_mitsuku.insert(tree_item, "end", text="Parse", values=(str(datetime.datetime.now()).split('.')[0]))
    parsed = html.parse(io.StringIO(response.text)).getroot()

    # Try to extract Mitsuku response from POST response
    try:
        return parsed[1][2][0][2].tail[1:]
    except IndexError:
        return False
