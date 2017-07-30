# -*- coding: utf-8 -*-

from model.project import Project

class ManageProjectsHelper(object):

    def __init__(self, app):
        self.app = app
        self.projects_chace = None

    def open_projects(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/manage_proj_page.php")):
            self.app.manage.open_manage()
            wd.find_element_by_link_text("Управление проектами").click()

    def create(self, project):
        self.open_projects()
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='создать новый проект']").click()
        wd.find_element_by_id("project-name").click()
        wd.find_element_by_id("project-name").clear()
        wd.find_element_by_id("project-name").send_keys(project.name)
        if project.description is not None:
            wd.find_element_by_id("project-description").click()
            wd.find_element_by_id("project-description").clear()
            wd.find_element_by_id("project-description").send_keys(project.description)
        wd.find_element_by_css_selector("input[value='Добавить проект']").click()
        self.projects_chace = None



    def get_projects_list(self):
        if self.projects_chace is None:
            self.projects_chace = []
            self.open_projects()
            wd = self.app.wd
            table_proj = wd.find_element_by_css_selector("div.table-responsive")
            projects = table_proj.find_elements_by_tag_name("tr")
            assert len(projects) != 0
            projects[:1] = []
            for project in projects:
                td = project.find_elements_by_tag_name("td")
                name = td[0].text
                description = td[-1].text
                self.projects_chace.append(Project(name=name, description=description))

        return list(self.projects_chace)




