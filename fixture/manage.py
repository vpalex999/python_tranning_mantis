# -*- coding: utf-8 -*-

class ManageHelper(object):

    def __init__(self, app):
        self.app = app

    def open_manage(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/manage_overview_page.php")):
            wd.find_element_by_link_text("управление").click()

