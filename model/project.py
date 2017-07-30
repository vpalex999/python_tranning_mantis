# -*- coding: utf-8 -*-

class Project(object):

    def __init__(self, name, description=None):
        self.name = name
        self.description = description


    def __repr__(self):
        return f"{self.name}:{self.description}"

    def __eq__(self, other):
        return (self.name == other.name) and\
               (self.description is None or other.description is None or self.description == other.description)

    def id_name(self):
        if self.name:
            return str(self.name)