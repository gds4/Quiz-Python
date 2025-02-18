# Quiz Game em Python com Pygame

## Descrição
Este projeto é um jogo de Quiz desenvolvido em Python utilizando a biblioteca Pygame para a disciplina de Tópicos Avançados II. O jogo segue uma estrutura cliente-servidor baseada em comunicação via sockets e possui dois modos de jogo: **Singleplayer** e **Multiplayer**.

## Funcionalidades
- **Modo Singleplayer**: O jogador se conecta ao servidor, solicita as perguntas e joga uma partida com 10 perguntas, tendo 15 segundos para responder cada uma.
- **Modo Multiplayer**: O jogador se conecta ao servidor informando o tipo de jogo. O servidor coloca o jogador em uma fila e aguarda a conexão de outro jogador. Quando um oponente se conecta, o servidor inicia uma thread para a partida. Ambos os jogadores recebem as mesmas 10 perguntas e jogam simultaneamente. No final, os jogadores enviam suas pontuações ao servidor, que retorna a pontuação do adversário.
- **Banco de Dados**: O servidor utiliza SQLite3 para armazenar dados, com interação via SQLAlchemy.

## Tecnologias Utilizadas
- **Python**
- **Pygame**
- **Sockets**
- **SQLAlchemy**
- **SQLite3**

## Como Executar
### Servidor:
1. Instale as dependências necessárias:
   ```sh
   pip install pygame sqlalchemy
   ```
2. Execute o servidor:
   ```sh
   python /server/server.py 
   ```

### Cliente:
1. Execute o cliente:
   ```sh
   python ./app/main.py      
   ```
2. Escolha entre **Singleplayer** ou **Multiplayer** e divirta-se!

# Lógica do Modo Multiplayer

## Comunicação Cliente-Servidor

O servidor e os clientes se comunicam via sockets, com o cliente enviando mensagens em formato JSON para o servidor. A estrutura de comunicação segue os seguintes fluxos:

### Fluxo de Conexão Inicial
O cliente se conecta ao servidor e envia uma mensagem inicial indicando o tipo de jogo (singleplayer ou multiplayer).

**Exemplo de JSON enviado pelo cliente para o servidor:**

```json
{
  "type": "multiplayer"
}
```

O servidor recebe a solicitação de multiplayer, coloca o jogador na fila de espera e aguarda outro jogador se conectar.


### Fluxo de Envio das Questões
Após a conexão de dois jogadores, o servidoros retira da fila e envia um conjunto de 10 perguntas aleatórias para ambos, indicando o jogador como "p1" ou "p2".

**Exemplo de JSON enviado pelo servidor para os jogadores:**
 ```json
 {
   "type": "questoes",
   "dados": [
     {
       "pergunta": "Qual a capital da França?",
       "respostas": [
         {"texto": "Paris", "correto": true},
         {"texto": "Londres", "correto": false},
         {"texto": "Berlim", "correto": false},
         {"texto": "Madrid", "correto": false}
       ]
     },
     {
       "pergunta": "Qual é o maior planeta do sistema solar?",
       "respostas": [
         {"texto": "Júpiter", "correto": true},
         {"texto": "Terra", "correto": false},
         {"texto": "Saturno", "correto": false},
         {"texto": "Marte", "correto": false}
       ]
     }
   ],
   "player": "p1"
 }
 ```

### Fluxo de Respostas e Pontuação
Os jogadores selecionam suas respostas dentro de 15 segundos. A pontuação é calculada com base no tempo restante (quanto mais rápido o jogador responder, mais pontos ele ganha).

**Exemplo de JSON enviado pelo cliente após responder todas as perguntas:**
 ```json
 {
   "type": "pontuacao",
   "pontuacao": 530
 }
 ```
### Fluxo de Finalização de Partida
   -Depois que ambos os jogadores completam as 10 perguntas, o servidor coleta as pontuações de cada um e envia o resultado para os jogadores.

**Exemplo de JSON enviado pelo servidor com o resultado final:**

 ```json
 {
   "type": "resultado",
   "pontuacoes": {
     "p1": 650,
     "p2": 700
   }
 }
 ```
