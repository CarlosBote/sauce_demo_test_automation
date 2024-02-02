from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os


def after_step(context, step):
    if step.status == "failed":
        take_screenshot(context, step)


def take_screenshot(context, step):
    # Crea un directorio para las capturas de pantalla si aún no existe
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    # Define el nombre del archivo con la marca de tiempo y el nombre del escenario
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    scenario_name = context.scenario.name.replace(' ', '_').replace('/', '_')
    step_name = step.name.replace(' ', '_').replace('/', '_')
    filename = f"screenshots/{scenario_name}_{step_name}_{timestamp}.png"

    # Toma la captura de pantalla y la guarda en el archivo definido
    context.browser.save_screenshot(filename)


def before_all(context):
    chrome_options = Options()

    if 'headless' in context.config.userdata:
        if context.config.userdata['headless'].lower() == 'true':
            chrome_options.add_argument("--headless")

    context.browser = webdriver.Chrome(options=chrome_options)
    context.browser.implicitly_wait(10)


def after_all(context):
    context.browser.quit()
