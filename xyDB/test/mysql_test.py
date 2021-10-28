# -*-coding:utf-8-*-

# 定义sql语句
# sql = """SELECT q.q_id,q.q_content,q.q_type,q.score, a2.b FROM exam.q q,exam.a2 a2 WHERE q.q_id=a2.q_id GROUP BY q.q_type;"""
from xyDB.connect.closeConnect import closeconn
from xyDB.connect.getConnect import getconn

sql = """SELECT q.q_id,q.q_content,q.q_type,q.score, a2.b 
        FROM exam.q q,exam.a2 a2 
        WHERE q.q_id=a2.q_id;"""

sql2 = """select count(*) from exam.a3 a3
                where a3.q_id= %s """

sql3 = """select  q.q_id,q.q_content,q.q_type,q.score,t.t_input,t.t_output,t.t_id
            from exam.q q,exam.t t
            where q.q_id=t.q_id"""

def conndb():
    # 获取连接
    # conn, cur = getconn()
    # exam 3306 root root
    # def getconn(port=3306, user="root", passwd="root", db="exam"):
    conn, cur = getconn(port=3306, user='root', passwd='root', db='exam')

    # 使用 execute()  方法执行 SQL 查询
    # cur.execute(sql2, 630)
    cur.execute(sql3)
    results = cur.fetchall()  # 元组 元组长度是sql查询的结果条数

    for result in results:
        # print(result)
        # result = str(result)
        result = list(result)
        # print(type(result))
        # print(len(result))
        # result = str(list(result))
        # print(result)
        # result = result.split(',')
        q_id = result[0]
        q_content = result[1]
        q_type = result[2]
        score = result[3]
        t_input = result[4]
        t_output = result[5]
        des = {'t_input': t_input, 't_output': t_output}
        t_id = result[6]
        print('q_id:' + str(q_id) + '\t' + 'q_content:' + str(q_content) + '\t' +
              'q_type:' + str(q_type) + '\t' + 'score:' + str(score) + '\t' +
              't_input:' + str(t_input) + '\t' + 't_output:' + str(t_output) + '\t' + 't_id:' + str(t_id) + '\n')
        print(des)
    closeconn(conn, cur)


print("开始调用函数")
# 调用函数
conndb()
