from behave import given, when, then
from pages.login_page import LoginPage


@given("I enter to the url '{page}'")
def step_enter_web_page(context, page):
    context.browser.get(page)


@when('I enter a valid username "{username}" and password "{password}"')
def step_i_enter_a_valid_username_and_password(context, username, password):
    context.login_page = LoginPage(context.browser)
    context.login_page.login(username, password)


@then('I Should be redirect to my account page')
def i_should_be_redirect_to_my_account_page(context):
    expected_url = 'https://www.saucedemo.com/inventory.html'
    assert context.browser.current_url == expected_url, \
        f"The expected URL is {expected_url}, buy got {context.browser.current_url}"
