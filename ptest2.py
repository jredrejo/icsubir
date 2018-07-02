#!/home/rbencrfm/virtualenv/ptest/3.6/bin/python
# -*- coding: UTF-8 -*-

# Archivo para poder usar Flask con cgi-bin.
# Situado en /home/rbencrfm/public_html/ptest/cgi-bin/
# import cgitb; cgitb.enable()  # This line enables CGI error reporting
from wsgiref.handlers import CGIHandler

from sys import path
path.insert(0, '/home/rbencrfm/public_html/ptest/')
from app import app

CGIHandler().run(app)
