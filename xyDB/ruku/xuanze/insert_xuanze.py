# -*-coding:utf-8-*-
from xyDB.ruku.xuanze.xuanze import xuanze1, xuanze2

my_sql = """SELECT q.q_id,q.q_content,q.q_type,q.score,o.o_id,o.o_content,o.o_number,o.checked
            FROM exam.q q,exam.o o
            WHERE q.q_id=o.q_id"""

pg_sql1 = """select count(*) from qs_question
                where qs_question.id= %s """


def insert_xuanze1(scur, xycur, xycon, select_sql1, count_sql, select_sql2):
    # 使用 execute()  方法执行 SQL 查询
    scur.execute(select_sql1)
    results = scur.fetchall()  # 元组 元组长度是sql查询的结果条数

    for result in results:
        result = list(result)

        q_id = result[0]
        q_content = result[1]
        score = result[2]

        xycur.execute(pg_sql1 % q_id)
        pg_count = xycur.fetchall()  # postgres

        xuanze1(scur, xycur, xycon, pg_count[0][0], q_id, q_content, score, count_sql, select_sql2)


# count_sql = SELECT SUM(o.checked) FROM o WHERE o.q_id=%s;

# select_sql2 = SELECT o.o_id,o.o_content,o.o_number,o.checked FROM o WHERE o.q_id=%s;

def insert_xuanze2(scur, xycur, xycon, select_sql1, count_sql, select_sql2):
    # 使用 execute()  方法执行 SQL 查询
    scur.execute(select_sql1)
    results = scur.fetchall()  # 元组 元组长度是sql查询的结果条数

    for result in results:
        result = list(result)

        q_id = result[0]
        q_content = result[1]
        score = result[2]

        xycur.execute(pg_sql1 % q_id)
        pg_count = xycur.fetchall()  # postgres

        xuanze2(scur, xycur, xycon, pg_count[0][0], q_id, q_content, score, count_sql, select_sql2)
