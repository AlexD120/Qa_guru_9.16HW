import pytest
from selene import browser


@pytest.fixture(params=[(1920, 1080), (1280, 720)])
def desktop_browser(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[(800, 480), (480, 360)])
def mobile_browser(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[(1920, 1080), (1280, 720), (800, 480), (480, 360)])
def skip_mobile_browser(request):

