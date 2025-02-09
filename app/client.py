import socket
import json

SERVER_IP = "localhost"  # Altere para o IP do servidor se necessário
SERVER_PORT = 7777

def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    print("Conectado ao servidor, aguardando perguntas...")

    # Aguarda as perguntas do servidor
    data = json.loads(client_socket.recv(4096).decode())
    if data["type"] == "questoes":
        questions = data["dados"]
        print(questions)
        #score = play_quiz(questions)

        # Envia a pontuação para o servidor
        #client_socket.send(json.dumps({"score": score}).encode())
        #print(f"Pontuação enviada: {score}")

        # Aguarda o resultado final
        #result = json.loads(client_socket.recv(1024).decode())
        #if result["type"] == "result":
            #print("Resultado final:", result["scores"])

    client_socket.close()

if __name__ == "__main__":
    connect_to_server()
