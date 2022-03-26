from flask import Flask, render_template
import platform
import os
from datetime import datetime
import docker

app = Flask(__name__)
client = docker.from_env()
stats = client.containers.get('trial-app').stats(stream=False)


@app.route('/')
def index():
    getOs = str(platform.platform())
    getVersion = str(os.environ['APP_VERSION'])
    getDate = str(datetime.today().strftime('%d-%m-%Y'))
    return render_template('index.html', OS=getOs, VERSION=getVersion, DATE=getDate, CPU=getCpu(), MEM=getMem())

def getCpu():
    usageDelta = stats['cpu_stats']['cpu_usage']['total_usage'] - stats['precpu_stats']['cpu_usage']['total_usage']
    systemDelta = stats['cpu_stats']['system_cpu_usage'] - stats['precpu_stats']['system_cpu_usage']
    len_cpu = len(stats['cpu_stats']['cpu_usage']['percpu_usage'])
    percentage = (usageDelta / systemDelta) * len_cpu * 100
    percent = round(percentage, 2)
    return percent

def getMem():
    usage = stats['memory_stats']['usage']
    convertion = usage / 1000000
    return convertion

if __name__ == '__main__':
    app.run()