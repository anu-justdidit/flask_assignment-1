from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index_notifications.html')

@socketio.on('connect')
def handle_connect():
    emit('notification', {'message': 'Welcome! You are connected.'})

# Simulating notifications triggered by an event (e.g., a button click)
@socketio.on('trigger_notification')
def trigger_notification():
    emit('notification', {'message': 'New update!'}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
