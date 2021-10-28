# -*-coding:utf-8-*-
from xyDB.ruku.panduan.panduan import panduan1, panduan2

# my_sql = """SELECT q.q_id,q.q_content,q.score,a2.b,a2.a_id
#             FROM exam.q q,exam.a2 a2
#             WHERE q.q_id=a2.q_id"""

pg_sql2 = """select count(*) from qs_question
                where qs_question.id= %s """


def insert_panduan1(scur, xycur, xycon, select_sql1, select_sql2):
    # 使用 execute()  方法执行 SQL 查询
    scur.execute(select_sql1)
    results = scur.fetchall()  # 元组 元组长度是sql查询的结果条数

    for result in results:
        result = list(result)

        q_id = result[0]
        q_content = result[1]
        score = result[2]

        xycur.execute(pg_sql2 % q_id)
        pg_count = xycur.fetchall()  # postgres

        panduan1(scur, xycur, xycon, pg_count[0][0], q_id, q_content, score, select_sql2)


def insert_panduan2(scur, xycur, xycon, select_sql1, select_sql2):
    # 使用 execute()  方法执行 SQL 查询
    scur.execute(select_sql1)
    results = scur.fetchall()  # 元组 元组长度是sql查询的结果条数

    for result in results:
        result = list(result)

        q_id = result[0]
        q_content = result[1]
        score = result[2]

        xycur.execute(pg_sql2 % q_id)
        pg_count = xycur.fetchall()  # postgres

        panduan2(scur, xycur, xycon, pg_count[0][0], q_id, q_content, score, select_sql2)
