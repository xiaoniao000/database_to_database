# -*-coding:utf-8-*-

# pg_sql = """INSERT INTO qs_question (id, store_id, user_id, title, type, score)
#         VALUES (%s, %s, %s, %s, %s, %s, %s);"""

# pg_sql1 = """INSERT INTO qs_question_option (id, correct, correct_value, question_id)
#         VALUES (%s, %s, %s, %s, %s, %s, %s);"""

sql1 = """select count(*) from t
                where t.q_id= %s """

my_sql2 = """select t.t_id,t.q_id,t.t_input,t.t_output,t.score 
            from t
            where t.q_id= %s """

pg_sql1 = """INSERT INTO qs_question_option (id, correct, correct_value, question_id, score)
        VALUES (%s, %s, %s, %s, %s);"""

pg_sql = """INSERT INTO qs_question (id, store_id, user_id, title, type, score)
        VALUES (%s, %s, %s, %s, %s, %s);"""


# <p>一个有N个元素的集合有2^N个不同子集（包含空集），现在要在这2^N个集合中取出若干集合（至少一个），
# 使得它们的交集的元素个数为K，求取法的方案数，答案模1000000007。</p>


# <p>输入描述:</p><p>输入一行两个整数N，K。</p><p>输入样例:</p><p>3 2</p>

# <p>输出描述:</p><p>输出一个整数表示答案。</p><p>输出样例:</p><p>6</p>


# def biancheng(pg_sql, pg_sql1, pg_cur, pg_conn, my_count, pg_count, q_id, q_content, des, score, t_id):

# count_sql = SELECT COUNT(*)
#             FROM t
#             WHERE t.q_id=%s;

# select_sql2 = SELECT t.t_id,q.q_id,t.t_input,t.t_output,t.score
#               FROM t
#               WHERE t.q_id=%s;

def biancheng(my_cur, pg_cur, pg_conn, pg_count, q_id, q_content, score, count_sql, select_sql2):
    my_cur.execute(count_sql % q_id)
    my_count = my_cur.fetchall()
    my_count = my_count[0][0]

    my_cur.execute(select_sql2 % q_id)
    results = my_cur.fetchall()

    if pg_count == 0:
        pg_cur.execute(pg_sql, (q_id, 0, 0, q_content, 10, score))
        if my_count == 1:
            for result in results:
                result = list(result)
                t_id = result[0]
                q_id = result[1]
                t_input = result[2]
                t_output = result[3]
                score = result[4]

                des = {'t_input': t_input, 't_output': t_output}

                pg_cur.execute(pg_sql1, (t_id, 2, str(des), q_id, score))

                pg_conn.commit()
                print("*************11111*********")
                # print('t_id:' + str(t_id) + '\t' + 'q_id:' + str(q_id) + '\t' + 't_input:' + str(t_input) + '\t' +
                #       't_output:' + str(t_output) + '\t' + 'score:' + str(score) + '\n')
        elif my_count > 1:
            for result in results:
                result = list(result)
                t_id = result[0]
                q_id = result[1]
                t_input = result[2]
                t_output = result[3]
                score = result[4]

                des = {'t_input': t_input, 't_output': t_output}

                pg_cur.execute(pg_sql1, (t_id, 2, str(des), q_id, score))

                pg_conn.commit()
                print("**************25343262547**********")
                # print('t_id:' + str(t_id) + '\t' + 'q_id:' + str(q_id) + '\t' + 't_input:' + str(t_input) + '\t' +
                #       't_output:' + str(t_output) + '\t' + 'score:' + str(score) + '\n')

    elif pg_count > 0:
        print("已有本条数据")
    else:
        print("插入失败")


# select_sql = SELECT problem.test_case_id,problem.id,problem.input_description,
#                       problem.output_description,problem.total_score
#              FROM problem
#              WHERE problem.id=%s;

# count_sql = SELECT COUNT(*) FROM problem WHERE problem.id=%s;

def biancheng1(my_cur, pg_cur, pg_conn, pg_count, q_id, q_content, score, count_sql, select_sql):
    my_cur.execute(count_sql % q_id)
    my_count = my_cur.fetchall()
    my_count = my_count[0][0]

    my_cur.execute(select_sql % q_id)
    results = my_cur.fetchall()

    if pg_count == 0:
        pg_cur.execute(pg_sql, (q_id, 0, 0, q_content, 10, score))
        if my_count == 1:
            for result in results:
                result = list(result)

                t_id = result[0]
                q_id = result[1]
                t_input = result[2]
                t_output = result[3]
                score = result[4]
                des = {'t_input': t_input, 't_output': t_output}

                pg_cur.execute(pg_sql1, (t_id, 2, str(des), q_id, score))

                pg_conn.commit()
                print("*************11111*********")
                # print('t_id:' + str(t_id) + '\t' + 'q_id:' + str(q_id) + '\t' + 't_input:' + str(t_input) + '\t' +
                #       't_output:' + str(t_output) + '\t' + 'score:' + str(score) + '\n')
        elif my_count > 1:
            for result in results:
                result = list(result)

                t_id = result[0]
                q_id = result[1]
                t_input = result[2]
                t_output = result[3]
                score = result[4]

                des = {'t_input': t_input, 't_output': t_output}

                pg_cur.execute(pg_sql1, (t_id, 2, str(des), q_id, score))

                pg_conn.commit()
                print("**************25343262547**********")
                # print('t_id:' + str(t_id) + '\t' + 'q_id:' + str(q_id) + '\t' + 't_input:' + str(t_input) + '\t' +
                #       't_output:' + str(t_output) + '\t' + 'score:' + str(score) + '\n')

    elif pg_count > 0:
        print("已有本条数据")
    else:
        print("插入失败")
