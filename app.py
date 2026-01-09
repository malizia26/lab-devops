from flask import Flask, render_template_string
import psutil
import socket
import datetime

app = Flask(__name__)

# Template HTML intégré pour faire joli sans fichier séparé
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>RPi5 Monitoring</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body { font-family: sans-serif; background: #121212; color: white; text-align: center; padding: 50px; }
        .card { background: #1e1e1e; border-radius: 15px; padding: 20px; display: inline-block; box-shadow: 0 4px 8px rgba(0,0,0,0.5); }
        .stat { font-size: 2em; color: #00ff88; }
        .label { color: #888; text-transform: uppercase; font-size: 0.8em; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 RPi5 Dashboard</h1>
        <p class="label">Hostname</p>
        <p>{{ hostname }}</p>
        <hr>
        <p class="label">CPU Usage</p>
        <p class="stat">{{ cpu }}%</p>
        <p class="label">RAM Usage</p>
        <p class="stat">{{ ram }}%</p>
        <hr>
        <p style="font-size: 0.7em; color: #555;">Dernière MAJ: {{ time }}</p>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    stats = {
        'hostname': socket.gethostname(),
        'cpu': psutil.cpu_percent(interval=1),
        'ram': psutil.virtual_memory().percent,
        'time': datetime.datetime.now().strftime("%H:%M:%S")
    }
    return render_template_string(HTML_TEMPLATE, **stats)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
