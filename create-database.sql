CREATE DATABASE techniqueCollector;

CREATE USER technique_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE techniqueCollector TO technique_admin;
