-- Tabela osób (persons)
CREATE TABLE IF NOT EXISTS persons (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  surname VARCHAR(255) NOT NULL,
  birth_year INT,
  death_year INT
);


-- Tabela języków (languages)
CREATE TABLE IF NOT EXISTS languages (
  id INT PRIMARY KEY AUTO_INCREMENT,
  lang VARCHAR(255) UNIQUE NOT NULL
);

-- Tabela wydawców (publishers)
CREATE TABLE IF NOT EXISTS publishers (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  localization VARCHAR(255) NOT NULL,
  foundation_year INT NOT NULL
);


-- Tabela kategorii (categories)
CREATE TABLE IF NOT EXISTS categories (
  id INT PRIMARY KEY AUTO_INCREMENT,
  category VARCHAR(255) UNIQUE NOT NULL
);


-- Tabela informacji o użytkownikach (user_infos)
CREATE TABLE IF NOT EXISTS user_infos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  surname VARCHAR(255) NOT NULL,
  phone VARCHAR(20),
  card_num VARCHAR(20) NOT NULL
);

-- Tabela form książek (forms)
CREATE TABLE IF NOT EXISTS forms (
  id INT PRIMARY KEY AUTO_INCREMENT,
  form VARCHAR(255) UNIQUE NOT NULL
);

ALTER TABLE forms AUTO_INCREMENT = 1;

-- Tabela książek (books)
CREATE TABLE IF NOT EXISTS books (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  lang_id INT NOT NULL,
  series VARCHAR(255),
  author_id INT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES persons(id),
  FOREIGN KEY (lang_id) REFERENCES languages(id)
);


-- Tabela informacji o edycjach (edition_infos)
CREATE TABLE IF NOT EXISTS edition_infos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  book_id INT NOT NULL,
  ed_title VARCHAR(255),
  ed_series VARCHAR(255),
  illustrator_id INT,
  translator_id INT,
  ed_lang_id INT,
  publisher_id INT NOT NULL,
  ed_num INT NOT NULL,
  ed_year INT NOT NULL,
  form_id INT NOT NULL,
  isbn BIGINT NOT NULL,
  ukd VARCHAR(255) NOT NULL,
  FOREIGN KEY (book_id) REFERENCES books(id),
  FOREIGN KEY (illustrator_id) REFERENCES persons(id),
  FOREIGN KEY (translator_id) REFERENCES persons(id),
  FOREIGN KEY (ed_lang_id) REFERENCES languages(id),
  FOREIGN KEY (publisher_id) REFERENCES publishers(id),
  FOREIGN KEY (form_id) REFERENCES forms(id)
);

-- Tabela kopii książek (copies)
CREATE TABLE IF NOT EXISTS copies (
  id INT PRIMARY KEY AUTO_INCREMENT,
  ed_id INT NOT NULL,
  rented BOOLEAN NOT NULL,
  FOREIGN KEY (ed_id) REFERENCES edition_infos(id)
);


-- Tabela pośrednia książki do kategorii (book_categories)
CREATE TABLE IF NOT EXISTS book_categories (
  book_id INT NOT NULL,
  cat_id INT NOT NULL,
  PRIMARY KEY (book_id, cat_id),
  FOREIGN KEY (book_id) REFERENCES books(id),
  FOREIGN KEY (cat_id) REFERENCES categories(id)
);


-- Tabela użytkowników (users)
CREATE TABLE IF NOT EXISTS users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  user_infos_id INT NOT NULL,
  role ENUM('User', 'Worker', 'Admin') NOT NULL DEFAULT 'User',
  created_at DATETIME NOT NULL,
  FOREIGN KEY (user_infos_id) REFERENCES user_infos(id)
);

-- Tabela wypożyczeń (rentals)
CREATE TABLE IF NOT EXISTS rentals (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  copy_id INT NOT NULL,
  rental_date DATE NOT NULL,
  due_date DATE NOT NULL,
  return_date DATE,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (copy_id) REFERENCES copies(id)
);

-- Tabela adnotacji (annotations)
CREATE TABLE IF NOT EXISTS annotations (
  id INT PRIMARY KEY AUTO_INCREMENT,
  book_id INT,
  ed_id INT,
  copy_id INT,
  content TEXT NOT NULL,
  FOREIGN KEY (book_id) REFERENCES books(id),
  FOREIGN KEY (ed_id) REFERENCES edition_infos(id),
  FOREIGN KEY (copy_id) REFERENCES copies(id)
);


