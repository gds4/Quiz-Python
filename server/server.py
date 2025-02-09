import socket
import threading
import json
import select
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
    Se o cliente desconectar enquanto está na fila, remove-o da fila.
    """
    while True:
        try:
            # Usa select para aguardar dados por até 1 segundo.
            ready, _, _ = select.select([cliente], [], [], 1)
            if ready:
                # Se o cliente estiver pronto para leitura, tenta receber dados.
                data = cliente.recv(1024)
                # Se não receber dados, a conexão foi encerrada.
                if not data:
                    break
        except Exception as e:
            break
    # Tenta remover o cliente da fila, se ele ainda estiver lá.
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
        # Inicia uma thread para monitorar se o cliente desconecta enquanto está na fila.
        monitor_thread = threading.Thread(target=monitor_cliente, args=(cliente,))
        monitor_thread.daemon = True
        monitor_thread.start()

        # Se houver pelo menos dois jogadores na fila, inicia uma partida.
        if len(fila_jogadores) >= 2:
            jogador_um = fila_jogadores.pop(0)
            jogador_dois = fila_jogadores.pop(0)
            thread_partida = threading.Thread(target=iniciar_partida, args=[jogador_um, jogador_dois])
            thread_partida.start()

def iniciar_partida(jogador_um, jogador_dois):
    partida_id = obter_id(jogador_um, jogador_dois)
    partidas_andamento[partida_id] = {'jogadores': [jogador_um, jogador_dois], 'pontuacoes': {}}
    questoes = questao_service.obter_questoes_aleatorias()
    questoes = [questao.to_dict() for questao in questoes]

    for jogador in [jogador_um, jogador_dois]:
        try:
            jogador.send(json.dumps({'type': 'questoes', 'dados': questoes}).encode())
        except Exception as e:
            print("Erro ao enviar questões para um jogador:", e)

def obter_id(jogador_um, jogador_dois):
    return f'partida_{id(jogador_um)}_{id(jogador_dois)}'

if __name__ == '__main__':
    main()
