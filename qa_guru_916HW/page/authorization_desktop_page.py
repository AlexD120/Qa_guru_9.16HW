import allure
from selene import browser, have, be, by
from selene.support.shared.jquery_style import s, ss


class AuthorizationDesktopPage:
    def __init__(self):
        self.sign_in_button = s(".HeaderMenu-link--sign-in")
        self.verify_sign_in = s(".auth-form-header")

    @allure.step('1. Open the main page')
    def open(self):
        browser.open('/')
        return self

    @allure.step('2. Click the sign in button')
    def sign_in(self):
        self.sign_in_button.click()

    @allure.step('3. Checking the text to sign in')
    def verify_text_header(self):
        self.verify_sign_in.should(have.text('Sign in to GitHub'))
