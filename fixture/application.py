# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.manage import ManageHelper
from fixture.manage_projects import ManageProjectsHelper

class Application(object):
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError(f"Unrecognized browser {browser}")

        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.manage = ManageHelper(self)
        self.manage_projects = ManageProjectsHelper(self)
        self.base_url = base_url
        self.open_home_page()

    def open_home_page(self):
        # open homepage
        wd = self.wd
        if not (wd.current_url.endswith("/mantisbt-2.5.1/")):
            wd.get(self.base_url)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()

