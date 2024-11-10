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


-- Wstawienie przykładowych danych do tabeli rentals
INSERT INTO rentals (user_id, copy_id, rental_date, due_date, return_date) VALUES
(1, 1, '2024-01-01', '2024-01-15', '2024-01-10'),
(2, 2, '2024-02-01', '2024-02-15', NULL),
(3, 3, '2024-03-01', '2024-03-15', '2024-03-12');


-- Wstawienie przykładowych danych do tabeli copies
INSERT INTO copies (ed_id, rented) VALUES
(1, TRUE),
(2, FALSE),
(3, TRUE);


-- Wstawienie przykładowych danych do tabeli books
INSERT INTO books (title, lang_id, series, author_id) VALUES
('The Great Gatsby', 1, 'Classic Series', 1),
('1984', 1, NULL, 2),
('Pride and Prejudice', 2, 'Romantic Series', 3);


-- Wstawienie przykładowych danych do tabeli edition_infos
INSERT INTO edition_infos (book_id, ed_title, ed_series, illustrator_id, translator_id, ed_lang_id, publisher_id, ed_num, ed_year, form_id, isbn, ukd) VALUES
(1, 'The Great Gatsby - Special Edition', 'Classic Series', NULL, NULL, 1, 1, 1, 1925, 1, 9781234567897, '82-94'),
(2, '1984 - Revised Edition', NULL, NULL, NULL, 1, 2, 1, 1949, 2, 9782345678910, '82-31'),
(3, 'Pride and Prejudice - Illustrated', 'Romantic Series', 4, NULL, 2, 3, 1, 1813, 1, 9783456789123, '82-94');


-- Wstawienie przykładowych danych do tabeli persons
INSERT INTO persons (name, surname, birth_year, death_year) VALUES
('F. Scott', 'Fitzgerald', 1896, 1940),
('George', 'Orwell', 1903, 1950),
('Jane', 'Austen', 1775, 1817);


-- Wstawienie przykładowych danych do tabeli languages
INSERT INTO languages (lang) VALUES
('English'),
('Polish'),
('Spanish');


-- Wstawienie przykładowych danych do tabeli publishers
INSERT INTO publishers (name, localization, foundation_year) VALUES
('Scribner', 'New York', 1846),
('Secker & Warburg', 'London', 1935),
('T. Egerton', 'London', 1780);


-- Wstawienie przykładowych danych do tabeli categories
INSERT INTO categories (category) VALUES
('Classic'),
('Science Fiction'),
('Romance');


-- Wstawienie przykładowych danych do tabeli annotations
INSERT INTO annotations (book_id, ed_id, copy_id, content) VALUES
(1, 1, 1, 'A story about the American dream and wealth.'),
(2, 2, 2, 'Dystopian tale of a totalitarian regime and surveillance.'),
(3, 3, 3, 'Romantic novel exploring manners and courtship.');


-- Wstawienie przykładowych danych do tabeli book_categories
INSERT INTO book_categories (book_id, cat_id) VALUES
(1, 1),
(2, 2),
(3, 3);


-- Wstawienie przykładowych danych do tabeli users
INSERT INTO users (email, password, user_infos_id, role, created_at) VALUES
('john@example.com', 'hashed_password1', 1, 'User', '2024-01-01 10:00:00'),
('jane@example.com', 'hashed_password2', 2, 'Worker', '2024-02-15 15:30:00'),
('alice@example.com', 'hashed_password3', 3, 'Admin', '2024-03-10 12:45:00');


-- Wstawienie przykładowych danych do tabeli user_infos
INSERT INTO user_infos (name, surname, phone, card_num) VALUES
('John', 'Doe', '123456789', '1001'),
('Jane', 'Smith', '987654321', '1002'),
('Alice', 'Jones', '555666777', '1003');


-- Wstawienie przykładowych danych do tabeli forms
INSERT INTO forms (form) VALUES
('Hardcover'),
('Paperback'),
('E-book');

/* */
