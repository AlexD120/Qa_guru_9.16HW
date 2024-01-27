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
def test_desktop_autorization(skip_mobile_browser):
    if skip_mobile_browser == 'mobile':
        pytest.skip("Мобильный размер окна браузера ")
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
def test_mobile_autorization(skip_mobile_browser):
    if skip_mobile_browser == 'desktop':
        pytest.skip("Десктопный размер окна браузера ")
    app.simple_user_mobile_autorization_page.open()
    app.simple_user_mobile_autorization_page.buttonn()
    app.simple_user_mobile_autorization_page.sign_in()
    app.simple_user_mobile_autorization_page.verify_text_header()
