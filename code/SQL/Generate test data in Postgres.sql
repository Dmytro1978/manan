CREATE TABLE test_data 
(
  section   NUMERIC NOT NULL,
  id1       NUMERIC NOT NULL,
  id2       NUMERIC NOT NULL
);

INSERT INTO test_data
SELECT sections.*,
       gen.*,
       CEIL(RANDOM()*100)   -- CEIL(expr2)  - rounds the argument to the nearest integer as greater than the argument
                            -- FLOOR(expr2) - rounds the argument to the nearest integer as smaller than the argument
                            -- RANDOM() - returns a random value in the range 0.0 <= x < 1.0
FROM GENERATE_SERIES(1,30) sections, -- GENERATE_SERIES(start, stop) - generates a series of values, from start to stop with a step size of one
     GENERATE_SERIES(1,90) gen
WHERE 
    gen <= sections*3000;