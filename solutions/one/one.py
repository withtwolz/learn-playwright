from playwright.sync_api import expect, sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practice.expandtesting.com/login")
    username_field = page.get_by_label("username")
    password_field = page.get_by_label("password")
    username_field.type("practice")
    password_field.type("SuperSecretPassword!")
    page.click("#submit-login")
    expect(page.get_by_role("alert")).to_contain_text("You logged into a secure area!")
    browser.close()
