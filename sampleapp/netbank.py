from flask import Flask
from flask import render_template
import socket
import random
import os
import time
import math

app = Flask(__name__)

success=math.floor(time.time())
failure=0

@app.route("/")
def main():
    return render_template('netbank.html', name=socket.gethostname())

@app.route("/metrics")
def metrics():
    global success
    success += math.floor(random.random()*1000)
    global failure
    failure += math.floor(random.random()*100)
    return render_template('metrics.html',
                           name=socket.gethostname(),
                           login_time=random.random(),
                           transaction_count_success=success,
                           transaction_count_failed=failure)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
