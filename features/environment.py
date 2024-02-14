from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os


def after_step(context, step):
    if step.status == "failed":
        take_screenshot(context, step)


def take_screenshot(context, step):
    # Create a directory for the screenshots if it doesn't exist
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    # Define the file name with timestamp and scenario name
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    scenario_name = context.scenario.name.replace(' ', '_').replace('/', '_')
    step_name = step.name.replace(' ', '_').replace('/', '_')
    filename = f"screenshots/{scenario_name}_{step_name}_{timestamp}.png"

    # Takes the screenshot and save it in the dir
    context.browser.save_screenshot(filename)


def before_all(context):
    chrome_options = Options()

    if 'headless' in context.config.userdata:
        if context.config.userdata['headless'].lower() == 'true':
            chrome_options.add_argument("--headless")

    context.browser = webdriver.Chrome(options=chrome_options)
    context.browser.maximize_window()
    context.browser.implicitly_wait(10)


def after_all(context):
    context.browser.quit()
