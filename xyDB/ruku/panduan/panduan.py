# -*-coding:utf-8-*-

my_sql2 = """SELECT a2.a_id,a2.b
            FROM exam.a2 a2
            WHERE a2.q_id=%s"""

pg_sql1 = """INSERT INTO qs_question_option (id, correct, question_id)
        VALUES (%s, %s, %s);"""

pg_sql = """INSERT INTO qs_question (id, store_id, user_id, title, type, score)
        VALUES (%s, %s, %s, %s, %s, %s);"""


def panduan1(scur, xycur, xycon, pg_count, q_id, q_content, score, select_sql2):
    scur.execute(select_sql2 % q_id)
    results = scur.fetchall()

    if pg_count == 0:
        xycur.execute(pg_sql, (q_id, 0, 0, q_content, 5, score))
        for result in results:
            result = list(result)
            a_id = result[0]
            b = result[1]

            xycur.execute(pg_sql1, (a_id, b + 1, q_id))
            xycon.commit()

            print("*************11111*********")

    elif pg_count > 0:
        print("已有本条数据")
        print(q_id)
    else:
        print("插入失败")


def panduan2(scur, xycur, xycon, pg_count, q_id, q_content, score, select_sql2):
    scur.execute(select_sql2 % q_id)
    results = scur.fetchall()

    if pg_count == 0:
        xycur.execute(pg_sql, (q_id, 0, 0, q_content, 5, score))
        for result in results:
            result = list(result)
            a_id = result[0]
            b = result[1]

            xycur.execute(pg_sql1, (a_id, b + 1, q_id))
            xycon.commit()

            print("*************11111*********")

    elif pg_count > 0:
        print("已有本条数据")
        print(q_id)
    else:
        print("插入失败")
