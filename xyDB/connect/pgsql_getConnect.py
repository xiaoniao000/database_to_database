# -*-coding:utf-8-*-
import psycopg2


def getpgconn(database='postgres', user='postgres', password='root', port='5432'):
    # 打开数据库连接
    # conn = psycopg2.connect(database='postgres', user='postgres', password='root', port='5432')
    conn = psycopg2.connect(database=database, user=user, password=password, port=port)
    # exam 3306 root root
    # postgres 5432 root root

    # 使用 my_cursor() 方法创建一个游标对象 my_cursor
    cur = conn.cursor()
    print("连接postgres成功")

    return conn, cur
