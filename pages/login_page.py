from selenium.webdriver.common.by import By


class LoginPage:
    username_input = (By.ID, 'user-name')
    password_input = (By.ID, 'password')
    submit_btn= (By.ID, 'login-button')

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_submit(self):
        self.driver.find_element(*self.submit_btn).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()

