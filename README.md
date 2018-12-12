# postgre

CREATE TABLE customer (
    id INTEGER NOT NULL,
    name VARCHAR(255),
    PRIMARY KEY (id)
);

CREATE TABLE public.customerbook
(
    id serial PRIMARY KEY,
    name varchar(255) NOT NULL,
    customer_id int NOT NULL,
    CONSTRAINT customerbook_customer_id_fk FOREIGN KEY (customer_id) REFERENCES public.customer (id)
);
CREATE UNIQUE INDEX customerbook_id_uindex ON public.customerbook (id);
