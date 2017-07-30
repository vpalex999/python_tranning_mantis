# -*- coding: utf-8 -*-
class SessionHelper(object):

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_css_selector("input.pull-right").click()
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_css_selector("input.pull-right").click()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("span.user-info").text



    def logout(self):
        # logout
        wd = self.app.wd
        dropdown = wd.find_elements_by_css_selector("a.dropdown-toggle")
        dropdown[-1].click()
        wd.find_element_by_link_text("выход").click()

    def ensure_logout(self):
        """Ensure logout"""
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        status = False
        if not (wd.current_url.endswith("/mantisbt-2.5.1/login_page.php")):
            status = True
        return status



