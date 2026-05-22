from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_user_can_login(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.navigate()
    login.login("test_user", "password123")

    assert dashboard.is_loaded()