## Lógica das Threads no Jogo Multiplayer

### 1. **Recepção da Solicitação e Monitoramento da Conexão**
   - Ao receber uma solicitação de jogo multiplayer, o servidor adiciona o cliente a uma fila de jogadores.
   - Simultaneamente, é iniciada uma thread dedicada para monitorar a conexão desse jogador (através da função `monitor_cliente`), usando o módulo `select` para identificar possíveis desconexões ou falhas de comunicação.

### 2. **Emparelhamento e Início da Partida**
   - Quando há pelo menos dois jogadores na fila, o servidor os remove e inicia uma nova thread para conduzir a partida multiplayer (chamada de `iniciar_partida_multiplayer`).
   - Nesta thread, é criado um ID único para a partida, associando os dois jogadores que serão identificados como `"p1"` e `"p2"`.

### 3. **Envio das Questões**
   - Dentro da thread da partida, o servidor obtém questões aleatórias e as converte para o formato adequado.
   - Em seguida, as questões são enviadas para ambos os jogadores, informando explicitamente qual jogador é `"p1"` e qual é `"p2"`.

### 4. **Recebimento Paralelo das Respostas**
   - Para que o servidor não fique bloqueado enquanto aguarda as respostas, ele cria duas threads separadas (uma para cada jogador) que executam a função `receber_pontuacao`.
   - Cada thread fica responsável por aguardar a mensagem de pontuação enviada pelo respectivo jogador, atualizando um dicionário compartilhado com os resultados.

### 5. **Sincronização e Aguardar a Finalização da Partida**
   - O servidor entra em um loop de espera que verifica periodicamente se as pontuações de ambos os jogadores foram recebidas.
   - Esse método de sincronização garante que o servidor continue operando normalmente, mesmo que um dos jogadores demore mais para responder.

### 6. **Envio do Resultado Final e Encerramento da Conexão**
   - Assim que as duas pontuações são recebidas, o servidor compila um resultado final com as pontuações de `"p1"` e `"p2"` e o envia para ambos os jogadores.
   - Por fim, as conexões com os jogadores são encerradas, finalizando a partida.


# Lógica do Modo Singleplayer

   - O cliente inicia a conexão com o servidor, enviando um JSON indicando que deseja jogar no modo singleplayer.
```json
{
    "type": "singleplayer"
}
```

### Fluxo de Envio das Questões
  - O servidor responde com um JSON contendo as perguntas para o jogo:
```json
 {
     "type": "questoes",
     "dados": [
         {
             "pergunta": "Qual é a capital da França?",
             "respostas": [
                 {"texto": "Paris", "correta": true},
                 {"texto": "Londres", "correta": false},
                 {"texto": "Berlim", "correta": false},
                 {"texto": "Madrid", "correta": false}
             ]
         },
         {
             "pergunta": "Quanto é 2 + 2?",
             "respostas": [
                 {"texto": "3", "correta": false},
                 {"texto": "4", "correta": true},
                 {"texto": "5", "correta": false},
                 {"texto": "6", "correta": false}
             ]
         }
     ]
 }
 ```
### Encerramento da Conexão

   - Após enviar os dados ao cliente, o servidor encerra a conexão, pois o jogo singleplayer é processado exclusivamente no lado do cliente após o recebimento das perguntas.

## Lógica das Threads no Jogo Singleplayer

### 1. **Recepção da Solicitação e Início da Partida**
   - Quando o servidor recebe uma solicitação de um jogador para iniciar um jogo no modo singleplayer, ele cria uma thread dedicada para essa partida (chamando a função `iniciar_partida_singleplayer`).

### 1.1. **Envio das Questões**
   - Dentro da thread, o servidor obtém um conjunto de questões aleatórias a partir do serviço de banco de dados (`questao_service`).
   - Essas questões são formatadas em um dicionario e enviadas para o jogador através do socket.

### 2. **Encerramento da Conexão**
   - Como o modo singleplayer não requer sincronização com outro jogador, o servidor fecha a conexão imediatamente após o envio das questões.

## Contribuição

Este projeto foi desenvolvido por gds4 e dieglop