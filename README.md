# postgre

CREATE TABLE customer (
    id INTEGER NOT NULL,
    name VARCHAR(255),
    PRIMARY KEY (id)
);

CREATE TABLE customerbook (
    id INTEGER NOT NULL,
    name VARCHAR NOT NULL,
    customer_id INTEGER,
    PRIMARY KEY (id),
    CONSTRAINT customer_id_fk FOREIGN KEY(customer_id) REFERENCES customer (id)
)
