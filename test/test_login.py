# -*- coding: utf-8 -*-


def test_login(app):
    assert app.session.is_logged_in_as("administrator")
