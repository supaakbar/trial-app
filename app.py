from flask import Flask, render_template
import platform
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    getOs = str(platform.platform())
    getVersion = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).strip()
    return render_template('index.html', OS=getOs, VERSION=getVersion)

if __name__ == '__main__':
    app.run()