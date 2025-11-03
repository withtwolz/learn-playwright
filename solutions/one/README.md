# Problem 1 Solution

## Explaination

1. So we should begin by opening up the Login page to identify the elements manually. Open the link and right click the element and choose `Identify`, alternatively `CMD + Option + I` in most browsers.
   ![One inspect](../screenshots/one-1.png)
2. So after the page is loaded, we can grab and store the testbox element using `my_field = page.get_by_label("...")` because each input has a label
3. Now that we have the fields in the form we need to send them the provided username and password using `my_field.type("...")`
4. At this point we should have both fields filled in! Now we can click on the form's Login button using the `.click(a_locator)` like `page.click("#somebuttonid")`
5. In theory the login was successful, you should try running your script either by writing `cpaste` within an `ipython` shell and `Enter/Return` or by using the python runner in VSCode, the play button to the right of the file tab. You can throw a wait in the end of your script so its easier to see the login `page.wait_for_timeout(20000)` where `20000 == 20 seconds` or `20,0000 milliseconds`.
6. Now we can use playwright assertions to test we got through. Using a regular browser (non-playwright), login and identify the text/locator we can use to see login succeed.
7. We will use playwright's `expect` function: `from playwright.sync_api import expect` to write something like this:

```
from playwright.sync_api import expect, sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    ...
    ...
    ...
    ...
    ...
    ...
    expect(page.get_by_role(...)).to_contain_text("The login text!")
```

8. Finally if that expect worked we just need to be responsible and close the browser session with `browser.close()`
