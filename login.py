#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import secret
import os
from http.cookies import SimpleCookie

# set up cgi
s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

formOK = username == secret.username and password == secret.password

cookie = SimpleCookie(os.environ['HTTP_COOKIE'])
cu = None
cp = None

if cookie.get("username"):
    cu = cookie.get("username").value
if cookie.get("password"):
    cp = cookie.get("password").value

cookieOK = cu == secret.username and cp == secret.password

if cookieOK:
    username = cu
    password = cp


if formOK:
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")

print("Content-Type: text/html")
print()

if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())
 