#!/usr/bin/env python

# this code parses an sql statement and retrieves table names

import sqlparse
from sqlparse.sql import IdentifierList, Identifier
from sqlparse.tokens import Keyword, DML


def is_subselect(parsed):
    if not parsed.is_group: 
        return False

    for item in parsed.tokens:
        if item.is_group:
            return is_subselect(item)
        elif item.ttype is DML and item.value.upper() == 'SELECT':
            return True
        
    return False


def extract_from_part(parsed):
    from_seen = False
    for item in parsed.tokens:
        #print '1: ' + item.value

        if from_seen or is_subselect(item):
            if is_subselect(item):
                #print '2: ' + item.value
                for x in extract_from_part(item):
                    #print 'yield 1:' + x.value
                    yield x
            #elif item.ttype is Keyword and item.value.upper()=='JOIN' or item.value.upper()=='INNER JOIN' or item.value.upper()=='LEFT JOIN' or item.value.upper()=='RIGHT JOIN' or item.value.upper()=='ON':
            elif item.ttype is Keyword and item.value.upper() in ['JOIN', 'INNER JOIN', 'LEFT JOIN', 'RIGHT JOIN', 'ON']:
                From_join=True
            elif item.ttype is Keyword and item.value.upper()=='UNION' or item.value.upper()=='UNION ALL' :
                from_seen=False
                
 
                
            elif item.ttype is Keyword:
                raise StopIteration
            else:
                #print 'yield2 : ' + item.value
                yield item
                
        elif item.ttype is Keyword and item.value.upper() == 'FROM':
            #print(item)
            from_seen = True


def extract_table_identifiers(token_stream):
    for item in token_stream:
        if isinstance(item, IdentifierList):
            for identifier in item.get_identifiers():
                yield identifier.get_name()
        elif isinstance(item, Identifier):
            yield item.value.split(' ')[0] 
            #yield item.get_name()
    
        elif item.ttype is Keyword:
            yield item.value


def extract_tables(in_sql):
    #print (sqlparse.parse(sql)[0])
    from_seen = False
    stream = extract_from_part(sqlparse.parse(in_sql)[0])
    #for v in stream:
    #    print v
    return list(extract_table_identifiers(stream))


if __name__ == '__main__':
    #sql = "select * from (select 1 from aaa as t1) as t2"

    sql1 = "select 1 from aaa as t1"
    sql2 = "select * from (select 1 from aaa as t1) as t2"

    sql3 = """
select * from 
(
select 1 from aaa as t1
union all 
select 2 from bbb as t2
union all
select 3 from ccc as t3
)
as t4
"""

    sql4 = """
SELECT  
b.ClientName,
a.TranID,
a.TranRemark1,
a.TranDateOfService,
a.TranPayment   
FROM
(select TranRemark1, TranID from TranDetail
union all
select TranRemark2, TranID from TranDetail
union all
select TranRemark3, TranID from TranDetail) as AAA
LEFT JOIN TranHeader as BBB ON 
b.TranID = a.TranID
;
"""

    sql5 = """

select * from (
select t1.name from table1 as t1
left join table2 as t2 on t1.ca = t2.ca
union all 
select t3.name from table3 as t3
left join table4 as t4 on t3.id = t4.id
union all
select t5.name from table5 as t5
left join table6 as t6 on t5.id = t6.id 
) as t7
"""

    sql6 = """

select t1.name from table1 as t1
left join table2 as t2 on t1.ca = t2.ca
union all 
select t3.name from table3 as t3
left join table4 as t4 on t3.id = t4.id
union all
select t5.name from table5 as t5
left join table6 as t6 on t5.id = t6.id 

"""
    sql7 = """

select * from (
select t1.name from table1 as t1
left join table2 as t2 on t1.ca = t2.ca
left join table4 as t4 on t3.id = t4.id
left join table6 as t6 on t5.id = t6.id 
) as t7
"""

    sql8 = """

select t1.name from table1 as t1
left join table2 as t2 on t1.ca = t2.ca
left join table4 as t4 on t3.id = t4.id
left join table6 as t6 on t5.id = t6.id 

"""

    sql9 = """

select * from (
select t1.name, t3.name from table1 as t1
left join (select t2.id, t2.name from table2 as t2 where id = 220) as t3
on t1.id = t3.id
union all 
select t3.name from table3 as t3
left join table4 as t4 on t3.id = t4.id
) as t5
"""


    print('Tables (sql1): {0}'.format(', '.join(extract_tables(sql1))))
    print('Tables (sql2): {0}'.format(', '.join(extract_tables(sql2))))
    print('Tables (sql3): {0}'.format(', '.join(extract_tables(sql3))))
    print('Tables (sql4): {0}'.format(', '.join(extract_tables(sql4))))
    print('Tables (sql5): {0}'.format(', '.join(extract_tables(sql5))))
    print('Tables (sql6): {0}'.format(', '.join(extract_tables(sql6))))
    print('Tables (sql7): {0}'.format(', '.join(extract_tables(sql7))))
    print('Tables (sql8): {0}'.format(', '.join(extract_tables(sql8))))
    print('Tables (sql9): {0}'.format(', '.join(extract_tables(sql9))))