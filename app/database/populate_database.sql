-- Inserir questões
INSERT INTO questoes (pergunta, nivel) VALUES
('Qual é a capital da França?', 'FACIL'),
('Qual é o maior planeta do sistema solar?', 'MEDIO'),
('Quem escreveu "Dom Quixote"?', 'DIFICIL'),
('Qual é a fórmula química da água?', 'FACIL'),
('Em que ano o homem chegou à Lua?', 'MEDIO');

-- Inserir respostas para a primeira questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Paris', 1, TRUE),
('Londres', 1, FALSE),
('Roma', 1, FALSE),
('Madri', 1, FALSE);

-- Inserir respostas para a segunda questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Júpiter', 2, TRUE),
('Saturno', 2, FALSE),
('Terra', 2, FALSE),
('Vênus', 2, FALSE);

-- Inserir respostas para a terceira questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Miguel de Cervantes', 3, TRUE),
('William Shakespeare', 3, FALSE),
('Mark Twain', 3, FALSE),
('Charles Dickens', 3, FALSE);

-- Inserir respostas para a quarta questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('H2O', 4, TRUE),
('CO2', 4, FALSE),
('O2', 4, FALSE),
('CH4', 4, FALSE);

-- Inserir respostas para a quinta questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('1969', 5, TRUE),
('1957', 5, FALSE),
('1972', 5, FALSE),
('1981', 5, FALSE);


-- Inserir questões
INSERT INTO questoes (pergunta, nivel) VALUES
('Qual é o maior oceano do mundo?', 'FACIL'),
('Quem pintou a Mona Lisa?', 'DIFICIL'),
('Qual é o símbolo químico do ouro?', 'FACIL'),
('Quem foi o primeiro presidente dos Estados Unidos?', 'MEDIO'),
('Qual é a capital do Japão?', 'FACIL'),
('Em que ano a Segunda Guerra Mundial terminou?', 'MEDIO'),
('Qual é a fórmula da lei de Newton para a gravitação universal?', 'DIFICIL'),
('Quem inventou o telefone?', 'MEDIO'),
('Em que continente fica o deserto do Saara?', 'FACIL'),
('Qual é o nome da lua de Saturno que tem um oceano subterrâneo?', 'DIFICIL');

-- Inserir respostas para a primeira questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Oceano Pacífico', 6, TRUE),
('Oceano Atlântico', 6, FALSE),
('Oceano Índico', 6, FALSE),
('Oceano Ártico', 6, FALSE);

-- Inserir respostas para a segunda questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Leonardo da Vinci', 7, TRUE),
('Pablo Picasso', 7, FALSE),
('Vincent van Gogh', 7, FALSE),
('Michelangelo', 7, FALSE);

-- Inserir respostas para a terceira questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Au', 8, TRUE),
('Ag', 8, FALSE),
('Pb', 8, FALSE),
('Fe', 8, FALSE);

-- Inserir respostas para a quarta questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('George Washington', 9, TRUE),
('Abraham Lincoln', 9, FALSE),
('Thomas Jefferson', 9, FALSE),
('John Adams', 9, FALSE);

-- Inserir respostas para a quinta questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Tóquio', 10, TRUE),
('Pequim', 10, FALSE),
('Seul', 10, FALSE),
('Bangkok', 10, FALSE);

-- Inserir respostas para a sexta questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('1945', 11, TRUE),
('1939', 11, FALSE),
('1950', 11, FALSE),
('1960', 11, FALSE);

-- Inserir respostas para a sétima questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('F = G * (m1 * m2) / r^2', 12, TRUE),
('F = ma', 12, FALSE),
('E = mc^2', 12, FALSE),
('F = m * g', 12, FALSE);

-- Inserir respostas para a oitava questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Alexander Graham Bell', 13, TRUE),
('Thomas Edison', 13, FALSE),
('Nikola Tesla', 13, FALSE),
('Marie Curie', 13, FALSE);

-- Inserir respostas para a nona questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('África', 14, TRUE),
('Ásia', 14, FALSE),
('América', 14, FALSE),
('Oceania', 14, FALSE);

