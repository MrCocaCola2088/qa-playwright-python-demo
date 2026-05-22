def test_create_customer_and_verify_ui(page):
    # Simulate creating customer via UI
    page.goto("https://example-crm.com/customers")

    page.click("text=New Customer")
    page.fill("#name", "John Doe")
    page.click("text=Save")

    # Validate UI
    assert page.locator("text=John Doe").is_visible()