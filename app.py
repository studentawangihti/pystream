# app.py (Hanya ubah bagian bawahnya saja, atasnya SAMA PERSIS)
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rahasia_ninja'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/broadcaster')
def broadcaster():
    return render_template('broadcaster.html')

@app.route('/viewer')
def viewer():
    return render_template('viewer.html')

# --- SIGNALING EVENTS (SAMA SEPERTI SEBELUMNYA) ---
@socketio.on('join')
def handle_join(room):
    join_room(room)
    emit('ready', room=room, include_self=False) 

@socketio.on('offer')
def handle_offer(data):
    emit('offer', data, room=data['room'], include_self=False)

@socketio.on('answer')
def handle_answer(data):
    emit('answer', data, room=data['room'], include_self=False)

@socketio.on('candidate')
def handle_candidate(data):
    emit('candidate', data, room=data['room'], include_self=False)

if __name__ == '__main__':
    # PERUBAHAN DISINI: Tambahkan ssl_context='adhoc'
    # Ini akan membuat Flask berjalan di HTTPS
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, ssl_context='adhoc')