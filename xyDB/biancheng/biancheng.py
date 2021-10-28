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

def biancheng(my_cur, pg_cur, pg_conn, pg_count, q_id, q_content, score, t_id):
    my_cur.execute(sql1 % q_id)
    my_count = my_cur.fetchall()
    my_count = my_count[0][0]

    my_cur.execute(my_sql2 % q_id)
    results = my_cur.fetchall()

    if pg_count == 0:
        pg_cur.execute(pg_sql, (q_id, 0, 0, q_content, 10, score))
        if my_count == 1:
            for result in results:
                # t.t_id,t.q_id,t.t_input,t.t_output,t.score
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
                # print('q_id:' + str(id) + '\t' + 'q_content:' + str(q_content) + '\t' +
                #       'score:' + str(score) + '\t' + 'a_content:' + str(des) + '\n')
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

    elif pg_count > 0:
        print("已有本条数据")
    else:
        print("插入失败")