-- Tabela rezerwacji (reservations)
CREATE TABLE IF NOT EXISTS reservations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    copy_id INT NOT NULL,
    reserved_at DATETIME NOT NULL,
    reserved_due DATETIME,
    status ENUM('Reserved', 'Awaiting', 'Cancelled', 'PastDue', 'Succeeded') NOT NULL DEFAULT 'Reserved',
    FOREIGN KEY (copy_id) REFERENCES copies(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);



CREATE PROCEDURE IF NOT EXISTS InsertPersonsIfEmpty()
BEGIN
    -- Sprawdź, czy tabela `persons` jest pusta
    IF (SELECT COUNT(*) FROM persons) = 0 THEN
        INSERT INTO persons (name, surname, birth_year, death_year)
        VALUES
            ('F. Scott', 'Fitzgerald', 1896, 1940),   -- ID=1
            ('George', 'Orwell', 1903, 1950),        -- ID=2
            ('Jane', 'Austen', 1775, 1817),          -- ID=3
            ('Mark', 'Twain', 1835, 1910),           -- ID=4
            ('Ernest', 'Hemingway', 1899, 1961),     -- ID=5
            ('Agatha', 'Christie', 1890, 1976),      -- ID=6
            ('J.K.', 'Rowling', 1965, NULL),         -- ID=7
            ('Stephen', 'King', 1947, NULL),         -- ID=8
            ('Haruki', 'Murakami', 1949, NULL),      -- ID=9
            ('Gabriel', 'Marquez', 1927, 2014),      -- ID=10
            ('Umberto', 'Eco', 1932, 2016),          -- ID=11
            ('Leo', 'Tolstoy', 1828, 1910),          -- ID=12
            ('Thomas', 'Pynchon', 1937, NULL),       -- ID=13
            ('Kurt', 'Vonnegut', 1922, 2007),        -- ID=14
            ('Isaac', 'Asimov', 1920, 1992),         -- ID=15
            ('Margaret', 'Atwood', 1939, NULL),      -- ID=16
            ('Mary', 'Shelley', 1797, 1851),         -- ID=17
            ('Franz', 'Kafka', 1883, 1924),          -- ID=18
            ('Virginia', 'Woolf', 1882, 1941),       -- ID=19
            ('Oscar', 'Wilde', 1854, 1900);          -- ID=20
    END IF;
END;



CREATE PROCEDURE IF NOT EXISTS InsertLanguagesIfEmpty()
BEGIN
    IF(SELECT COUNT(*) FROM languages) = 0 THEN
        INSERT INTO languages (lang) VALUES
            ('English'),     -- ID=1
            ('Polish'),      -- ID=2
            ('Spanish'),     -- ID=3
            ('French'),      -- ID=4
            ('German'),      -- ID=5
            ('Italian'),     -- ID=6
            ('Russian'),     -- ID=7
            ('Japanese'),    -- ID=8
            ('Chinese'),     -- ID=9
            ('Portuguese'),  -- ID=10
            ('Dutch'),       -- ID=11
            ('Swedish'),     -- ID=12
            ('Arabic'),      -- ID=13
            ('Latin'),       -- ID=14
            ('Norwegian'),   -- ID=15
            ('Polynesian'),  -- ID=16
            ('Turkish'),     -- ID=17
            ('African'),     -- ID=18
            ('Hungarian'),   -- ID=19
            ('Czech'),       -- ID=20
            ('Korean');      -- ID=21
    END IF;
END;

CREATE PROCEDURE IF NOT EXISTS InsertPublishersIfEmpty()
BEGIN
    IF(SELECT COUNT(*) FROM publishers) = 0 THEN
        INSERT INTO publishers (name, localization, foundation_year) VALUES
            ('Scribner', 'New York', 1846),    -- ID=1
            ('Secker & Warburg', 'London', 1935), -- ID=2
            ('T. Egerton', 'London', 1780),    -- ID=3
            ('Penguin Books', 'London', 1935), -- ID=4
            ('HarperCollins', 'New York', 1989), -- ID=5
            ('Random House', 'New York', 1927), -- ID=6
            ('Macmillan Publishers', 'London', 1843), -- ID=7
            ('Simon & Schuster', 'New York', 1924), -- ID=8
            ('Oxford University Press', 'Oxford', 1586), -- ID=9
            ('Hachette Livre', 'Paris', 1826),  -- ID=10
            ('Bantam Books', 'New York', 1945), -- ID=11
            ('Bloomsbury', 'London', 1986),     -- ID=12
            ('Alfred A. Knopf', 'New York', 1915), -- ID=13
            ('Penguin Books', 'London', 1935),
            ('Vintage Books', 'New York', 1954),
            ('Ace Books', 'New York', 1953),
            ('Gallimard', 'Paris', 1911),
            ('Wydawnictwo Literackie', 'Krakow', 1953),
            ('Shueisha', 'Tokyo', 1925),
            ('Springer', 'Berlin', 1842),
            ('Einaudi', 'Turin', 1933),
            ('Little, Brown and Company', 'Boston', 1837);
    END IF;
