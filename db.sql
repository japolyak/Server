CREATE DATABASE app;

USE app;


CREATE TABLE people
(
    id    INT AUTO_INCREMENT,
    name  TEXT,
    sname TEXT,
    PRIMARY KEY (id)
);

INSERT INTO people (name, sname) VALUES ('A', 'B'), ('C', 'D'), ('E', 'F');


SELECT
    id,
    name,
    sname
FROM people;


SELECT *
FROM people
WHERE
    id = 3;

DELETE FROM people
WHERE
    id = 3;

UPDATE people
SET
    name = 'mda',
    sname = 'pizda'
WHERE
    id = 1;


# https://mariadb.com/kb/en/joining-tables-with-join-clauses/
SELECT
    mems.id,
    mems.name,
    mems.link,
    mems.person_id,
    people.id,
    people.name
FROM mems
JOIN people on mems.person_id = people.id
WHERE people.name = 'Vasya'

ALTER TABLE people ADD login text;
