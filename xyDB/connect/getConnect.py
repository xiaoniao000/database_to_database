# -*-coding:utf-8-*-
import pymysql


# 定义函数
# conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root", db="exam", charset='utf8')
# cur = conn.cursor()
# def getconn(host="127.0.0.1", port=3306, user="root", passwd="root", db="exam", charset='utf8'):
#     # 打开数据库连接
#     conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
#
#     # 使用 cursor() 方法创建一个游标对象 cursor
#     cur = conn.cursor()
#     return conn, cur

def getconn(port=3306, user="root", passwd="root", db="exam"):
    # 打开数据库连接
    conn = pymysql.connect(port=port, user=user, passwd=passwd, db=db)
    # exam 3306 root root
    # postgres 5432 root root

    # 使用 cursor() 方法创建一个游标对象 cursor
    cur = conn.cursor()
    print("连接mysql成功")
    return conn, cur
