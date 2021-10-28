# -*-coding:utf-8-*-
from xyDB.ruku.biancheng.biancheng import biancheng, biancheng1

select_sql = """select  q.q_id,q.q_content,q.q_type,q.score,t.t_input,t.t_output,t.t_id
            from exam.q q,exam.t t
            where q.q_id=t.q_id"""

pg_sql2 = """select count(*) from qs_question
                where qs_question.id= %s """


# SELECT problem.id,problem.description,problem.total_score,problem.input_description,
#        problem.output_description,problem.test_case_id
# FROM problem;

# select_sql1 = SELECT q.q_id,q.q_content,q.score,t.t_input,t.t_output
#               FROM q,t
#               WHERE q.q_id=t.q_id;


def insert_biancheng(scur, xycur, xycon, select_sql1, count_sql, select_sql2):
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

        biancheng(scur, xycur, xycon, pg_count[0][0], q_id, q_content, score, count_sql, select_sql2)


# select_sql = SELECT problem.id,problem.description,problem.total_score,problem.input_description,
#        problem.output_description,problem.test_case_id FROM problem;

# count_sql = SELECT COUNT(*) FROM problem WHERE problem.id=%s;

def insert_biancheng1(scur, xycur, xycon, select_sql, count_sql, select_sql2):
    # 使用 execute()  方法执行 SQL 查询
    scur.execute(select_sql)
    results = scur.fetchall()  # 元组 元组长度是sql查询的结果条数

    for result in results:
        result = list(result)

        q_id = result[0]
        q_content = result[1]
        score = result[2]

        xycur.execute(pg_sql2 % q_id)
        pg_count = xycur.fetchall()  # postgres

        print("#################################", q_id, type(q_id))

        biancheng1(scur, xycur, xycon, pg_count[0][0], q_id, q_content, score, count_sql, select_sql2)
