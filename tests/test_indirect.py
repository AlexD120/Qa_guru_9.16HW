from qa_guru_916HW.application import app
import allure
import pytest


@allure.title('Desktop authorization functionality')
@allure.feature('Authorization')
@allure.story('User can sign in on desktop')
@allure.label('UI')
@allure.tag('smoke')
@allure.severity('critical')
@allure.label("owner", "Davydov")
@pytest.mark.desktop
@pytest.mark.parametrize("desktop_browser", [(1920, 1080), (1280, 720)], indirect=True)
def test_desktop_autorization(desktop_browser):
    app.simple_user_desctop_autorization_page.open()
    app.simple_user_desctop_autorization_page.sign_in()
    app.simple_user_desctop_autorization_page.verify_text_header()


@allure.title('Mobile authorization functionality')
@allure.feature('Authorization')
@allure.story('User can sign in on mobile')
@allure.label('UI')
@allure.tag('smoke')
@allure.severity('critical')
@allure.label("owner", "Davydov")
@pytest.mark.mobile
@pytest.mark.parametrize("mobile_browser", [(800, 480), (480, 360)], indirect=True)
def test_mobile_autorization(mobile_browser):
    app.simple_user_mobile_autorization_page.open()
    app.simple_user_mobile_autorization_page.buttonn()
    app.simple_user_mobile_autorization_page.sign_in()
    app.simple_user_mobile_autorization_page.verify_text_header()
