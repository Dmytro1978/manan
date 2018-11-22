
--Convert XML data to XMLTYPE and then convert to string
with sq1 as 
(
    select 
        xmltype('
            <note> 
                <to>Tove</to> 
                <from>Jani</from> 
                <heading>Reminder</heading> 
                <body>Don''t forget me this weekend!</body> 
            </note>
        ') as xml_body
    from dual
)
select t.xml_body.GetStringVal() as xml_body from sq1 t;

-- Create a table with XMLTYPE data type 
CREATE TABLE XML_TEST
(
    ID NUMBER(10),
    NAME VARCHAR2(200),
    XML_BODY XMLTYPE
);

-- Insert XML data into the tables
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

-- Select data and convert XMLTYPE data type to string
select t.id, t.name, t.xml_body.getStringVal() xml_body from xml_test t;