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
            ('F. Scott', 'Fitzgerald', 1896, 1940),
            ('George', 'Orwell', 1903, 1950),
            ('Jane', 'Austen', 1775, 1817),
            ('Mark', 'Twain', 1835, 1910),          -- ID=4
            ('Ernest', 'Hemingway', 1899, 1961),    -- ID=5
            ('Agatha', 'Christie', 1890, 1976),     -- ID=6
            ('J.K.', 'Rowling', 1965, NULL),        -- ID=7
            ('Stephen', 'King', 1947, NULL),        -- ID=8
            ('Haruki', 'Murakami', 1949, NULL),     -- ID=9
            ('Gabriel', 'Marquez', 1927, 2014),     -- ID=10
            ('Umberto', 'Eco', 1932, 2016),         -- ID=11
            ('Leo', 'Tolstoy', 1828, 1910),         -- ID=12
            ('Charles', 'Dickens', 1812, 1870);     -- ID=13
    END IF;
END;



CREATE PROCEDURE IF NOT EXISTS InsertLanguagesIfEmpty()
BEGIN
    IF(SELECT COUNT(*) FROM languages) = 0 THEN
        INSERT INTO languages (lang) VALUES
            ('English'),
            ('Polish'),
            ('Spanish'),
            ('French'),       -- ID=4
            ('German'),       -- ID=5
            ('Italian'),      -- ID=6
            ('Russian'),      -- ID=7
            ('Japanese'),     -- ID=8
            ('Chinese'),      -- ID=9
            ('Portuguese'),   -- ID=10
            ('Dutch'),        -- ID=11
            ('Swedish'),      -- ID=12
            ('Arabic');       -- ID=13
    END IF;
END;

CREATE PROCEDURE IF NOT EXISTS InsertPublishersIfEmpty()
BEGIN
    IF(SELECT COUNT(*) FROM publishers) = 0 THEN
        INSERT INTO publishers (name, localization, foundation_year) VALUES
            ('Scribner', 'New York', 1846),
            ('Secker & Warburg', 'London', 1935),
            ('T. Egerton', 'London', 1780),
            ('Penguin Books', 'London', 1935),            -- ID=4
            ('HarperCollins', 'New York', 1989),          -- ID=5
            ('Random House', 'New York', 1927),           -- ID=6
            ('Macmillan Publishers', 'London', 1843),     -- ID=7
            ('Simon & Schuster', 'New York', 1924),       -- ID=8
            ('Oxford University Press', 'Oxford', 1586),  -- ID=9
            ('Hachette Livre', 'Paris', 1826),            -- ID=10
            ('Bantam Books', 'New York', 1945),           -- ID=11
            ('Bloomsbury', 'London', 1986),               -- ID=12
            ('Alfred A. Knopf', 'New York', 1915);        -- ID=13
    END IF;
END;

CREATE PROCEDURE IF NOT EXISTS InsertCategoriesIfEmpty()
BEGIN
    IF(SELECT COUNT(*) FROM categories) = 0 THEN
        INSERT INTO categories (category) VALUES
            ('Classic'),
            ('Science Fiction'),
            ('Romance'),
            ('Thriller'),      -- ID=4
            ('Fantasy'),       -- ID=5
            ('Detective'),     -- ID=6
            ('Historical'),    -- ID=7
            ('Horror'),        -- ID=8
            ('Adventure'),     -- ID=9
            ('Biography'),     -- ID=10
            ('Poetry'),        -- ID=11
            ('Science'),       -- ID=12
            ('Philosophy');    -- ID=13
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
        ('Tony',  'Stark',   '555666777', '1008');  -- ID=8
    END IF;
END;

CREATE PROCEDURE IF NOT EXISTS InsertFormsIfEmpty()
BEGIN
    IF(SELECT COUNT(*) FROM forms) = 0 THEN
        INSERT INTO forms (form) VALUES
            ('Hardcover'),
            ('Paperback'),
            ('E-book'),
            ('Audiobook'),      -- ID=4
            ('Magazine'),       -- ID=5
            ('Newspaper'),      -- ID=6
            ('Digital PDF'),    -- ID=7
            ('Special Edition');-- ID=8
    END IF;
END;

CREATE PROCEDURE IF NOT EXISTS InsertBookIfEmpty()
BEGIN
    IF(SELECT COUNT(*) FROM books) = 0 THEN
        INSERT INTO books (title, lang_id, series, author_id) VALUES
        ('The Great Gatsby', 1, 'Classic Series', 1),
        ('1984', 1, NULL, 2),
        ('Pride and Prejudice', 2, 'Romantic Series', 3),
        ('The Adventures of Tom Sawyer',      4, 'Children Classics',     4 ),  -- ID=4
        ('Murder on the Orient Express',      1, 'Crime Collection',      6 ),  -- ID=5
        ('Harry Potter and the Philosophers Stone', 5, 'Potter Series', 7 ),  -- ID=6
        ('The Shining',                       8, 'Horror Masterworks',   8 ),  -- ID=7
        ('Norwegian Wood',                    4, NULL,                   9 ),  -- ID=8
        ('One Hundred Years of Solitude',     3, 'Latin Magic',         10 ),  -- ID=9
        ('The Name of the Rose',              6, 'Historical Detective', 11 ),  -- ID=10
        ('War and Peace',                     7, 'Epic Russian',        12 ),  -- ID=11
        ('Great Expectations',                1, 'Dickens Series',      13 ),  -- ID=12
        ('A Farewell to Arms',                2, 'Hemingway Collection', 5 );  -- ID=13
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
            (13, 'A Farewell to Arms - Revised',               'Hemingway Collection',5,   NULL, 2, 13, 3, 1957, 1,  9781234567010, '82-110'); -- ID=13
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
            (13, TRUE);  -- ID=13
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
            (13, 13); -- ID=13
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
            (2, 8, '2024-08-01', '2024-08-15', NULL);       -- ID=8
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
            (8, 8, 8, 'A Japanese tale exploring love, loss, and memory in Tokyo.');    -- ID=8
    END IF;
END;



CALL InsertPersonsIfEmpty();

CALL InsertLanguagesIfEmpty();

CALL InsertPublishersIfEmpty();

CALL InsertCategoriesIfEmpty();

CALL InsertUser_InfosIfEmpty();

CALL InsertFormsIfEmpty();

CALL InsertBookIfEmpty();

CALL InsertEditionsInfoIfEmpty();

CALL InsertCopiesIfEmpty();

CALL InsertBook_catIfEmpty();

CALL InsertUsersIfEmpty();

CALL InsertRentalsIfEmpty();

CALL InsertAnnotationsIfEmpty();
