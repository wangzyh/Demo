# 数据库

## MySQL
1. 主从复制(Master-Slave)<br/>
    Mysql的复制 Replication 是一个异步的复制过程,从一个 Mysql instace(我们称之为 Master)复制到另一个 Mysql instance(我们称之 Slave)。
    在 Master 与 Slave 之间的实现整个复制过程主要由三个线程来完成,其中两个线程(Sql线程和IO线程)在 Slave 端,另外一个线程(IO线程)在 Master 端。
2. myisam 和 innodb的区别
    1. myisam引擎是5.1版本之前的默认引擎，支持全文检索、压缩、空间函数等，但是不支持事务和行级锁，
       所以一般用于有大量查询少量插入的场景来使用，而且myisam不支持外键，并且索引和数据是分开存储的。 
    2. innodb是基于聚簇索引建立的，和myisam相反它支持事务、外键，并且通过MVCC来支持高并发，索引和数据存储在一起。
3. 幂等性: 分布式环境下常见问题, 多次操作, 结果一致.
