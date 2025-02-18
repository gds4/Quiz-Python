import socket
import threading
import json
import select
import time
from database.database import get_db

class QuizServer:
    def __init__(self, host='localhost', port=7777):
        self.host = host
        self.port = port
        self.fila_jogadores = []
        self.questao_service = self.obter_questao_service()
    
    def obter_questao_service(self):
        db = next(get_db())
        from services.questao_service import QuestaoService
        return QuestaoService(db)

    def monitor_cliente(self, cliente):
        while cliente in self.fila_jogadores:
            try:
                ready, _, _ = select.select([cliente], [], [], 1)
                if ready:
                    data = cliente.recv(1024)
                    if not data:
                        break
            except Exception:
                break
        try:
            if cliente in self.fila_jogadores:
                self.fila_jogadores.remove(cliente)
                print("Cliente removido da fila por desconexão.")
        except ValueError:
            pass
    
    def start(self):
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            servidor.bind((self.host, self.port))
            servidor.listen(5)
        except Exception as e:
            print('Não foi possível se conectar ao servidor:', e)
            return

        print(f"Servidor iniciado em {self.host}:{self.port}")

        while True:
            cliente, endereco_ip_cliente = servidor.accept()
            print(f"Conexão recebida de {endereco_ip_cliente}")
            
            try:
                data = cliente.recv(1024).decode()
                msg = json.loads(data)
                tipo_jogo = msg.get("type")

                if tipo_jogo == "singleplayer":
                    threading.Thread(target=self.iniciar_partida_singleplayer, args=[cliente]).start()
                elif tipo_jogo == "multiplayer":
                    self.fila_jogadores.append(cliente)
                    threading.Thread(target=self.monitor_cliente, args=[cliente], daemon=True).start()
                    if len(self.fila_jogadores) >= 2:
                        jogador_um = self.fila_jogadores.pop(0)
                        jogador_dois = self.fila_jogadores.pop(0)
                        threading.Thread(target=self.iniciar_partida_multiplayer, args=[jogador_um, jogador_dois]).start()
                else:
                    cliente.close()
            except Exception as e:
                print("Erro ao receber mensagem inicial:", e)
                cliente.close()
    
    def iniciar_partida_multiplayer(self, jogador_um, jogador_dois):
        partida_id = f'partida_{id(jogador_um)}_{id(jogador_dois)}'
        questoes = self.questao_service.obter_questoes_aleatorias()
        questoes = [questao.to_dict() for questao in questoes]
        
        try:
            jogador_um.send(json.dumps({'type': 'questoes', 'dados': questoes, 'player': 'p1'}).encode())
            jogador_dois.send(json.dumps({'type': 'questoes', 'dados': questoes, 'player': 'p2'}).encode())
        except Exception as e:
            print("Erro ao enviar questões:", e)

        scores = {}

        def receber_pontuacao(jogador, key):
            try:
                data = jogador.recv(1024)
                if data:
                    msg = json.loads(data.decode())
                    if msg.get("type") == "pontuacao":
                        scores[key] = msg["pontuacao"]
                else:
                    scores[key] = 0
            except Exception as e:
                print(f"Erro recebendo pontuação de {key}: {e}")
                scores[key] = 0

        t1 = threading.Thread(target=receber_pontuacao, args=(jogador_um, "p1"))
        t2 = threading.Thread(target=receber_pontuacao, args=(jogador_dois, "p2"))
        t1.start()
        t2.start()

        while len(scores) < 2:
            time.sleep(0.5)

        result_msg = json.dumps({"type": "resultado", "pontuacoes": scores})
        for jogador in [jogador_um, jogador_dois]:
            try:
                jogador.send(result_msg.encode())
            except Exception as e:
                print("Erro ao enviar resultado:", e)
            finally:
                jogador.close()

    def iniciar_partida_singleplayer(self, cliente):
        print("Iniciando partida singleplayer.")
        questoes = self.questao_service.obter_questoes_aleatorias()
        questoes = [questao.to_dict() for questao in questoes]

        try:
            cliente.send(json.dumps({'type': 'questoes', 'dados': questoes}).encode())
        except Exception as e:
            print("Erro ao enviar questões:", e)
            cliente.close()
            return

        cliente.close()

if __name__ == '__main__':
    servidor = QuizServer()
    servidor.start()
