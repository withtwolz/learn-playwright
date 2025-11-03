"""Try out your playwright setup"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practice.expandtesting.com/login")
    print(page.inner_html)
    page.wait_for_timeout(5000)
    browser.close()
