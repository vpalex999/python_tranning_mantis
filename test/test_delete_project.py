# -*- coding: utf-8 -*-

import random
import pytest
from generator.project import testdata
from model.project import Project


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_delete_project(app, project):
    if not app.manage_projects.count():
        app.manage_projects.create(project)

    old_list_projects = app.manage_projects.get_projects_list()
    proj = random.choice(old_list_projects)
    app.manage_projects.delete(proj)
    assert len(old_list_projects) - 1 == app.manage_projects.count()
    old_list_projects.remove(proj)
    new_list_projects = app.manage_projects.get_projects_list()
    if len(new_list_projects):
        assert sorted(old_list_projects, key=Project.id_name) == sorted(new_list_projects, key=Project.id_name)

