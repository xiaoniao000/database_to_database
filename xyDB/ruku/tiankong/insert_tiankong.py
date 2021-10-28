# -*-coding:utf-8-*-
from xyDB.ruku.tiankong.tiankong import tiankong1, tiankong2

my_sql = """SELECT DISTINCT q.q_id,q.q_content,q.q_type,q.score,a3.a_content,a3.a_id
            from exam.q q,exam.a3 a3
            WHERE q.q_id=a3.q_id"""

pg_sql1 = """select count(*) from qs_question
                where qs_question.id= %s """


# select_sql1 = SELECT test.test_id,test.test_titile,test.test_total
#               FROM test;

def insert_tiankong1(scur, xycur, xycon, select_sql1, count_sql, select_sql2):
    # 使用 execute()  方法执行 SQL 查询
    scur.execute(select_sql1)
    results = scur.fetchall()  # 元组 元组长度是sql查询的结果条数

    for result in results:
        result = list(result)
        q_id = result[0]
        q_content = result[1]
        score = result[2]
        # print("q_id:" + str(q_id) + '\t' + "q_content:" + str(q_content) + '\t' + "score:" + str(score) + '\n')

        xycur.execute(pg_sql1 % q_id)
        pg_count = xycur.fetchall()  # postgres

        tiankong1(scur, xycur, xycon, pg_count[0][0], q_id, q_content, score, count_sql, select_sql2)


# select_sql1 = SELECT q.q_id,q.q_content,q.score FROM q,o WHERE q.q_id=o.q_id;

def insert_tiankong2(scur, xycur, xycon, select_sql1, count_sql, select_sql2):
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

        tiankong2(scur, xycur, xycon, pg_count[0][0], q_id, q_content, score, count_sql, select_sql2)
