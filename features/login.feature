Feature: Login feature
  As a user
  I want to login to my account
  So i can access to the shop

  Background: Enter web page
    Given I enter to the url 'https://www.saucedemo.com'

  Scenario Outline: Successful login
    When I enter a valid username "<username>" and password "<password>"
    Then I Should be redirect to my account page

    Examples:
      | username      | password     |
      | standard_user | secret_sauce |
      | error_user    | secret_sauce |