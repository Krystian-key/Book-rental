-- Tabela users: przechowuje dane użytkowników
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT CHECK(role IN ('czytelnik', 'pracownik', 'admin')) NOT NULL
);

-- Tabela books: przechowuje dane książek
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT,
    status TEXT CHECK(status IN ('dostępna', 'wypożyczona')) DEFAULT 'dostępna',
    borrowed_by INTEGER,
    FOREIGN KEY(borrowed_by) REFERENCES users(id)
);

-- Tabela borrow_history: przechowuje historię wypożyczeń książek
CREATE TABLE IF NOT EXISTS borrow_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    book_id INTEGER,
    borrow_date TEXT,
    return_date TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(book_id) REFERENCES books(id)
);
