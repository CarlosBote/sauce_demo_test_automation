from behave import given, when, then
from pages.login_page import LoginPage


@given('I am in the login page')
def step_i_am_in_the_login_page(context):
    context.login_page = LoginPage(context.browser)
    context.browser.get('https://www.saucedemo.com')


@when('I enter a valid username "{username}" and password "{password}"')
def step_i_enter_a_valid_username_and_password(context, username, password):
    context.login_page.login(username, password)


@then('I Should be redirect to my account page')
def i_should_be_redirect_to_my_account_page(context):
    expected_url = 'https://www.1saucedemo.com/inventory.html'
    assert context.browser.current_url == expected_url,\
        f"The expected URL is {expected_url}, buy got {context.browser.current_url()}"







