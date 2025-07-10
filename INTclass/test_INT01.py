"""
Opens https://rahulshettyacademy.com in Chrome browser.
Prints the title of the page in the console.
Navigates to https://www.wikipedia.org after 2 seconds.
Maximizes the browser window.
Prints the current URL of the page.
Goes back to https://rahulshettyacademy.com using browser navigation.
Takes a screenshot of loaded page and save it as rahul_homepage.png.
Closes the browser at the end of the script.
"""

from selenium import webdriver
import time

academy_url = "https://rahulshettyacademy.com"
wiki_url = "https://www.wikipedia.org"

def run_test(browser_name):

    if browser_name == "chrome":
        driver = webdriver.Chrome()


    elif browser_name == "firefox":
        driver = webdriver.Firefox()


    elif browser_name == "IE":
        driver = webdriver.Ie()


    else:
        print("\n Unsupported browser")
        return

    try:
        driver.get(academy_url)

        print("Page Title: ", driver.title)

        time.sleep(2)

        driver.get(wiki_url)

        driver.maximize_window()

        print("Current URL", driver.current_url)

        driver.back()

        time.sleep(2)

        screenshot_name = f"rahul_homepage_{browser_name}.png"
        driver.save_screenshot(screenshot_name)

    except Exception as error:
        print(f"An error occurred during execution: {error}")

    finally:
        driver.quit()

for browser in ["chrome", "firefox", "IE"]:
    run_test(browser)



