-- Tabela osób (persons)
CREATE TABLE IF NOT EXISTS persons (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  surname VARCHAR(255),
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
  FOREIGN KEY (author_id)
    REFERENCES persons(id)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION,
  FOREIGN KEY (lang_id)
    REFERENCES languages(id)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION
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
  FOREIGN KEY (book_id)
    REFERENCES books(id)
    ON DELETE NO ACTION,
  FOREIGN KEY (illustrator_id)
    REFERENCES persons(id)
    ON DELETE RESTRICT,
  FOREIGN KEY (translator_id)
    REFERENCES persons(id)
    ON DELETE RESTRICT,
  FOREIGN KEY (ed_lang_id)
    REFERENCES languages(id)
    ON DELETE RESTRICT,
  FOREIGN KEY (publisher_id)
    REFERENCES publishers(id)
    ON DELETE RESTRICT,
  FOREIGN KEY (form_id)
    REFERENCES forms(id)
    ON DELETE RESTRICT
);

-- Tabela kopii książek (copies)
CREATE TABLE IF NOT EXISTS copies (
  id INT PRIMARY KEY AUTO_INCREMENT,
  ed_id INT NOT NULL,
  rented BOOLEAN NOT NULL DEFAULT FALSE,
  FOREIGN KEY (ed_id)
    REFERENCES edition_infos(id)
    ON DELETE NO ACTION
);


-- Tabela pośrednia książki do kategorii (book_categories)
CREATE TABLE IF NOT EXISTS book_categories (
  book_id INT NOT NULL,
  cat_id INT NOT NULL,
  PRIMARY KEY (book_id, cat_id),
  FOREIGN KEY (book_id)
    REFERENCES books(id)
    ON DELETE CASCADE,
  FOREIGN KEY (cat_id)
    REFERENCES categories(id)
    ON DELETE CASCADE
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
  copy_id INT,
  rental_date DATE NOT NULL,
  due_date DATE NOT NULL,
  return_date DATE,
  FOREIGN KEY (user_id)
    REFERENCES users(id)
    ON UPDATE NO ACTION
    ON DELETE NO ACTION,
  FOREIGN KEY (copy_id)
    REFERENCES copies(id)
    ON UPDATE NO ACTION
    ON DELETE SET NULL
);

-- Tabela adnotacji (annotations)
CREATE TABLE IF NOT EXISTS annotations (
  id INT PRIMARY KEY AUTO_INCREMENT,
  book_id INT,
  ed_id INT,
  copy_id INT,
  content TEXT NOT NULL,
  FOREIGN KEY (book_id)
    REFERENCES books(id)
    ON DELETE CASCADE,
  FOREIGN KEY (ed_id)
    REFERENCES edition_infos(id)
    ON DELETE CASCADE,
  FOREIGN KEY (copy_id)
    REFERENCES copies(id)
    ON DELETE CASCADE
);


-- Tabela rezerwacji (reservations)
CREATE TABLE IF NOT EXISTS reservations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    copy_id INT,
    reserved_at DATETIME NOT NULL,
    reserved_due DATE,
    status ENUM('Reserved', 'Awaiting', 'Cancelled', 'PastDue', 'Succeeded') NOT NULL DEFAULT 'Reserved',
    FOREIGN KEY (copy_id)
        REFERENCES copies(id)
        ON UPDATE NO ACTION
        ON DELETE SET NULL,
    FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);