-- Inserir respostas para a décima questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Encélado', 15, TRUE),
('Titã', 15, FALSE),
('Ío', 15, FALSE),
('Europa', 15, FALSE);


-- Inserir questões
INSERT INTO questoes (pergunta, nivel) VALUES
('Qual é o elemento mais abundante na crosta terrestre?', 'FACIL'),
('Quem descobriu a teoria da relatividade?', 'DIFICIL'),
('Qual é o maior animal terrestre?', 'FACIL'),
('Em que país se encontra a Grande Muralha?', 'MEDIO'),
('Qual é a capital da Austrália?', 'MEDIO'),
('Quem foi o autor de "Harry Potter"?', 'FACIL'),
('Qual é a capital da Itália?', 'FACIL'),
('Em que continente está o Egito?', 'MEDIO'),
('Qual é o maior deserto do mundo?', 'DIFICIL'),
('Qual é o maior rio do mundo?', 'MEDIO');

-- Inserir respostas para a primeira questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Oxigênio', 16, FALSE),
('Silício', 16, TRUE),
('Carbono', 16, FALSE),
('Nitrogênio', 16, FALSE);

-- Inserir respostas para a segunda questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Albert Einstein', 17, TRUE),
('Isaac Newton', 17, FALSE),
('Niels Bohr', 17, FALSE),
('Galileu Galilei', 17, FALSE);

-- Inserir respostas para a terceira questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Elefante africano', 18, TRUE),
('Girafa', 18, FALSE),
('Rinoceronte', 18, FALSE),
('Hipopótamo', 18, FALSE);

-- Inserir respostas para a quarta questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('China', 19, TRUE),
('Índia', 19, FALSE),
('Japão', 19, FALSE),
('Rússia', 19, FALSE);

-- Inserir respostas para a quinta questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Canberra', 20, TRUE),
('Sydney', 20, FALSE),
('Melbourne', 20, FALSE),
('Brisbane', 20, FALSE);

-- Inserir respostas para a sexta questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('J.K. Rowling', 21, TRUE),
('J.R.R. Tolkien', 21, FALSE),
('George R.R. Martin', 21, FALSE),
('C.S. Lewis', 21, FALSE);

-- Inserir respostas para a sétima questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Roma', 22, TRUE),
('Milão', 22, FALSE),
('Veneza', 22, FALSE),
('Florença', 22, FALSE);

-- Inserir respostas para a oitava questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('África', 23, TRUE),
('Ásia', 23, FALSE),
('Europa', 23, FALSE),
('América', 23, FALSE);

-- Inserir respostas para a nona questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Deserto da Antártida', 24, TRUE),
('Deserto do Saara', 24, FALSE),
('Deserto de Atacama', 24, FALSE),
('Deserto de Gobi', 24, FALSE);

-- Inserir respostas para a décima questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Amazonas', 25, TRUE),
('Nilo', 25, FALSE),
('Yangtze', 25, FALSE),
('Mississippi', 25, FALSE);


-- Inserir questões
INSERT INTO questoes (pergunta, nivel) VALUES
('Qual é o planeta mais próximo do Sol?', 'FACIL'),
('Quem foi o primeiro homem a ir ao espaço?', 'DIFICIL'),
('Quantos estados tem o Brasil?', 'FACIL'),
('Qual é o maior continente?', 'FACIL'),
('Quem foi o autor de "1984"?', 'DIFICIL'),
('Qual é o maior lago de água doce do mundo?', 'MEDIO'),
('Em que país está localizada a cidade de Machu Picchu?', 'MEDIO'),
('Qual é o nome do processo de conversão de alimentos em energia pelo corpo?', 'FACIL'),
('Qual é a moeda oficial do Japão?', 'FACIL'),
('Qual é o maior estádio de futebol do mundo?', 'DIFICIL');

-- Inserir respostas para a primeira questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Mercúrio', 26, TRUE),
('Vênus', 26, FALSE),
('Terra', 26, FALSE),
('Marte', 26, FALSE);

-- Inserir respostas para a segunda questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Yuri Gagarin', 27, TRUE),
('Neil Armstrong', 27, FALSE),
('Buzz Aldrin', 27, FALSE),
('John Glenn', 27, FALSE);

