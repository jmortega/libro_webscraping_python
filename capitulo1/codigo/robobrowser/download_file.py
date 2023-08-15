#!/usr/bin/env python
# -*- coding: utf-8 -*-

import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from robobrowser import RoboBrowser

browser = RoboBrowser(history=True)

url = "https://docs.python.org/3.11/archives/python-3.11.2-docs-pdf-letter.zip"
zip_file_path = "python-3.11.2-docs-pdf-letter.zip"

# obtener la sesión del objeto browser
request = browser.session.get(url, stream=True)

with open(zip_file_path, "wb") as zip_file:
    zip_file.write(request.content)
