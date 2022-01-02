import os
import platform

import requests
from faker import Faker
from flask import Flask, request, render_template, redirect

if os.name == 'posix':
    CLEAR = "clear"
    SLASH = "/"
else:
    CLEAR = "clear"
    SLASH = "\\"

app = Flask(__name__)


if __name__ == "__main__":
    app.run("0.0.0.0", port=3331, debug=True)
