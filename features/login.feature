Feature: Login
    The user must be registered in BETTA

Background:
    Given A user successfully landed at the login page

Scenario: As a user, I am able to log in to the system
    When A user inputs a username and password
    And Clicks the login button
    Then The page should be redirected to Home Page
    And An "Example Domain" text should be displayed in the center of the page