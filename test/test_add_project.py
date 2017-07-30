# -*- coding: utf-8 -*-

import pytest
from generator.project import testdata
from model.project import Project


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):
    old_list_projects = app.manage_projects.get_projects_list()
    app.manage_projects.create(project)
    new_list_projects = app.manage_projects.get_projects_list()
    assert len(old_list_projects) +1 == len(new_list_projects)
    old_list_projects.append(project)
    assert sorted(old_list_projects, key=Project.id_name) == sorted(new_list_projects, key=Project.id_name)

