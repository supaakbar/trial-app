from flask import Flask, render_template
import platform
import os
import sys

app = Flask(__name__)


@app.route('/')
def index():
    # return 'Hello, World!'
    # print("Hello Panji")
    # print("Operating System: ",os.name)
    # print("Platform System: ",platform.system())
    # print("Version Platform: ",platform.release())
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run()