from flask import Flask, render_template, request
import platform
import os
from datetime import datetime
import docker
import logging
import sys

app = Flask(__name__)

# linux command export env
cmdGetContainerID = 'export CONTAINER_ID=$(cat /proc/self/cgroup | grep -o  -e "docker-.*.scope" | head -n 1 | sed "s/docker-\(.*\).scope/\\1/")'
os.system(cmdGetContainerID)

# docker command
client = docker.from_env()
stats = client.containers.get(os.environ['CONTAINER_ID']).stats(stream=False)

# logging
logging.basicConfig(filename='./logs/app.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s : %(message)s')


@app.route('/')
def index():
    getOs = str(platform.platform())
    getVersion = str(os.environ['APP_VERSION'])
    getDate = str(datetime.today().strftime('%d-%m-%Y'))
    app.logger.info('USER ACCESS /')
    return render_template('index.html', OS=getOs, VERSION=getVersion, DATE=getDate, CPU=getCpu(), MEM=getMem())

@app.route("/getcpu/", methods=['GET'])
def getCpu():
    client = docker.from_env()
    stats = client.containers.get(os.environ['CONTAINER_ID']).stats(stream=False)
    usageDelta = stats['cpu_stats']['cpu_usage']['total_usage'] - stats['precpu_stats']['cpu_usage']['total_usage']
    systemDelta = stats['cpu_stats']['system_cpu_usage'] - stats['precpu_stats']['system_cpu_usage']
    len_cpu = len(stats['cpu_stats']['cpu_usage']['percpu_usage'])
    percentage = (usageDelta / systemDelta) * len_cpu * 100
    percent = str(round(percentage, 2))
    return percent

@app.route("/getmem/", methods=['GET'])
def getMem():
    client = docker.from_env()
    stats = client.containers.get(os.environ['CONTAINER_ID']).stats(stream=False)
    usage = stats['memory_stats']['usage']
    convertion = str(usage / 1000000)
    return convertion

if __name__ == '__main__':
    app.run(debug=True)