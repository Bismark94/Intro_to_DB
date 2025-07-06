-- task_3.sql
-- List all tables in the database supplied to the mysql command

SELECT
  TABLE_NAME
FROM
  information_schema.tables
WHERE
  table_schema = DATABASE()
ORDER BY
  TABLE_NAME;
