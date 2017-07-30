# -*- coding: utf-8 -*-

import random
import string
from model.project import Project


def random_string(prefix, maxlen):
    symbols = f"{string.ascii_letters}{string.digits}"
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Project(name=random_string("name", 10), description=random_string("desc", 10))
    for i in range(3)
    ]
