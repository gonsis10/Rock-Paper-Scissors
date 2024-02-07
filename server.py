import socket
from _thread import *
import pickle
from game import Game

server = "https://ftpupload.net/"
port = 21

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("started")
s.listen()

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

connected = set()
games = {}
client_count = 0


def client_manager(conn, id, game_id):
    global client_count
    conn.send(str.encode(str(id)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()
            if game_id in games:
                game = games[game_id]
                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(id, data)

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    client_count += 1
    id = 0
    game_id = (client_count - 1)//2
    if client_count % 2 == 1:
        games[game_id] = Game(game_id)
        print("New game.")
    else:
        games[game_id].ready = True
        id = 1

    start_new_thread(client_manager(), (conn, id, game_id))