-- Inserir respostas para a terceira questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('26', 28, FALSE),
('25', 28, FALSE),
('27', 28, FALSE),
('28', 28, TRUE);

-- Inserir respostas para a quarta questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('África', 29, FALSE),
('América', 29, FALSE),
('Ásia', 29, TRUE),
('Europa', 29, FALSE);

-- Inserir respostas para a quinta questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('George Orwell', 30, TRUE),
('Aldous Huxley', 30, FALSE),
('Ray Bradbury', 30, FALSE),
('Margaret Atwood', 30, FALSE);

-- Inserir respostas para a sexta questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Lago Superior', 31, TRUE),
('Lago Baikal', 31, FALSE),
('Lago Michigan', 31, FALSE),
('Lago Titicaca', 31, FALSE);

-- Inserir respostas para a sétima questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Peru', 32, TRUE),
('Chile', 32, FALSE),
('Brasil', 32, FALSE),
('Equador', 32, FALSE);

-- Inserir respostas para a oitava questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Digestão', 33, TRUE),
('Respiração', 33, FALSE),
('Circulação', 33, FALSE),
('Excreção', 33, FALSE);

-- Inserir respostas para a nona questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Iene', 34, TRUE),
('Dólar', 34, FALSE),
('Euro', 34, FALSE),
('Yuan', 34, FALSE);

-- Inserir respostas para a décima questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Rungrado 1 de Maio', 35, TRUE),
('Maracanã', 35, FALSE),
('Camp Nou', 35, FALSE),
('Wembley', 35, FALSE);


-- Inserir questões
INSERT INTO questoes (pergunta, nivel) VALUES
('Qual é o menor continente?', 'FACIL'),
('Em que ano o Titanic afundou?', 'MEDIO'),
('Quem foi o primeiro ser vivo a viajar ao espaço?', 'DIFICIL'),
('Qual é o maior animal marinho?', 'FACIL'),
('Quem foi o líder da Revolução Francesa?', 'DIFICIL'),
('Qual é o maior vulcão do mundo?', 'MEDIO'),
('Em que país foi construído o primeiro computador?', 'DIFICIL'),
('Qual é a capital da Alemanha?', 'FACIL'),
('Quem foi o primeiro imperador romano?', 'DIFICIL'),
('Qual é o número de planetas no sistema solar?', 'FACIL'),

('Em que ano a Primeira Guerra Mundial começou?', 'MEDIO'),
('Quem foi o cientista responsável pela lei da gravitação universal?', 'DIFICIL'),
('Qual é o nome da teoria que propõe que a Terra gira em torno do Sol?', 'MEDIO'),
('Em que ano foi fundado o Facebook?', 'FACIL'),
('Quantos jogadores há em um time de futebol?', 'FACIL'),
('Qual é o nome do famoso monumento em Paris?', 'FACIL'),
('Qual é a unidade básica da vida?', 'MEDIO'),
('Em que país fica a cidade de Petra?', 'DIFICIL'),
('Qual é o maior país do mundo em termos de área?', 'FACIL'),
('Quem escreveu "O Senhor dos Anéis"?', 'DIFICIL'),

('Qual é o número atômico do oxigênio?', 'FACIL'),
('Quem foi o presidente dos Estados Unidos durante a Segunda Guerra Mundial?', 'MEDIO'),
('Quem pintou a Capela Sistina?', 'DIFICIL'),
('Em que ano ocorreu o primeiro pouso na Lua?', 'FACIL'),
('Qual é o maior país da América do Sul?', 'FACIL'),
('Qual é o maior sistema de rios do mundo?', 'MEDIO'),
('Quantos continentes existem no mundo?', 'FACIL'),
('Qual é o maior rio da África?', 'MEDIO'),
('Em que país se encontra a Torre de Pisa?', 'FACIL'),
('Qual é o nome da teoria que sugere que os dinossauros foram extintos por um meteoro?', 'DIFICIL'),

-- Inserir respostas para as questões
-- Primeira questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Oceania', 36, TRUE),
('África', 36, FALSE),
('Ásia', 36, FALSE),
('Antártida', 36, FALSE);

-- Segunda questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('1912', 37, FALSE),
('1910', 37, FALSE),
('1915', 37, FALSE),
('1912', 37, TRUE);

