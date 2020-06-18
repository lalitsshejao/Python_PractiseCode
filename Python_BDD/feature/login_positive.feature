Feature: Logging in with valid credentials

  Scenario: User Login successfully

    Given I create a new user
    When I type email
    When I type password
    When I click on 'Login'
    Then I should see the text Welcome
    