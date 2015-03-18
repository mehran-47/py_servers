#!/usr/bin/env python3
from os import getpid
print('Content-type: text/html\n')
print('<title>Hello World</title>')
print('<p>my PID:' + str(getpid())+'</p>')