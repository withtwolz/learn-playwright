# Learn Playwright

A hands-on guide to learning Playwright for test automation, designed for QA engineers.

## Prerequisites

-   [ ] Python 3.13+ (Install from [python.org](https://www.python.org/downloads/))
-   [ ] Setup the environment by running:

```bash
make setup
```

## Basic Exercises

Complete these exercises to learn the fundamentals of Playwright. Each exercise builds upon the previous ones, introducing new concepts and techniques.

1. [ ] **Login Form Automation [Loose Guide](./solutions/one/README.md)|[Solution](./solutions/one/one.py)**

    - Navigate to the login page
    - Fill in username and password fields
    - Submit the form
    - Verify successful/failed login
    - URL: https://practice.expandtesting.com/login

2. [ ] **Form Validation Testing**

    - Test various form inputs (text, numbers, dates)
    - Validate error messages
    - Test submission with valid/invalid data
    - URL: https://practice.expandtesting.com/form-validation

3. [ ] **Dynamic Controls**

    - Work with appearing/disappearing elements
    - Handle async operations
    - Verify element states
    - URL: https://practice.expandtesting.com/dynamic-controls

4. [ ] **File Upload/Download**

    - Upload a file to the server
    - Verify successful upload
    - Download a file
    - Verify downloaded content
    - URL: https://practice.expandtesting.com/upload

5. [ ] **Drag and Drop Operations**

    - Perform basic drag and drop
    - Verify element positions
    - Handle multiple drag targets
    - URL: https://practice.expandtesting.com/drag-and-drop

6. [ ] **Table Data Verification**

    - Read table contents
    - Sort columns
    - Filter data
    - Verify cell values
    - URL: https://practice.expandtesting.com/dynamic-table

7. [ ] **Working with Alerts**

    - Handle different types of alerts
    - Verify alert messages
    - Accept/Dismiss alerts
    - URL: https://practice.expandtesting.com/js-dialogs

8. [ ] **Multiple Windows/Tabs**

    - Open new windows/tabs
    - Switch between contexts
    - Handle popups
    - URL: https://practice.expandtesting.com/windows

9. [ ] **Iframe Interactions**

    - Locate iframes
    - Switch between frames
    - Interact with elements inside frames
    - URL: https://practice.expandtesting.com/iframe

10. [ ] **API Testing with Playwright**
    - Make HTTP requests
    - Verify response status
    - Check response body
    - Handle authentication
    - URL: https://practice.expandtesting.com/api/api-docs/

## Advanced Topic: Page Object Model (POM)

After completing the basic exercises, refactor them using the Page Object Model pattern. POM helps create more maintainable and reusable test code.

### Example POM Structure:

```python
# pages/login_page.py
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")

    async def login(self, username, password):
        await self.username_input.fill(username)
        await self.password_input.fill(password)
        await self.login_button.click()

# tests/test_login.py
from pages.login_page import LoginPage

async def test_valid_login(page):
    login_page = LoginPage(page)
    await page.goto("https://practice.expandtesting.com/login")
    await login_page.login("test_user", "test_pass")
    assert await page.locator(".success-message").is_visible()
```

### Convert Basic Exercises to POM

-   [ ] Refactor Exercise 1 (Login Form) using POM
-   [ ] Refactor Exercise 2 (Form Validation) using POM
-   [ ] Refactor Exercise 3 (Dynamic Controls) using POM
-   [ ] Refactor Exercise 4 (File Upload/Download) using POM
-   [ ] Refactor Exercise 5 (Drag and Drop) using POM
-   [ ] Refactor Exercise 6 (Table Data) using POM
-   [ ] Refactor Exercise 7 (Alerts) using POM
-   [ ] Refactor Exercise 8 (Multiple Windows) using POM
-   [ ] Refactor Exercise 9 (Iframes) using POM
-   [ ] Refactor Exercise 10 (API Testing) using POM

## Additional Resources

-   [Official Playwright Documentation](https://playwright.dev/python/docs/intro)
-   [Practice Website](https://practice.expandtesting.com/)
-   [Playwright Best Practices](https://playwright.dev/python/docs/best-practices)
