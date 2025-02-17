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

## Contribuição
Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades.

## Licença
Este projeto está sob a licença MIT.

