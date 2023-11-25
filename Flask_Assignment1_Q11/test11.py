#11. Create a real-time chat application using Flask-SocketIO.



from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index_chat.html')

@socketio.on('connect')
def handle_connect():
    emit('chat_message', {'message': 'You are connected.'})

@socketio.on('chat_message')
def handle_message(data):
    emit('chat_message', {'message': data['message']}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