END;

CREATE PROCEDURE IF NOT EXISTS InsertCategoriesIfEmpty()
BEGIN
    IF(SELECT COUNT(*) FROM categories) = 0 THEN
        INSERT INTO categories (category) VALUES
            ('Classic'),         -- ID=1
            ('Science Fiction'), -- ID=2
            ('Romance'),         -- ID=3
            ('Thriller'),        -- ID=4
            ('Fantasy'),         -- ID=5
            ('Detective'),       -- ID=6
            ('Historical'),      -- ID=7
            ('Horror'),          -- ID=8
            ('Adventure'),       -- ID=9
            ('Biography'),       -- ID=10
            ('Poetry'),          -- ID=11
            ('Philosophy'),      -- ID=12
            ('Postmodern'),      -- ID=13
            ('Satire'),          -- ID=14
            ('Science'),         -- ID=15
            ('Drama'),           -- ID=16
            ('Essay'),           -- ID=17
            ('Political'),       -- ID=18
            ('Tragedy'),         -- ID=19
            ('Comedy');          -- ID=20
    END IF;
END;

CREATE PROCEDURE IF NOT EXISTS InsertFormsIfEmpty()
BEGIN
    IF(SELECT COUNT(*) FROM forms) = 0 THEN
        INSERT INTO forms (form) VALUES
            ('Hardcover'),       -- ID=1
            ('Paperback'),       -- ID=2
            ('E-book'),          -- ID=3
            ('Audiobook'),       -- ID=4
            ('Magazine'),        -- ID=5
            ('Newspaper'),       -- ID=6
            ('Digital PDF'),     -- ID=7
            ('Special Edition'), -- ID=8
            ('Pocket Book'),     -- ID=9
            ('Boxed Set'),       -- ID=10
            ('Collectors Edition'), -- ID=11
            ('Comic'),           -- ID=12
            ('Art Album'),       -- ID=13
            ('Loose Pages');     -- ID=14
    END IF;
END;

CREATE PROCEDURE IF NOT EXISTS InsertBookIfEmpty()
BEGIN
    IF ( (SELECT COUNT(*) FROM books) = 0 ) THEN
        INSERT INTO books (title, lang_id, series, author_id) VALUES
            ('The Great Gatsby', 1, 'Classic Series', 1),
            ('1984', 1, NULL, 2),
            ('Pride and Prejudice', 2, 'Romantic Series', 3),
            ('The Adventures of Tom Sawyer', 4, 'Children Classics', 4),
            ('Murder on the Orient Express', 1, 'Crime Collection', 6),
            ('Harry Potter and the Philosopher''s Stone', 5, 'Potter Series', 7),
            ('The Shining', 8, 'Horror Masterworks', 8),
            ('Norwegian Wood', 4, NULL, 9),
            ('One Hundred Years of Solitude', 3, 'Latin Magic', 10),
            ('The Name of the Rose', 6, 'Historical Detective', 11),
            ('War and Peace', 7, 'Epic Russian', 12),
            ('Great Expectations', 1, 'Dickens Series', 13),
            ('A Farewell to Arms', 2, 'Hemingway Collection', 5),
            ('Gravitys Rainbow', 14, NULL, 13),        -- Thomas Pynchon => ID=13
            ('Slaughterhouse-Five', 1, 'Vonnegut Collection', 14), -- Kurt Vonnegut => ID=14
            ('I, Robot', 2, 'Robot Series', 15),       -- Isaac Asimov => ID=15
            ('The Handmaids Tale', 3, 'Dystopia Atwood', 16),  -- Margaret Atwood => ID=16
            ('Frankenstein', 14, 'Gothic Horror', 17), -- Mary Shelley => ID=17
            ('The Metamorphosis', 21, 'Kafka Works', 18), -- Franz Kafka => ID=18
            ('Mrs Dalloway', 1, 'Woolf Collection', 19), -- Virginia Woolf => ID=19
            ('The Importance of Being Earnest', 1, 'Oscar Wilde Plays', 20), -- Oscar Wilde => ID=20
            ('Fahrenheit 451', 1, 'Dystopian Classics', 2),
            ('Brave New World', 1, 'Dystopian Classics', 2);
    END IF;
