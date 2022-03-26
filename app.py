from flask import Flask, render_template
import platform
import os
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    getOs = str(platform.platform())
    getVersion = str(os.environ['APP_VERSION'])
    getDate = str(datetime.today().strftime('%d-%m-%Y'))
    return render_template('index.html', OS=getOs, VERSION=getVersion, DATE=getDate)

if __name__ == '__main__':
    app.run()