# -*-coding:utf-8-*-


# 关闭数据库连接
def closeconn(conn, my_cur):
    my_cur.close()
    conn.close()
