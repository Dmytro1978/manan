# XML Oracle Data Types & Sqoop

Sqoop does not work directly with Oracle XMLTYPE data type. You need to convert 
XMLTYPE data type to String. 

```sql
create table xml_test
(
    id number(18),
    name varchar2(200),
    xml_body xmltype
)
```

Use following sqoop parameters:
```sh
--query 'select t.id, t.name, t.xml_body.getStringVal() as xml_body from xml_test t'
```

Another approach is to convert XMLTYPE data type to CLOB and then use column mapping to convert CLOB to string in Sqoop command.

Use following sqoop parameters:
```sh
--map-column-java XML_BODY=String 
--query 'select t.id, t.name, t.xml_body.getCLOBVal() as xml_body from xml_test t'