END;

CREATE PROCEDURE IF NOT EXISTS InsertEditionsInfoIfEmpty()
BEGIN
    IF(SELECT COUNT(*) FROM edition_infos) = 0 THEN
        INSERT INTO edition_infos (book_id, ed_title, ed_series, illustrator_id, translator_id, ed_lang_id, publisher_id, ed_num, ed_year, form_id, isbn, ukd) VALUES
            (1, 'The Great Gatsby - Special Edition', 'Classic Series', NULL, NULL, 1, 1, 1, 1925, 1, 9781234567897, '82-94'),
            (2, '1984 - Revised Edition', NULL, NULL, NULL, 1, 2, 1, 1949, 2, 9782345678910, '82-31'),
            (3, 'Pride and Prejudice - Illustrated', 'Romantic Series', 3, NULL, 2, 3, 1, 1813, 1, 9783456789123, '82-94'),
            (4,  'The Adventures of Tom Sawyer - Illustrated', 'Childhood Classics',   2,   NULL, 4,  5, 2, 2025, 4,  9781234567001, '82-101'), -- ID=4
            (5,  'Murder on the Orient Express - New Edition', NULL,                  8,   9,    1,  5, 1, 1974, 2,  9781234567002, '82-102'), -- ID=5
            (6,  'Harry Potter 1 - Deluxe',                    'Potter Deluxe',       9,   NULL, 2,  6, 1, 1997, 5,  9781234567003, '82-103'), -- ID=6
            (7,  'The Shining - Collectors',                 'Horror Masterworks',  NULL, NULL, 8,  7, 2, 1977, 5,  9781234567004, '82-104'), -- ID=7
            (8,  'Norwegian Wood - Anniversary',               NULL,                  10,  NULL, 4,  8, 3, 1987, 1,  9781234567005, '82-105'), -- ID=8
            (9,  'One Hundred Years of Solitude - Special',    'Latin Magic',         NULL, NULL, 3,  9, 1, 1967, 1,  9781234567006, '82-106'), -- ID=9
            (10, 'The Name of the Rose - Revised',             'Historical Detective',11,  6,    6, 10, 1, 1980, 4,  9781234567007, '82-107'), -- ID=10
            (11, 'War and Peace - Epic Edition',               NULL,                  NULL, NULL, 7, 11, 2, 1869, 8,  9781234567008, '82-108'), -- ID=11
            (12, 'Great Expectations - Modern',                'Dickens Series',      13,  NULL, 1, 12, 2, 2020, 2,  9781234567009, '82-109'), -- ID=12
            (13, 'A Farewell to Arms - Revised',               'Hemingway Collection',5,   NULL, 2, 13, 3, 1957, 1,  9781234567010, '82-110'),
            (14, 'Gravitys Rainbow - Illustrated', NULL, NULL, 16, 14, 14, 1, 1973, 14, 9782222222014, '82-201'),
            (15, 'Slaughterhouse-Five - Reprint', 'Vonnegut Collection', 15, NULL, 1, 15, 1, 1969, 15, 9782222222015, '82-202'),
            (16, 'I, Robot - Anniversary Edition', 'Robot Series', NULL, NULL, 2, 16, 2, 1950, 16, 9782222222016, '82-203'),
            (17, 'The Handmaids Tale - Deluxe', 'Dystopia Atwood', NULL, 17, 3, 17, 1, 1985, 17, 9782222222017, '82-204'),
            (18, 'Frankenstein - Critical', 'Gothic Horror', 14, NULL, 14, 18, 2, 1818, 18, 9782222222018, '82-205'),
            (19, 'The Metamorphosis - Illustrated', 'Kafka Works', NULL, 19, 21, 19, 1, 1915, 19, 9782222222019, '82-206'),
            (20, 'Mrs Dalloway - Updated', 'Woolf Collection', NULL, NULL, 1, 20, 1, 1925, 14, 9782222222020, '82-207'),
            (21, 'The Importance of Being Earnest - Modern', 'Oscar Wilde Plays', 21, NULL, 1, 21, 2, 1895, 15, 9782222222021, '82-208'),
            (22, 'Fahrenheit 451 - Reissue', 'Dystopian Classics', NULL, NULL, 1, 15, 1, 1953, 16, 9782222222022, '82-209'),
            (23, 'Brave New World - Reissue', 'Dystopian Classics', NULL, NULL, 1, 15, 1, 1932, 17, 9782222222023, '82-210');
    END IF;
