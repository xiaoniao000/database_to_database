# -*-coding:utf-8-*-
from xyDB.biancheng.biancheng import biancheng
from xyDB.connect.closeConnect import closeconn


select_sql = """select  q.q_id,q.q_content,q.q_type,q.score,t.t_input,t.t_output,t.t_id
            from exam.q q,exam.t t
            where q.q_id=t.q_id"""

pg_sql2 = """select count(*) from qs_question
                where qs_question.id= %s """

# SELECT problem.id,problem.description,problem.total_score,problem.input_description,
#        problem.output_description,problem.test_case_id
# FROM problem;

def insert_biancheng(scon, scur, xycon, xycur, select_sql):
    # 使用 execute()  方法执行 SQL 查询
    scur.execute(select_sql)
    results = scur.fetchall()  # 元组 元组长度是sql查询的结果条数

    for result in results:
        result = list(result)

        q_id = result[0]
        q_content = result[1]
        score = result[2]
        t_input = result[3]
        t_output = result[4]
        t_id = result[5]

        des = {'t_input': t_input, 't_output': t_output}

        print('q_id:' + str(q_id) + '\t' + 'q_content:' + str(q_content) + '\t' +
              'score:' + str(score) + '\t' + 'a_content:' + str(des) + '\t' + "t_id:" + t_id + '\n')

        xycur.execute(pg_sql2 % q_id)
        pg_count = xycur.fetchall()  # postgres

        biancheng(scur, xycur, xycon, pg_count[0][0], q_id, q_content, score, t_id)

