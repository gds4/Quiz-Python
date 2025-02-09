import socket
import threading
import json
import select
import time  # para o sleep
from database.database import get_db

def obter_questao_service():
    db = next(get_db())
    from services.questao_service import QuestaoService
    return QuestaoService(db)

host = 'localhost'
port = 7777

fila_jogadores = []
partidas_andamento = {}
questao_service = obter_questao_service()

def monitor_cliente(cliente):
    """
    Monitora a conexão do cliente.
    Se o cliente desconectar enquanto está na fila ou partida, remove-o da fila.
    """
    while True:
        try:
            ready, _, _ = select.select([cliente], [], [], 1)
            if ready:
                data = cliente.recv(1024)
                if not data:
                    break
        except Exception:
            break
    try:
        if cliente in fila_jogadores:
            fila_jogadores.remove(cliente)
            print("Cliente removido da fila por desconexão.")
    except ValueError:
        pass

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        servidor.bind((host, port))
        servidor.listen(5)
    except Exception as e:
        print('Não foi possível se conectar ao servidor:', e)
        return

    print(f"Servidor iniciado em {host}:{port}")

    while True:
        cliente, endereco_ip_cliente = servidor.accept()
        print(f"Conexão recebida de {endereco_ip_cliente}")
        fila_jogadores.append(cliente)
        monitor_thread = threading.Thread(target=monitor_cliente, args=(cliente,))
        monitor_thread.daemon = True
        monitor_thread.start()

        if len(fila_jogadores) >= 2:
            jogador_um = fila_jogadores.pop(0)
            jogador_dois = fila_jogadores.pop(0)
            thread_partida = threading.Thread(target=iniciar_partida, args=[jogador_um, jogador_dois])
            thread_partida.start()

def iniciar_partida(jogador_um, jogador_dois):
    """
    Inicia uma partida entre dois jogadores:
      - Envia as questões e uma identificação ("player": "p1" ou "p2") para cada um.
      - Aguarda que ambos os jogadores enviem suas pontuações e só então envia o resultado.
    """
    partida_id = f'partida_{id(jogador_um)}_{id(jogador_dois)}'
    partidas_andamento[partida_id] = {'jogadores': [jogador_um, jogador_dois], 'pontuacoes': {}}
    questoes = questao_service.obter_questoes_aleatorias()
    questoes = [questao.to_dict() for questao in questoes]

    # Envia as questões com a identificação apropriada.
    try:
        jogador_um.send(json.dumps({'type': 'questoes', 'dados': questoes, 'player': 'p1'}).encode())
    except Exception as e:
        print("Erro ao enviar questões para jogador 1:", e)
    try:
        jogador_dois.send(json.dumps({'type': 'questoes', 'dados': questoes, 'player': 'p2'}).encode())
    except Exception as e:
        print("Erro ao enviar questões para jogador 2:", e)

    scores = {}

    def receber_pontuacao(jogador, key):
        try:
            # Removemos o timeout para que o recebimento bloqueie até que o jogador envie sua pontuação.
            data = jogador.recv(1024)
            if data:
                msg = json.loads(data.decode())
                if msg.get("type") == "pontuacao":
                    scores[key] = msg["pontuacao"]
            else:
                print(f"Jogador {key} desconectou (dados vazios).")
                scores[key] = 0
        except Exception as e:
            print(f"Erro recebendo pontuação de {key}: {e}")
            scores[key] = 0

    # Inicia threads para receber pontuações de ambos os jogadores.
    t1 = threading.Thread(target=receber_pontuacao, args=(jogador_um, "p1"))
    t2 = threading.Thread(target=receber_pontuacao, args=(jogador_dois, "p2"))
    t1.start()
    t2.start()

    # Aguarda num loop até que scores tenha ambas as pontuações.
    while len(scores) < 2:
        time.sleep(0.5)
    print("Pontuações recebidas:", scores)

    result_msg = json.dumps({"type": "resultado", "pontuacoes": scores})
    for jogador in [jogador_um, jogador_dois]:
        try:
            jogador.send(result_msg.encode())
        except Exception as e:
            print("Erro ao enviar resultado para um jogador:", e)
        finally:
            jogador.close()

if __name__ == '__main__':
    main()
