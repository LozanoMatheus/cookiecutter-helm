#!/usr/bin/env python3
from __future__ import unicode_literals, absolute_import, print_function

import os
import shutil
from collections import OrderedDict
from cookiecutter.prompt import read_user_yes_no

try:
    input = raw_input
except NameError:
    pass

components = OrderedDict()