END;

CREATE PROCEDURE IF NOT EXISTS InsertCopiesIfEmpty()
BEGIN
    IF(SELECT COUNT(*) FROM copies) = 0 THEN
        INSERT INTO copies (ed_id, rented) VALUES
            (1, TRUE),
            (2, FALSE),
            (3, TRUE),
            (4, TRUE),   -- ID=4
            (5, FALSE),  -- ID=5
            (6, TRUE),   -- ID=6
            (7, FALSE),  -- ID=7
            (8, TRUE),   -- ID=8
            (9, TRUE),   -- ID=9
            (10, FALSE), -- ID=10
            (11, TRUE),  -- ID=11
            (12, FALSE), -- ID=12
            (13, TRUE),
            (14, FALSE),
            (15, TRUE),
            (16, FALSE),
            (17, TRUE),
            (18, FALSE),
            (19, TRUE),
            (20, FALSE),
            (21, TRUE),
            (22, FALSE),
            (23, TRUE);
    END IF;
END;

CREATE PROCEDURE IF NOT EXISTS InsertBook_catIfEmpty()
BEGIN
    IF(SELECT COUNT(*) FROM book_categories) = 0 THEN
        INSERT INTO book_categories (book_id, cat_id) VALUES
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),   -- ID=4
            (5, 5),   -- ID=5
            (6, 6),   -- ID=6
            (7, 7),   -- ID=7
            (8, 8),   -- ID=8
            (9, 9),   -- ID=9
            (10, 10), -- ID=10
            (11, 11), -- ID=11
            (12, 12), -- ID=12
            (13, 13),
            (14, 14),
            (15, 15),
            (16, 16),
            (17, 17),
            (18, 18),
            (19, 19),
            (20, 20),
            (21, 21);
    END IF;
END;

CREATE PROCEDURE IF NOT EXISTS InsertUser_InfosIfEmpty()
BEGIN
    IF(SELECT COUNT(*) FROM user_infos) = 0 THEN
        INSERT INTO user_infos (name, surname, phone, card_num) VALUES
        ('John', 'Doe', '123456789', '1001'),
        ('Jane', 'Smith', '987654321', '1002'),
        ('Alice', 'Jones', '555666777', '1003'),
        ('Tom',   'Adams',   '111222333', '1004'),  -- ID=4
        ('Mary',  'Baker',   '222333444', '1005'),  -- ID=5
        ('Bruce', 'Wayne',   '333444555', '1006'),  -- ID=6
        ('Peter', 'Parker',  '444555666', '1007'),  -- ID=7
        ('Tony',  'Stark',   '555666777', '1008'),  -- ID=8
        ('Clark', 'Kent', '111111111', '1014'),
        ('Diana', 'Prince', '222222222', '1015'),
        ('Steve', 'Rogers', '333333333', '1016'),
        ('Natasha', 'Romanoff', '444444444', '1017'),
        ('Barry', 'Allen', '555555555', '1018'),
        ('Victor', 'Stone', '666666666', '1019');
    END IF;
END;

CREATE PROCEDURE IF NOT EXISTS InsertUsersIfEmpty()
BEGIN
    IF(SELECT COUNT(*) FROM users) = 0 THEN
        INSERT INTO users (email, password, user_infos_id, role, created_at) VALUES
            ('john@example.com', '$2b$12$Fvh3f.QLDfMLPcgW0YvbEON2M3zTE05zpm41/A9REJWqQAVzxgvTO', 1, 'User', '2024-01-01 10:00:00'),
            ('jane@example.com', '$2b$12$mpfjKgqZPLaidH.4Ft8VQ.xt10aU42g.lkqT8xqFNEPMaJjxkZxWu', 2, 'Worker', '2024-02-15 15:30:00'),
            ('alice@example.com', '$2b$12$XEhx74/luzQjClZX7AMEq.jFOECOCq5ZFgyJee01vH58m8S7EM1B.', 3, 'Admin', '2024-03-10 12:45:00');
    END IF;
