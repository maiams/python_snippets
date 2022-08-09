from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


def before_all(context):
    context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


def before_scenario(context, scenario):
    context.driver.maximize_window()


def before_step(context, step):
    context.driver.implicitly_wait(7)


def after_all(context):
    sleep(5)
    context.driver.close()
