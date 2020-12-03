from flask import Flask
from flask import render_template
import socket
import random
import os
import time

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('netbank.html', name=socket.gethostname())

@app.route("/metrics")
def metrics():
    return render_template('metrics.html',
                           name=socket.gethostname(),
                           login_time=random.random(),
                           transaction_count_success=time.time()+random.random()-0.5,
                           transaction_count_failed=0.000000001*time.time()*random.random())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
