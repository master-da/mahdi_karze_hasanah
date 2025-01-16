CREATE TABLE IF NOT EXISTS customer (
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(63) NOT NULL,
    password VARCHAR(63) NOT NULL,
    first_name VARCHAR(63) NOT NULL,
    last_name VARCHAR(63) NOT NULL,
    email VARCHAR(127) NOT NULL,
    mobile_number VARCHAR(15) NOT NULL,
    date_of_birth DATE NOT NULL,
    address TEXT NOT NULL,
    balance NUMERIC(10, 2) NOT NULL CHECK (balance >= 0)
);

CREATE TABLE IF NOT EXISTS transaction (
    trx_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    from_user_id INT NOT NULL,
    to_user_id INT NOT NULL,
    amount NUMERIC(10, 2) NOT NULL CHECK (amount >= 0),
    FOREIGN KEY (to_user_id) REFERENCES customer(user_id),
    FOREIGN KEY (from_user_id) REFERENCES customer(user_id)
);