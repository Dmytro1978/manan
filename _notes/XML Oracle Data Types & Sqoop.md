# XML Oracle Data Types & Sqoop

Sqoop does not work directly with Oracle XMLTYPE data type. You need to convert 
XMLTYPE data type to String. 

First, create a table:

```sql
create table xml_test
(
    id number(18),
    name varchar2(200),
    xml_body xmltype
)
```
Insert a couple of records with XML data into the table:

Record 1

```sql
insert into xml_test
select 
    1, 
    'Sam', 
    xmltype('
        <note> 
            <to>Tove</to> 
            <from>Jani</from> 
            <heading>Reminder</heading> 
            <body>Don''t forget me this weekend!</body> 
        </note>
    ')
from dual;
```

Record 2

```sql
insert into xml_test
select 
    2, 
    'Jani', 
    xmltype('
        <breakfast_menu> 
        <food> 
            <name>Belgian Waffles</name> 
            <price>$5.95</price> 
            <description>Two of our famous Belgian Waffles with plenty of real maple syrup</description> 
            <calories>650</calories> </food> 
        <food> 
            <name>Strawberry Belgian Waffles</name> 
            <price>$7.95</price> 
            <description>Light Belgian waffles covered with strawberries and whipped cream</description> 
            <calories>900</calories> </food> 
        <food> 
            <name>Berry-Berry Belgian Waffles</name> 
            <price>$8.95</price> 
            <description>Light Belgian waffles covered with an assortment of fresh berries and whipped cream</description> 
            <calories>900</calories> </food> 
        <food> 
            <name>French Toast</name> 
            <price>$4.50</price> 
            <description>Thick slices made from our homemade sourdough bread</description> 
            <calories>600</calories> </food> 
        <food> 
            <name>Homestyle Breakfast</name> 
            <price>$6.95</price> 
            <description>Two eggs, bacon or sausage, toast, and our ever-popular hash browns</description> 
            <calories>950</calories> </food> 
        </breakfast_menu>
    ')
from dual;

commit;
```

Then use Oracle _getStringVal()_ function in Sqoop SQL query:
```sh
--query 'select t.id, t.name, t.xml_body.getStringVal() as xml_body from xml_test t'
```

Another approach is to convert XMLTYPE data type to CLOB and then use Sqoop column mapping parameter to convert CLOB to string in Sqoop command.

Use following sqoop parameters:
```sh
--map-column-java XML_BODY=String 
--query 'select t.id, t.name, t.xml_body.getCLOBVal() as xml_body from xml_test t'
