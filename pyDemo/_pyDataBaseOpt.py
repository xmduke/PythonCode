#!/usr/bin/env python3
#使用python连接MySql数据库

#0.导入模块
import mysql.connector

#1.连接数据库
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123456',
    'port':'3306',
    'database':'Test',
    'charset':'utf8'
}

conn = mysql.connector.connect(**config)

#方法2：
#conn = mysql.connector.connect(user = 'root',
#  password = '123456',
#  database = 'Test')


#2.SQL操作

try:
    #设置游标
    cursor = conn.cursor()

    #创建表
    cursor.execute('drop table if EXISTS test;')
    cursor.execute('create table test(id int primary key, name varchar(20))')

    #插入记录
    cursor.execute('insert into test(id, name) values(%s, %s)', (1, 'y0n'))
    print('rowcount = ', cursor.rowcount)

    #提交事务
    conn.commit()
    cursor.close()

    #查询
    cursor = conn.cursor()
    cursor.execute('select * from test where id = %s', ('1',))
    values = cursor.fetchall()
    print(values)

except:
    #发生错误时回滚
    conn.rollback()

#3.关闭连接
cursor.close()
conn.close()

