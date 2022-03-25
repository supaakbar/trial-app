from flask import Flask, render_template
import platform
import os

app = Flask(__name__)


@app.route('/')
def index():
    getOs = str(platform.platform())
    getVersion = str(os.environ['APP_VERSION'])
    return render_template('index.html', OS=getOs, VERSION=getVersion)

if __name__ == '__main__':
    app.run()