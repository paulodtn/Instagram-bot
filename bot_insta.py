from numpy import require
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import click

@click.command()
@click.option("--user", help = "Your acount password", required=True)
@click.option("--password_account", help = "Your acount password", required=True)
@click.option("--page", help = "Page to comment", required=True )

def instagram(user, password_account, page):
    """Program to automate comments on instagram page"""
    browser = webdriver.Firefox()
    browser.get("https://www.instagram.com")

    time.sleep(5)
    username = browser.find_element("css selector", "input[name='username']")
    password = browser.find_element("css selector", "input[name='password']")
    username.clear()
    password.clear()
    username.send_keys(user)
    password.send_keys(password_account)
    login = browser.find_element("css selector", "button[type='submit']").click()

    time.sleep(5)

    browser.get(page)
    text_area = browser.find_element("id", "textarea")
    text_area.send_keys("@recifeordinário")


if __name__ == '__main__':
    instagram()