CREATE USER user_ai WITH PASSWORD 'UltraSuperSecretote';

CREATE DATABASE db_ai OWNER user_ai;

\c db_ai postgres

CREATE EXTENSION IF NOT EXISTS vector;

\c db_ai user_ai

CREATE TABLE faqs (
  id SERIAL PRIMARY KEY,
  question TEXT NOT NULL,
  answer TEXT NOT NULL,
  embedding vector(1536)
);
