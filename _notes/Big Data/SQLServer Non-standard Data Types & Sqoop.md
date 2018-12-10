## Non standard SQL Server data types & Sqoop: UNIQUEIDENTIFIER and SQL_VARIANT 

### UNIQUEIDENTIFIER
_UNIQUEIDENTIFIER_ as a primary key in the table:

The _UNIQUEIDENTIFIER_ is a GUID and can’t be used by sqoop to split work units. By default, if number of mappers is not mentioned, sqoop defines 4 mappers and it uses a primary key column in _--split-by_ parameter to split work units. 
There are two options to solve the issue:
1. Set number of mappers to 1. In this case sqoop will not use _--split-by_ parameter;
2. Explicitly choose different column to be used for _--split-by_ parameter.

For information: to insert a new _UNIQUEIDENTIFIER_ value into a table use _NEWID()_:
```sql
CREATE TABLE Table1 
(
    Id UNIQUEIDENTIFIER, 
    Name VARCHAR(20)
);

INSERT INTO Table1
SELECT NEWID(), 'Sam'
```

A function _NEWSEQUENTIALID()_ can only be used in _CREATE TABLE_ or _ALTER TABLE_:

```sql
CREATE TABLE Table2
(
    Id UNIQUEIDENTIFIER DEFAULT NEWSEQUENTIALID(),
    Name VARCHAR(20)
);
```
_NEWSEQUENTIALID_ cannot be referenced in queries.

## SQL_VARIANT

Sqoop does not work with SQL_VARIANT data type, so it should be converted to String. It can be done in an sql-query: 
```sql
CAST(<sql_variant type column> AS VARCHAR)
```
Note: Adding _--map-column-java_ argument to sqoop command will not work. Sqoop does not understand _SQL_VARIANT_ data type and will not convert it to String.

#### Example:

```sql
CREATE TABLE main_db.dbo.test_variant
(
   id        INT,
   var_item  SQL_VARIANT,
   name      VARCHAR(20),
   uniq      UNIQUEIDENTIFIER
);

INSERT INTO test_variant
SELECT 1, 'Sam', 'String', NEWID();

INSERT INTO  test_variant
SELECT 2, 345.678, 'Float', NEWID();

INSERT INTO  test_variant
SELECT 3, 20, 'Integer', NEWID();
```
This will not work:
```sh
sqoop import ... --map-column-java var_item=String 
```
This will work:
```sh
sqoop import ... --query 'SELECT CAST(var_item AS VARCHAR) AS var_item_str FROM test_variant'
```