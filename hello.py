#!/usr/bin/env python3

import os
import json

# Print the env variables

print("Content-Type: text/html")
print()
print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")
print(f"<p>HTTP_USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")
