CREATE DATABASE foods;
use foods;

CREATE TABLE food (
  name VARCHAR(20),
  eid VARCHAR(10)
);

INSERT INTO food
VALUES
  ('ice-cream', 30),
  ('potato', 10),
  ('noodles',50);