CREATE PROCEDURE IF NOT EXISTS InsertPersonsIfEmpty()
BEGIN
    -- Sprawdź, czy tabela `persons` jest pusta
    IF (SELECT COUNT(*) FROM persons) = 0 THEN
        INSERT INTO persons (name, surname, birth_year, death_year) VALUES
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
            ('Oscar', 'Wilde', 1854, 1900),          -- ID=20
            ('Wolfgang Amadeus', 'Mozart', 1712, 1740);          -- ID=20
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
            ('Hardcover'),         -- ID=1
            ('Paperback'),         -- ID=2
            ('E-book'),            -- ID=3
            ('Audiobook'),         -- ID=4
            ('Magazine'),          -- ID=5
            ('Newspaper'),         -- ID=6
            ('Digital PDF'),       -- ID=7
            ('Special Edition'),   -- ID=8
            ('Pocket Book'),       -- ID=9
            ('Boxed Set'),         -- ID=10
            ('Collectors Edition'),-- ID=11
            ('Comic'),             -- ID=12
            ('Art Album'),         -- ID=13
            ('Loose Pages'),       -- ID=14
            ('Extended Format'),   -- ID=15
            ('Deluxe Bound'),      -- ID=16
            ('Ancient Scroll'),    -- ID=17
            ('Pocket Magazine'),   -- ID=18
            ('Print on Demand');   -- ID=19
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
            (4, 'The Adventures of Tom Sawyer - Illustrated', 'Childhood Classics', 2, NULL, 4, 5, 2, 2025, 4, 9781234567001, '82-101'),
            (5, 'Murder on the Orient Express - New Edition', NULL, 8, 9, 1, 5, 1, 1974, 2, 9781234567002, '82-102'),
            (6, 'Harry Potter 1 - Deluxe', 'Potter Deluxe', 9, NULL, 2, 6, 1, 1997, 5, 9781234567003, '82-103'),
            (7, 'The Shining - Collectors', 'Horror Masterworks', NULL, NULL, 8,  7, 2, 1977, 5, 9781234567004, '82-104'),
            (8, 'Norwegian Wood - Anniversary', NULL, 10, NULL, 4, 8, 3, 1987, 1, 9781234567005, '82-105'),
            (9, 'One Hundred Years of Solitude - Special', 'Latin Magic', NULL, NULL, 3, 9, 1, 1967, 1, 9781234567006, '82-106'),
            (10, 'The Name of the Rose - Revised', 'Historical Detective', 11, 6, 6, 10, 1, 1980, 4, 9781234567007, '82-107'),
            (11, 'War and Peace - Epic Edition', NULL, NULL, NULL, 7, 11, 2, 1869, 8, 9781234567008, '82-108'),
            (12, 'Great Expectations - Modern', 'Dickens Series', 13, NULL, 1, 12, 2, 2020, 2, 9781234567009, '82-109'),
            (13, 'A Farewell to Arms - Revised', 'Hemingway Collection',5, NULL, 2, 13, 3, 1957, 1, 9781234567010, '82-110'),
            (14, 'Gravitys Rainbow - Illustrated', NULL, NULL, 16, 14, 14, 1, 1973, 14, 9782222222014, '82-201'),
            (15, 'Slaughterhouse-Five - Reprint', 'Vonnegut Collection', 15, NULL, 1, 15, 1, 1969, 15, 9782222222015, '82-202'),
            (16, 'I, Robot - Anniversary Edition', 'Robot Series', NULL, NULL, 2, 16, 2, 1950, 16, 9782222222016, '82-203'),
            (17, 'The Handmaids Tale - Deluxe', 'Dystopia Atwood', NULL, 17, 3, 17, 1, 1985, 17, 9782222222017, '82-204'),
            (18, 'Frankenstein - Critical', 'Gothic Horror', 14, NULL, 14, 18, 2, 1818, 18, 9782222222018, '82-205'),
            (19, 'The Metamorphosis - Illustrated', 'Kafka Works', NULL, 19, 21, 19, 1, 1915, 19, 9782222222019, '82-206'),
            (20, 'Mrs Dalloway - Updated', 'Woolf Collection', NULL, NULL, 1, 20, 1, 1925, 14, 9782222222020, '82-207'),
            (21, 'The Importance of Being Earnest - Modern', 'Oscar Wilde Plays', 20, NULL, 1, 21, 2, 1895, 15, 9782222222021, '82-208'),
            (22, 'Fahrenheit 451 - Reissue', 'Dystopian Classics', NULL, NULL, 1, 15, 1, 1953, 16, 9782222222022, '82-209'),
            (23, 'Brave New World - Reissue', 'Dystopian Classics', NULL, NULL, 1, 15, 1, 1932, 17, 9782222222023, '82-210');
    END IF;
END;

CREATE PROCEDURE IF NOT EXISTS InsertCopiesIfEmpty()
BEGIN
    IF(SELECT COUNT(*) FROM copies) = 0 THEN
        INSERT INTO copies (ed_id) VALUES
            (1),
            (2),
            (3),
            (4),   -- ID=4
            (5),  -- ID=5
            (6),   -- ID=6
            (7),  -- ID=7
            (8),   -- ID=8
            (9),   -- ID=9
            (10), -- ID=10
            (11),  -- ID=11
            (12), -- ID=12
            (13),
            (14),
            (15),
            (16),
            (17),
            (18),
            (19),
            (20),
            (21),
            (22),
            (23);
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
            (20, 20);
    END IF;
END;

CREATE PROCEDURE IF NOT EXISTS InsertUser_InfosIfEmpty()
BEGIN
    IF(SELECT COUNT(*) FROM user_infos) = 0 THEN
        INSERT INTO user_infos (name, surname, phone, card_num) VALUES
        ('John', 'Doe', '123456789', '1001'),
        ('Jane', 'Smith', '987654321', '1002'),
        ('Alice', 'Jones', '555666777', '1003');
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
            (10, 10, 10, 'A future where books are burned for censorship.'),
            (9, 9, 9, 'A genetically engineered utopia turning dystopian.');
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

CALL InsertAnnotationsIfEmpty();