# -*-coding:utf-8-*-
from multiprocessing import Lock

sql1 = """select count(*) from exam.a3 a3
                where a3.q_id= %s """

my_sql2 = """select a3.a_id,a3.q_id,a3.a_content 
            from exam.a3 a3
            where a3.q_id=%s"""

pg_sql = """INSERT INTO qs_question (id, store_id, user_id, title, type, score)
        VALUES (%s, %s, %s, %s, %s, %s);"""

pg_sql2 = """INSERT INTO qs_question_option (id, correct, correct_value, question_id, score)
        VALUES (%s, %s, %s, %s, %s);"""


# count_sql = SELECT COUNT(*) FROM test WHERE test.test_id=%s;

# select_sql2 = SELECT test.o_id,test.test_value FROM test WHERE test.test_id=%s;
# select_sql2 = SELECT test.o_id,test.test_value,test.t_score FROM test WHERE test.test_id=%s;

def tiankong1(my_cur, pg_cur, pg_conn, pg_count, q_id, q_content, score, count_sql, select_sql2):
    my_cur.execute(count_sql % q_id)
    my_count = my_cur.fetchall()
    my_count = my_count[0][0]

    my_cur.execute(select_sql2 % q_id)
    results = my_cur.fetchall()

    if pg_count == 0:
        if my_count == 1:
            pg_cur.execute(pg_sql, (q_id, 0, 0, q_content, 3, score))
            for result in results:
                result = list(result)
                a_id = result[0]
                a_content = result[1]
                id = str(a_id) + str(q_id)
                if 2 == len(result):
                    # print("a_id:" + str(a_id) + '\t' + "a_content:" + str(a_content) + '\t' + "id:" + id + '\n')
                    pg_cur.execute(pg_sql2, (id, 2, a_content, q_id, 0))
                elif 3 == len(result):
                    a_score = result[2]
                    # print("a_id:" + str(a_id) + '\t' + "a_content:" + str(a_content) + '\t' +
                    #       "id:" + id + '\t' + "a_score:" + a_score + '\n')
                    pg_cur.execute(pg_sql2, (id, 2, a_content, q_id, a_score))

                pg_conn.commit()
                print("*************11111*********")

        elif my_count > 1:
            pg_cur.execute(pg_sql, (q_id, 0, 0, q_content, 4, score))
            for result in results:
                result = list(result)
                a_id = result[0]
                a_content = result[1]
                id = str(a_id) + str(q_id)
                if 2 == len(result):
                    # print("a_id:" + str(a_id) + '\t' + "a_content:" + str(a_content) + '\t' + "id:" + id + '\n')
                    pg_cur.execute(pg_sql2, (id, 2, a_content, q_id, 0))
                elif 3 == len(result):
                    a_score = result[2]
                    # print("a_id:" + str(a_id) + '\t' + "a_content:" + str(a_content) + '\t' +
                    #       "id:" + id + '\t' + "a_score:" + a_score + '\n')
                    pg_cur.execute(pg_sql2, (id, 2, a_content, q_id, a_score))

                pg_conn.commit()
                print("**************25343262547**********")

    elif pg_count > 0:
        print("已有本条数据")
        print(q_id)
    else:
        print("插入失败")


# count_sql = SELECT COUNT(*) FROM a3 WHERE a3.q_id=%s;
#
# select_sql2 = SELECT a3.a_id,a3.a_content FROM a3 WHERE a3.q_id=%s;

def tiankong2(my_cur, pg_cur, pg_conn, pg_count, q_id, q_content, score, count_sql, select_sql2):
    my_cur.execute(count_sql % q_id)
    my_count = my_cur.fetchall()
    my_count = my_count[0][0]

    my_cur.execute(select_sql2 % q_id)
    results = my_cur.fetchall()

    if pg_count == 0:
        if my_count == 1:
            pg_cur.execute(pg_sql, (q_id, 0, 0, q_content, 3, score))
            for result in results:
                result = list(result)
                a_id = result[0]
                a_content = result[1]
                id = str(a_id) + str(q_id)
                if 2 == len(result):
                    # print("a_id:" + str(a_id) + '\t' + "a_content:" + str(a_content) + '\t' + "id:" + id + '\n')
                    pg_cur.execute(pg_sql2, (id, 2, a_content, q_id, 0))
                elif 3 == len(result):
                    a_score = result[2]
                    # print("a_id:" + str(a_id) + '\t' + "a_content:" + str(a_content) + '\t' +
                    #       "id:" + id + '\t' + "a_score:" + a_score + '\n')
                    pg_cur.execute(pg_sql2, (id, 2, a_content, q_id, a_score))

                pg_conn.commit()
                print("*************11111*********")

        elif my_count > 1:
            pg_cur.execute(pg_sql, (q_id, 0, 0, q_content, 4, score))
            for result in results:
                result = list(result)
                a_id = result[0]
                a_content = result[1]
                id = str(a_id) + str(q_id)
                if 2 == len(result):
                    # print("a_id:" + str(a_id) + '\t' + "a_content:" + str(a_content) + '\t' + "id:" + id + '\n')
                    pg_cur.execute(pg_sql2, (id, 2, a_content, q_id, 0))
                elif 3 == len(result):
                    a_score = result[2]
                    # print("a_id:" + str(a_id) + '\t' + "a_content:" + str(a_content) + '\t' +
                    #       "id:" + id + '\t' + "a_score:" + a_score + '\n')
                    pg_cur.execute(pg_sql2, (id, 2, a_content, q_id, a_score))

                pg_conn.commit()
                print("**************25343262547**********")

    elif pg_count > 0:
        print("已有本条数据")
    else:
        print("插入失败")