END;

CREATE PROCEDURE IF NOT EXISTS InsertRentalsIfEmpty()
BEGIN
    IF(SELECT COUNT(*) FROM rentals) = 0 THEN
        INSERT INTO rentals (user_id, copy_id, rental_date, due_date, return_date) VALUES
            (1, 1, '2024-01-01', '2024-01-15', '2024-01-10'),
            (2, 2, '2024-02-01', '2024-02-15', NULL),
            (3, 3, '2024-03-01', '2024-03-15', '2024-03-12'),
            (1, 4, '2024-04-01', '2024-04-15', NULL),       -- ID=4
            (2, 5, '2024-05-01', '2024-05-15', '2024-05-14'),
            (3, 6, '2024-06-01', '2024-06-15', NULL),
            (1, 7, '2024-07-01', '2024-07-15', '2024-07-10'),
            (2, 8, '2024-08-01', '2024-08-15', NULL),
            (1, 14, '2025-01-01', '2025-01-15', NULL),
            (2, 15, '2025-02-01', '2025-02-15', '2025-02-14'),
            (3, 16, '2025-03-01', '2025-03-15', NULL),
            (1, 17, '2025-04-01', '2025-04-15', '2025-04-10'),
            (2, 18, '2025-05-01', '2025-05-15', NULL),
            (3, 19, '2025-06-01', '2025-06-15', '2025-06-13'),
            (1, 20, '2025-07-01', '2025-07-15', NULL),
            (2, 21, '2025-08-01', '2025-08-15', NULL);
    END IF;
END;

CREATE PROCEDURE IF NOT EXISTS InsertAnnotationsIfEmpty()
BEGIN
    IF(SELECT COUNT(*) FROM annotations) = 0 THEN
        INSERT INTO annotations (book_id, ed_id, copy_id, content) VALUES
            (1, NULL, NULL, 'A story about the American dream and wealth.'),
            (2, NULL, NULL, 'Dystopian tale of a totalitarian regime and surveillance.'),
            (3, NULL, NULL, 'Romantic novel exploring manners and courtship.'),
            (4, 4, 4, 'A coming-of-age tale set in a small town.'),                    -- ID=4
            (5, 5, 5, 'A thrilling detective story taking place aboard a train.'),     -- ID=5
            (6, 6, 6, 'A young wizard begins his journey at Hogwarts.'),               -- ID=6
            (7, 7, 7, 'A writer battles supernatural forces in an isolated hotel.'),    -- ID=7
            (8, 8, 8, 'A Japanese tale exploring love, loss, and memory in Tokyo.'),
            (14, 14, 14, 'A dense, complex novel set in WWII Europe.'),
            (15, 15, 15, 'An anti-war satire involving time travel.'),
            (16, 16, 16, 'A collection of short stories about robots and ethics.'),
            (17, 17, 17, 'Dystopian future where women lose autonomy.'),
            (18, 18, 18, 'A gothic tale of science creating a monster.'),
            (19, 19, 19, 'A man wakes up transformed into an insect.'),
            (20, 20, 20, 'An experimental novel of one day in a woman’s life.'),
            (21, 21, 21, 'A witty comedy of mistaken identities.'),
            (22, 22, 22, 'A future where books are burned for censorship.'),
            (23, 23, 23, 'A genetically engineered utopia turning dystopian.');
    END IF;
END;

CALL InsertPersonsIfEmpty();

CALL InsertLanguagesIfEmpty();

CALL InsertPublishersIfEmpty();

CALL InsertCategoriesIfEmpty();

CALL InsertUser_InfosIfEmpty();

CALL InsertFormsIfEmpty();

CALL InsertBookIfEmpty();
-- wymaga persons & languages
CALL InsertEditionsInfoIfEmpty();
-- wymaga books
CALL InsertCopiesIfEmpty();
-- wymaga edition_infos
CALL InsertBook_catIfEmpty();
-- wymaga books & categories
CALL InsertUsersIfEmpty();
-- wstawiamy użytkowników (opcjonalnie, 3 w sumie)
CALL InsertRentalsIfEmpty();
-- wymaga copies & users
CALL InsertAnnotationsIfEmpty();    -- wymaga books (i ewentualnie ed/copy)
