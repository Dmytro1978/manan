## How to restart AWS EMR Hive Metastore:

You can check the status, start and stop the **Hive metastore** using the following commands in EMR:

```sh
sudo initctl status hive-hcatalog-server # check the status

sudo initctl stop hive-hcatalog-server   # stop HCatalog

sudo initctl start hive-hcatalog-server  # start HCatalog
```

The logs for the hive metastore will be available at _/var/log/hive-hcatalog/_ in the master node.

## How to restart AWS EMR HiveServer2:

```sh
sudo initctl status hive-server2 # check the status

sudo initctl stop hive-server2   # stop HiveServer2

sudo initctl start hive-server2  # start HiveServer2
```

## Sizing Hadoop Heap Memory

### HADOOP_HEAPSIZE
*HADOOP_HEAPSIZE* sets the JVM heap size for all Hadoop project servers such as HDFS, YARN, and MapReduce. *HADOOP_HEAPSIZE* is an integer passed to the JVM as the maximum memory (Xmx) argument (for example, in */etc/hadoop/conf/hadoop-env.sh*):

```sh
export HADOOP_HEAPSIZE=2048
```

To configure the heap size for **HiveServer2** and **Hive metastore**, set the **-Xmx** parameter in the *HADOOP_OPTS* variable to the desired maximum heap size in the *hive-env.sh* advanced configuration snippet if you use Cloudera Manager or otherwise edit */etc/hive/conf/hive-env.sh*.

To configure the heap size for the **Beeline CLI**, set the *HADOOP_HEAPSIZE* environment variable in the *hive-env.sh* advanced configuration snippet if you use Cloudera Manager or otherwise edit */etc/hive/conf/hive-env.sh* before starting the **Beeline CLI**.



The following example shows a configuration with the following settings:
* HiveServer2 uses 12 GB heap
* Hive metastore uses 12 GB heap
* Hive clients use 2 GB heap

The settings to change are in bold. All of these lines are commented out (prefixed with a **#** character) by default. Uncomment the lines by removing the **#** character.

```sh
if [ "$SERVICE" = "cli" ]; then
  if [ -z "$DEBUG" ]; then
    export HADOOP_OPTS="$HADOOP_OPTS -XX:NewRatio=12 -Xmx12288m -Xms10m -XX:MaxHeapFreeRatio=40 -XX:MinHeapFreeRatio=15 -XX:+UseParNewGC -XX:-UseGCOverheadLimit"
  else
    export HADOOP_OPTS="$HADOOP_OPTS -XX:NewRatio=12 -Xmx12288m -Xms10m -XX:MaxHeapFreeRatio=40 -XX:MinHeapFreeRatio=15 -XX:-UseGCOverheadLimit"
  fi
fi

export HADOOP_HEAPSIZE=2048
```
