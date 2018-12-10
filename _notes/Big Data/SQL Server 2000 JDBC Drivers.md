## SQL Server 2000 JDBC drivers

### JDBC Driver
The Microsoft JDBC Driver for SQL Server is available to all SQL Server users at no additional charge from Microsoft. It provides access to SQL Server 2000-2016 from any Java application.

Required File(s):
```
sqljdbc4.jar
```
Default Driver Class:
```
com.microsoft.sqlserver.jdbc.SQLServerDriver
```
JDBC URL Format:
```sh
jdbc:sqlserver://<host>[:<port1433>];databaseName=<database>
```


### jTDS JDBC Driver
jTDS is an open source 100% pure Java (type 4) JDBC 3.0 driver for Microsoft SQL Server (6.5, 7, 2000-2016) and Sybase (10, 11, 12, 15).
Required File(s):
```
jtds-1.3.1.jar
```
Default Driver Class:
```
net.sourceforge.jtds.jdbc.Driver
```
JDBC URL Format:
```
jdbc:jtds:sqlserver://<host>[:<port>][/<database>] 
```

Examples:
```
jdbc:jtds:sqlserver://localhost:5000/myDB
jdbc:jtds:sqlserver://192.168.10.201:5000/SAMPLE
 ```

Example of Sqoop command that stores data in HDFS: 

```sh
sqoop import --connect "jdbc:jtds:sqlserver://10.133.53.43:1433/PowerView" --connection-manager org.apache.sqoop.manager.SQLServerManager --query 'select * from dbo.ptra where $CONDITIONS' --driver net.sourceforge.jtds.jdbc.Driver --username sgroup --password <password> --target-dir hdfs:///user/hive/warehouse/ptra --num-mappers 1
```

Example of Sqoop command that stores data in S3: 

```sh
sqoop import --connect "jdbc:jtds:sqlserver://10.133.53.43:1433/PowerView" --connection-manager org.apache.sqoop.manager.SQLServerManager --query 'select * from dbo.ptra where $CONDITIONS' --driver net.sourceforge.jtds.jdbc.Driver --username sgroup --password <password> --target-dir s3://dmytro-dw/staging/ptra --num-mappers 1
```

### SQL Server versions mapping

```
80 = SQL Server 2000    =  8.00.xxxx
90 = SQL Server 2005    =  9.00.xxxx
100 = SQL Server 2008    = 10.00.xxxx
105 = SQL Server 2008 R2 = 10.50.xxxx
110 = SQL Server 2012    = 11.00.xxxx
120 = SQL Server 2014    = 12.00.xxxx
130 = SQL Server 2016    = 13.00.xxxx
```