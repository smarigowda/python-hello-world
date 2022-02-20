from ast import keyword
from datetime import date, datetime
from os import getcwd
import os
import keyword
import sys
import datetime
import time
import html

help("keywords")
print("hello world!")

print(keyword.kwlist)

if 10.2.is_integer():
    print('it is iteger')
else:
    print("it is not")


current_dir = getcwd()
print(current_dir)

print(sys.platform)
print(sys.version)
# print(os.environ)

print(os.getenv('AWS_DEFAULT_REGION'))

print(datetime.date.today())
print(datetime.date.today().month)
print(datetime.date.today().day)
print(datetime.date.today().year)
print(datetime.date.isoformat(datetime.date.today()))

print(time.strftime('%H:%M:%S'))
print(time.strftime("%A %p"))

print(html.escape("This html contains script tag <script>var a;</script>"))
print(html.unescape("This html contains script tag &lt;script&gt;var a;&lt;/script&gt;"))