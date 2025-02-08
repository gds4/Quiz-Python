INSERT INTO questoes (id, pergunta, nivel) VALUES
(1,'Qual é a capital da França?', 'FACIL'),
(2,'Qual é o maior planeta do sistema solar?', 'MEDIO'),
(3,'Quem escreveu "Dom Quixote"?', 'DIFICIL'),
(4,'Qual é a fórmula química da água?', 'FACIL'),
(5,'Em que ano o homem chegou à Lua?', 'MEDIO'),
(6,'Qual é o maior oceano do mundo?', 'FACIL'),
(7,'Quem pintou a Mona Lisa?', 'DIFICIL'),
(8,'Qual é o símbolo químico do ouro?', 'FACIL'),
(9,'Quem foi o primeiro presidente dos Estados Unidos?', 'MEDIO'),
(10,'Qual é a capital do Japão?', 'FACIL'),
(11,'Em que ano a Segunda Guerra Mundial terminou?', 'MEDIO'),
(12,'Qual é a fórmula da lei de Newton para a gravitação universal?', 'DIFICIL'),
(13,'Quem inventou o telefone?', 'MEDIO'),
(14,'Em que continente fica o deserto do Saara?', 'FACIL'),
(15,'Qual é o nome da lua de Saturno que tem um oceano subterrâneo?', 'DIFICIL'),
(16,'Qual é o elemento mais abundante na crosta terrestre?', 'FACIL'),
(17,'Quem descobriu a teoria da relatividade?', 'DIFICIL'),
(18,'Qual é o maior animal terrestre?', 'FACIL'),
(19,'Em que país se encontra a Grande Muralha?', 'MEDIO'),
(20,'Qual é a capital da Austrália?', 'MEDIO'),
(21,'Quem foi o autor de "Harry Potter"?', 'FACIL'),
(22,'Qual é a capital da Itália?', 'FACIL'),
(23,'Em que continente está o Egito?', 'MEDIO'),
(24,'Qual é o maior deserto do mundo?', 'DIFICIL'),
(25,'Qual é o maior rio do mundo?', 'MEDIO'),
(26,'Qual é o planeta mais próximo do Sol?', 'FACIL'),
(27,'Quem foi o primeiro homem a ir ao espaço?', 'DIFICIL'),
(28,'Quantos estados tem o Brasil?', 'FACIL'),
(29,'Qual é o maior continente?', 'FACIL'),
(30,'Quem foi o autor de "1984"?', 'DIFICIL'),
(31,'Qual é o maior lago de água doce do mundo?', 'MEDIO'),
(32,'Em que país está localizada a cidade de Machu Picchu?', 'MEDIO'),
(33,'Qual é o nome do processo de conversão de alimentos em energia pelo corpo?', 'FACIL'),
(34,'Qual é a moeda oficial do Japão?', 'FACIL'),
(35,'Qual é o maior estádio de futebol do mundo?', 'DIFICIL'),
(36,'Qual é o menor continente?', 'FACIL'),
(37,'Em que ano o Titanic afundou?', 'MEDIO'),
(38,'Quem foi o primeiro ser vivo a viajar ao espaço?', 'DIFICIL'),
(39,'Qual é o maior animal marinho?', 'FACIL'),
(40,'Quem foi o líder da Revolução Francesa?', 'DIFICIL'),
(41,'Qual é o maior vulcão do mundo?', 'MEDIO'),
(42,'Em que país foi construído o primeiro computador?', 'DIFICIL'),
(43,'Qual é a capital da Alemanha?', 'FACIL'),
(44,'Quem foi o primeiro imperador romano?', 'DIFICIL'),
(45,'Qual é o número de planetas no sistema solar?', 'FACIL'),
(46,'Em que ano a Primeira Guerra Mundial começou?', 'MEDIO'),
(47,'Quem foi o cientista responsável pela lei da gravitação universal?', 'DIFICIL'),
(48,'Qual é o nome da teoria que propõe que a Terra gira em torno do Sol?', 'MEDIO'),
(49,'Em que ano foi fundado o Facebook?', 'FACIL'),
(50,'Quantos jogadores há em um time de futebol?', 'FACIL'),
(51,'Qual é o nome do famoso monumento em Paris?', 'FACIL'),
(52,'Qual é a unidade básica da vida?', 'MEDIO'),
(53,'Em que país fica a cidade de Petra?', 'DIFICIL'),
(54,'Qual é o maior país do mundo em termos de área?', 'FACIL'),
(55,'Quem escreveu "O Senhor dos Anéis"?', 'DIFICIL'),
(56,'Qual é o número atômico do oxigênio?', 'FACIL'),
(57,'Quem foi o presidente dos Estados Unidos durante a Segunda Guerra Mundial?', 'MEDIO'),
(58,'Quem pintou a Capela Sistina?', 'DIFICIL'),
(59,'Em que ano ocorreu o primeiro pouso na Lua?', 'FACIL'),
(60,'Qual é o maior país da América do Sul?', 'FACIL'),
(61,'Qual é o maior sistema de rios do mundo?', 'MEDIO'),
(62,'Quantos continentes existem no mundo?', 'FACIL'),
(63,'Qual é o maior rio da África?', 'MEDIO'),
(64,'Em que país se encontra a Torre de Pisa?', 'FACIL'),
(65,'Qual é o nome da teoria que sugere que os dinossauros foram extintos por um meteoro?', 'DIFICIL');

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Paris', 1, TRUE),
('Londres', 1, FALSE),
('Roma', 1, FALSE),
('Madri', 1, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Júpiter', 2, TRUE),
('Saturno', 2, FALSE),
('Terra', 2, FALSE),
('Vênus', 2, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Miguel de Cervantes', 3, TRUE),
('William Shakespeare', 3, FALSE),
('Mark Twain', 3, FALSE),
('Charles Dickens', 3, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('H2O', 4, TRUE),
('CO2', 4, FALSE),
('O2', 4, FALSE),
('CH4', 4, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('1969', 5, TRUE),
('1957', 5, FALSE),
('1972', 5, FALSE),
('1981', 5, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Oceano Pacífico', 6, TRUE),
('Oceano Atlântico', 6, FALSE),
('Oceano Índico', 6, FALSE),
('Oceano Ártico', 6, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Leonardo da Vinci', 7, TRUE),
('Pablo Picasso', 7, FALSE),
('Vincent van Gogh', 7, FALSE),
('Michelangelo', 7, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Au', 8, TRUE),
('Ag', 8, FALSE),
('Pb', 8, FALSE),
('Fe', 8, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('George Washington', 9, TRUE),
('Abraham Lincoln', 9, FALSE),
('Thomas Jefferson', 9, FALSE),
('John Adams', 9, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Tóquio', 10, TRUE),
('Pequim', 10, FALSE),
('Seul', 10, FALSE),
('Bangkok', 10, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('1945', 11, TRUE),
('1939', 11, FALSE),
('1950', 11, FALSE),
('1960', 11, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('F = G * (m1 * m2) / r^2', 12, TRUE),
('F = ma', 12, FALSE),
('E = mc^2', 12, FALSE),
('F = m * g', 12, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Alexander Graham Bell', 13, TRUE),
('Thomas Edison', 13, FALSE),
('Nikola Tesla', 13, FALSE),
('Marie Curie', 13, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('África', 14, TRUE),
('Ásia', 14, FALSE),
('América', 14, FALSE),
('Oceania', 14, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Encélado', 15, TRUE),
('Titã', 15, FALSE),
('Ío', 15, FALSE),
('Europa', 15, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Oxigênio', 16, FALSE),
('Silício', 16, TRUE),
('Carbono', 16, FALSE),
('Nitrogênio', 16, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Albert Einstein', 17, TRUE),
('Isaac Newton', 17, FALSE),
('Niels Bohr', 17, FALSE),
('Galileu Galilei', 17, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Elefante africano', 18, TRUE),
('Girafa', 18, FALSE),
('Rinoceronte', 18, FALSE),
('Hipopótamo', 18, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('China', 19, TRUE),
('Índia', 19, FALSE),
('Japão', 19, FALSE),
('Rússia', 19, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Canberra', 20, TRUE),
('Sydney', 20, FALSE),
('Melbourne', 20, FALSE),
('Brisbane', 20, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('J.K. Rowling', 21, TRUE),
('J.R.R. Tolkien', 21, FALSE),
('George R.R. Martin', 21, FALSE),
('C.S. Lewis', 21, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Roma', 22, TRUE),
('Milão', 22, FALSE),
('Veneza', 22, FALSE),
('Florença', 22, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('África', 23, TRUE),
('Ásia', 23, FALSE),
('Europa', 23, FALSE),
('América', 23, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Deserto da Antártida', 24, TRUE),
('Deserto do Saara', 24, FALSE),
('Deserto de Atacama', 24, FALSE),
('Deserto de Gobi', 24, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Amazonas', 25, TRUE),
('Nilo', 25, FALSE),
('Yangtze', 25, FALSE),
('Mississippi', 25, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Mercúrio', 26, TRUE),
('Vênus', 26, FALSE),
('Terra', 26, FALSE),
('Marte', 26, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Yuri Gagarin', 27, TRUE),
('Neil Armstrong', 27, FALSE),
('Buzz Aldrin', 27, FALSE),
('John Glenn', 27, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('26', 28, FALSE),
('25', 28, FALSE),
('27', 28, FALSE),
('28', 28, TRUE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('África', 29, FALSE),
('América', 29, FALSE),
('Ásia', 29, TRUE),
('Europa', 29, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('George Orwell', 30, TRUE),
('Aldous Huxley', 30, FALSE),
('Ray Bradbury', 30, FALSE),
('Margaret Atwood', 30, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Lago Superior', 31, TRUE),
('Lago Baikal', 31, FALSE),
('Lago Michigan', 31, FALSE),
('Lago Titicaca', 31, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Peru', 32, TRUE),
('Chile', 32, FALSE),
('Brasil', 32, FALSE),
('Equador', 32, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Digestão', 33, TRUE),
('Respiração', 33, FALSE),
('Circulação', 33, FALSE),
('Excreção', 33, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Iene', 34, TRUE),
('Dólar', 34, FALSE),
('Euro', 34, FALSE),
('Yuan', 34, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Rungrado 1 de Maio', 35, TRUE),
('Maracanã', 35, FALSE),
('Camp Nou', 35, FALSE),
('Wembley', 35, FALSE);


INSERT INTO respostas (texto, questao_id, correta) VALUES
('Oceania', 36, TRUE),
('África', 36, FALSE),
('Ásia', 36, FALSE),
('Antártida', 36, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('1912', 37, FALSE),
('1910', 37, FALSE),
('1915', 37, FALSE),
('1912', 37, TRUE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Laika', 38, TRUE),
('Yuri Gagarin', 38, FALSE),
('Neil Armstrong', 38, FALSE),
('Belka', 38, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Baleia azul', 39, TRUE),
('Golfinho', 39, FALSE),
('Tubarão branco', 39, FALSE),
('Orca', 39, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Napoleão Bonaparte', 40, TRUE),
('Jean-Paul Marat', 40, FALSE),
('Maximilien Robespierre', 40, FALSE),
('Ludwig van Beethoven', 40, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Mauna Loa', 41, TRUE),
('Etna', 41, FALSE),
('Kilauea', 41, FALSE),
('Vesuvius', 41, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Alemanha', 42, TRUE),
('França', 42, FALSE),
('EUA', 42, FALSE),
('Reino Unido', 42, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Roma', 43, TRUE),
('Milão', 43, FALSE),
('Napoli', 43, FALSE),
('Florença', 43, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Augusto', 44, TRUE),
('Júlio César', 44, FALSE),
('Nero', 44, FALSE),
('Trajano', 44, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('8', 45, TRUE),
('9', 45, FALSE),
('7', 45, FALSE),
('10', 45, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('1914', 46, TRUE),
('1915', 46, FALSE),
('1912', 46, FALSE),
('1913', 46, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Isaac Newton', 47, TRUE),
('Galileu Galilei', 47, FALSE),
('Nikola Tesla', 47, FALSE),
('Albert Einstein', 47, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Heliocentrismo', 48, TRUE),
('Geocentrismo', 48, FALSE),
('Evolução', 48, FALSE),
('Teoria do Big Bang', 48, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('2004', 49, TRUE),
('2002', 49, FALSE),
('2000', 49, FALSE),
('2006', 49, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('11', 50, TRUE),
('12', 50, FALSE),
('9', 50, FALSE),
('10', 50, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Eiffel', 51, TRUE),
('Leaning', 51, FALSE),
('Pisa', 51, FALSE),
('Louvre', 51, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Célula', 52, TRUE),
('Organelo', 52, FALSE),
('Átomo', 52, FALSE),
('Molécula', 52, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Jordânia', 53, TRUE),
('Peru', 53, FALSE),
('México', 53, FALSE),
('Brasil', 53, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Rússia', 54, TRUE),
('Canadá', 54, FALSE),
('China', 54, FALSE),
('EUA', 54, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('J.R.R. Tolkien', 55, TRUE),
('George Orwell', 55, FALSE),
('H.G. Wells', 55, FALSE),
('C.S. Lewis', 55, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('8', 56, TRUE),
('6', 56, FALSE),
('10', 56, FALSE),
('7', 56, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Franklin D. Roosevelt', 57, TRUE),
('Abraham Lincoln', 57, FALSE),
('Theodore Roosevelt', 57, FALSE),
('Woodrow Wilson', 57, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Michelangelo', 58, TRUE),
('Leonardo Da Vinci', 58, FALSE),
('Pablo Picasso', 58, FALSE),
('Vincent Van Gogh', 58, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('1969', 59, TRUE),
('1961', 59, FALSE),
('1975', 59, FALSE),
('1965', 59, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Brasil', 60, TRUE),
('Argentina', 60, FALSE),
('Colômbia', 60, FALSE),
('Chile', 60, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Amazonas', 61, TRUE),
('Nilo', 61, FALSE),
('Yangtze', 61, FALSE),
('Mississippi', 61, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('7', 62, TRUE),
('6', 62, FALSE),
('8', 62, FALSE),
('5', 62, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Nilo', 63, TRUE),
('Congo', 63, FALSE),
('Zambeze', 63, FALSE),
('Limpopo', 63, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Itália', 64, TRUE),
('França', 64, FALSE),
('Espanha', 64, FALSE),
('Portugal', 64, FALSE);

INSERT INTO respostas (texto, questao_id, correta) VALUES
('Teoria do impacto', 65, TRUE),
('Teoria do vulcanismo', 65, FALSE),
('Teoria da evolução', 65, FALSE),
('Teoria da mudança climática', 65, FALSE);
