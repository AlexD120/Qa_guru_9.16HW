from qa_guru_916HW.page.authorization_desktop_page import AuthorizationDesktopPage
from qa_guru_916HW.page.autorization_mobile_page import AuthorizationMobilePage


class Application:
    def __init__(self):
        self.simple_user_desctop_autorization_page = AuthorizationDesktopPage()
        self.simple_user_mobile_autorization_page = AuthorizationMobilePage()


app = Application()
