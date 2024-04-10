# this is the "conftest.py" file...

import pytest
from bs4 import BeautifulSoup

from web_app import create_app

#
# HELPER CLIENT FOR MAKING REQUESTS
# ... https://flask.palletsprojects.com/en/2.1.x/testing/
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/flask.md#testing
#

@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    app.config.update({"TESTING": True})
    return app.test_client()

def parse_page(html):
    """Params
        html : some HTML text, like the response.data returned by web_client.get()
    """
    return BeautifulSoup(html, features="html.parser")
