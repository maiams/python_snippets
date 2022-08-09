from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



@given('User access "{url}"')
def step_impl(context, url):
    """
    :type context: behave.runner.Context
    """
    context.driver.get(url)


@when('User search for "{q}"')
def step_impl(context, q):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.NAME, "q").send_keys(q, Keys.ENTER)


@then('User must see "{text}" results')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    assert context.driver.find_element(By.XPATH, f"//*[contains(text(), '{text}')]")
