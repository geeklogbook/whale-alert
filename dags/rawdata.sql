-- -- create table

CREATE TABLE IF NOT EXISTS rawdata (
    id VARCHAR(20) PRIMARY KEY,
    datetime_utc VARCHAR(20),
    crypto VARCHAR(20),
    known VARCHAR(20),
    unknown VARCHAR(20),
    username
);