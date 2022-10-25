from pytest_bdd import scenarios, given, when, then

# scenarios
scenarios('../features/login.feature')


@given('A user successfully landed at the login page')
def a_user_browses_to_betta_login_page():
    pass


# When steps
@when('A user inputs a username and password')
def a_user_input_username_and_password():
    pass


@when('Clicks the login button')
def clicks_the_login_button():
    pass


# Then steps
@then('The page should be redirected to Home Page')
def a_login_success_alert_should_be_displayed():
    pass


@then('An "Example Domain" text should be displayed in the center of the page')
def the_page_should_be_redirected_to_the_home_page():
    pass
