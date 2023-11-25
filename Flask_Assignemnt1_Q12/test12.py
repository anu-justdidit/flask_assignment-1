#12. Build a Flask app that updates data in real-time using WebSocket connections with successful output


from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random
import time
from threading import Thread

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index_realtime.html')

@socketio.on('connect')
def handle_connect():
    emit('update', {'data': generate_sensor_data()}, broadcast=True)
    if not socketio.async_mode == 'threading':
        socketio.start_background_task(target=update_sensor_data)

def generate_sensor_data():
    # Generate random sensor data for demonstration
    return {'temperature': random.uniform(15.0, 35.0), 'humidity': random.uniform(40.0, 70.0)}

def update_sensor_data():
    while True:
        socketio.sleep(5)  # Update every 5 seconds
        data = {'data': generate_sensor_data()}
        emit('update', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)


