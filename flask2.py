from flask import Flask
import threading
import os
import requests
import json
import httplib2
import time
from ngrokUtility import ngrokUtility
app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'Hello, World!'



x=ngrokUtility("5000")
print(x.publicAddr(5))
app.run()
