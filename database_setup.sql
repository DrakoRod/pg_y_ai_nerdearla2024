CREATE USER draks_bot_user WITH PASSWORD 'UltraSuperSecretote';

CREATE DATABASE draks_bot_db OWNER draks_bot_user;

\c draks_bot_db postgres

CREATE EXTENSION IF NOT EXISTS vector;

\c draks_bot_db draks_bot_user

CREATE TABLE faqs (
  id SERIAL PRIMARY KEY,
  question TEXT NOT NULL,
  answer TEXT NOT NULL,
  embedding vector(1536)
);