-- Terceira questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Laika', 38, TRUE),
('Yuri Gagarin', 38, FALSE),
('Neil Armstrong', 38, FALSE),
('Belka', 38, FALSE);

-- Quarta questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Baleia azul', 39, TRUE),
('Golfinho', 39, FALSE),
('Tubarão branco', 39, FALSE),
('Orca', 39, FALSE);

-- Quinta questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Napoleão Bonaparte', 40, TRUE),
('Jean-Paul Marat', 40, FALSE),
('Maximilien Robespierre', 40, FALSE),
('Ludwig van Beethoven', 40, FALSE);

-- Sexta questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Mauna Loa', 41, TRUE),
('Etna', 41, FALSE),
('Kilauea', 41, FALSE),
('Vesuvius', 41, FALSE);

-- Sétima questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Alemanha', 42, TRUE),
('França', 42, FALSE),
('EUA', 42, FALSE),
('Reino Unido', 42, FALSE);

-- Oitava questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Roma', 43, TRUE),
('Milão', 43, FALSE),
('Napoli', 43, FALSE),
('Florença', 43, FALSE);

-- Nona questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Augusto', 44, TRUE),
('Júlio César', 44, FALSE),
('Nero', 44, FALSE),
('Trajano', 44, FALSE);

-- Décima questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('8', 45, TRUE),
('9', 45, FALSE),
('7', 45, FALSE),
('10', 45, FALSE);

-- 11ª questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('1914', 46, TRUE),
('1915', 46, FALSE),
('1912', 46, FALSE),
('1913', 46, FALSE);

-- 12ª questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Isaac Newton', 47, TRUE),
('Galileu Galilei', 47, FALSE),
('Nikola Tesla', 47, FALSE),
('Albert Einstein', 47, FALSE);

-- 13ª questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Heliocentrismo', 48, TRUE),
('Geocentrismo', 48, FALSE),
('Evolução', 48, FALSE),
('Teoria do Big Bang', 48, FALSE);

-- 14ª questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('2004', 49, TRUE),
('2002', 49, FALSE),
('2000', 49, FALSE),
('2006', 49, FALSE);

-- 15ª questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('11', 50, TRUE),
('12', 50, FALSE),
('9', 50, FALSE),
('10', 50, FALSE);

-- 16ª questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Eiffel', 51, TRUE),
('Leaning', 51, FALSE),
('Pisa', 51, FALSE),
('Louvre', 51, FALSE);

-- 17ª questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Célula', 52, TRUE),
('Organelo', 52, FALSE),
('Átomo', 52, FALSE),
('Molécula', 52, FALSE);

-- 18ª questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Jordânia', 53, TRUE),
('Peru', 53, FALSE),
('México', 53, FALSE),
('Brasil', 53, FALSE);

-- 19ª questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Rússia', 54, TRUE),
('Canadá', 54, FALSE),
('China', 54, FALSE),
('EUA', 54, FALSE);

-- 20ª questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('J.R.R. Tolkien', 55, TRUE),
('George Orwell', 55, FALSE),
('H.G. Wells', 55, FALSE),
('C.S. Lewis', 55, FALSE);

-- 21ª questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('8', 56, TRUE),
('6', 56, FALSE),
('10', 56, FALSE),
('7', 56, FALSE);

-- 22ª questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Oxygen', 57, TRUE),
('O3', 57, FALSE),
('Carbon', 57, FALSE),
('Hydrogen', 57, FALSE);

-- 23ª questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Franklin D. Roosevelt', 58, TRUE),
('Abraham Lincoln', 58, FALSE),
('Theodore Roosevelt', 58, FALSE),
('Woodrow Wilson', 58, FALSE);

-- 24ª questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('Michelangelo', 59, TRUE),
('Leonardo Da Vinci', 59, FALSE),
('Pablo Picasso', 59, FALSE),
('Vincent Van Gogh', 59, FALSE);

-- 25ª questão
INSERT INTO respostas (texto, questao_id, correta) VALUES
('1969', 60, TRUE),
('1961', 60, FALSE),
('1975', 60, FALSE),
('1965', 60, FALSE);

