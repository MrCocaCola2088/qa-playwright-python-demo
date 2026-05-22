from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import pytest
@pytest.mark.ui
def test_switch_between_tenants(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.navigate()
    login.login("tenant_user", "password123")

    dashboard.select_tenant("Tenant A")
    assert page.locator("text=Tenant A Dashboard").is_visible()

    dashboard.select_tenant("Tenant B")
    assert page.locator("text=Tenant B Dashboard").is_visible()