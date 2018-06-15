#!/usr/bin/python3
# -*- coding: utf-8 -*-
import mysql.connector
# 连接数据库
# 1.数据库连接方式, mysql -u root -p 然后键入密码
# 2.create DATABASE test; 一定要记得加分号,不加分好表示持续操作.分号是结束
con = mysql.connector.connect(user='root',password='apple',database='test')
cursor = con.cursor()
# 创建一个user表
cursor.execute('create table usertest222 (id varchar(20) primary key, name varchar(20))')
# 插入一行记录,%s作为占位符
cursor.execute('insert into usertest222 (id,name) values (%s,%s)',['1','Micheal'])
cursor.rowcount
# 提交事物
con.commit()
# 关闭连接
cursor.close()
# 查询
cursor = con.cursor()
cursor.execute('select * from usertest222 where id = %s',('1',))
values = cursor.fetchall()
print (values)