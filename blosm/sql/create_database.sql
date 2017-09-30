CREATE DATABASE blosm;

CREATE USER blosm WITH PASSWORD 'bl0sm';
ALTER ROLE blosm SET client_encoding TO 'utf8';
ALTER ROLE blosm SET default_transaction_isolation TO 'read committed';
ALTER ROLE blosm SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE blosm TO blosm;
