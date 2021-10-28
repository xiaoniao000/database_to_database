# -*-coding:utf-8-*-
from xyDB.connect.closeConnect import closeconn
from xyDB.connect.pgsql_getConnect import getpgconn

conn, cur = getpgconn()

pg_sql = """select qs_reference."id",qs_reference.question_id,qs_reference.ref_base_id,qs_reference.ref_question_id
            from qs_reference"""

# pg_sql2 = """insert into qs_reference(question_id,ref_base_id,ref_question_id)
#             values(%s, %s, %s) RETURNING ID INTO "id";"""

pg_sql3 = """insert into qs_reference(id,question_id,ref_base_id,ref_question_id)
            values(%s, %s, %s, %s) RETURNING "id";"""

pg_delete = """delete from qs_reference where qs_reference."id"=%s"""

# pg_nextval = """SELECT nextval('person_id_seq');"""
pg_nextval = """SELECT nextval('qs_question_pkey');"""


cur.execute(pg_nextval)
results = cur.fetchall()
print(results[0][0])


# insert
# cur.execute(pg_sql3, (0, 0, 0))
# # 提交执行
# re = conn.commit()
# print(re[0][0])

# for i in range(0, 4):
#     cur.execute(pg_nextval)
#     results = cur.fetchall()
#     cur.execute(pg_sql3, (results[0][0], i, i, i))
#
#     # print(re[0][0])
#     cur.execute(pg_sql)
#     results = cur.fetchall()
#     print(results)
#
# re = conn.commit()

# selete
# cur.execute(pg_sql)
# results = cur.fetchall()
# print(results)

# delete
# cur.execute(pg_delete, '10')
# # 提交执行
# re = conn.commit()

# 关闭连接
closeconn(conn, cur)
