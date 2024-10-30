/* Tabela users: przechowuje dane użytkowników */
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('czytelnik', 'pracownik', 'admin') NOT NULL
);

/* Tabela books: przechowuje dane książek */
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255),
    status ENUM('dostępna', 'wypożyczona') DEFAULT 'dostępna',
    borrowed_by INT,
    FOREIGN KEY(borrowed_by) REFERENCES users(id)
);

/* Tabela borrow_history: przechowuje historię wypożyczeń książek */
CREATE TABLE IF NOT EXISTS borrow_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    book_id INT,
    borrow_date DATETIME,
    return_date DATETIME,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(book_id) REFERENCES books(id)
);