# -*-coding:utf-8-*-

# sql1 = """select count(*) from exam.a3 a3
#                 where a3.q_id= %s """

my_sql3 = """select sum(o.checked)
            FROM exam.o o
            where o.q_id=%s"""

my_sql2 = """select o.o_id,o.o_content,o.o_number,o.checked
            from exam.o o
            where o.q_id=%s;"""

pg_sql = """INSERT INTO qs_question (id, store_id, user_id, title, type, score, option_sort)
            VALUES (%s, %s, %s, %s, %s, %s, %s);"""

pg_sql1 = """INSERT INTO qs_question_option (id, correct, correct_value, question_id, score)
            VALUES (%s, %s, %s, %s, %s);"""


def xuanze1(scur, xycur, xycon, pg_count, q_id, q_content, score, count_sql, select_sql2):
    scur.execute(count_sql % q_id)
    many_c = scur.fetchall()
    many_c = many_c[0][0]

    scur.execute(select_sql2 % q_id)
    results = scur.fetchall()

    if pg_count == 0:
        if many_c == 1:
            option_sort = []
            for result in results:
                result = list(result)
                o_id = result[0]
                o_content = result[1]
                o_number = result[2]
                checked = result[3]
                checked = int.from_bytes(checked, byteorder='big', signed=False)

                option_sort.append(o_number)
                id = str(q_id) + str(o_id)

                if 5 == len(result):
                    a_score = result[4]
                    xycur.execute(pg_sql1, (id, checked + 1, o_content, q_id, a_score))
                else:
                    xycur.execute(pg_sql1, (id, checked + 1, o_content, q_id, 0))
                xycon.commit()

                print("*************11111*********")
            xycur.execute(pg_sql, (q_id, 0, 0, q_content, 1, score, str(option_sort)))
            xycon.commit()

        elif many_c > 1:
            option_sort = []
            for result in results:
                result = list(result)
                o_id = result[0]
                o_content = result[1]
                o_number = result[2]
                checked = result[3]
                checked = int.from_bytes(checked, byteorder='big', signed=False)

                option_sort.append(o_number)
                id = str(q_id) + str(o_id)

                if 5 == len(result):
                    a_score = result[4]
                    xycur.execute(pg_sql1, (id, checked + 1, o_content, q_id, a_score))
                else:
                    xycur.execute(pg_sql1, (id, checked + 1, o_content, q_id, 0))
                xycon.commit()

                print("**************25343262547**********")
            xycur.execute(pg_sql, (q_id, 0, 0, q_content, 2, score, str(option_sort)))
            xycon.commit()

    elif pg_count > 0:
        print("已有本条数据")
    else:
        print("插入失败")


def xuanze2(scur, xycur, xycon, pg_count, q_id, q_content, score, count_sql, select_sql2):
    scur.execute(count_sql % q_id)
    many_c = scur.fetchall()
    many_c = many_c[0][0]

    scur.execute(select_sql2 % q_id)
    results = scur.fetchall()

    if pg_count == 0:
        if many_c == 1:
            option_sort = []
            for result in results:
                result = list(result)
                o_id = result[0]
                o_content = result[1]
                o_number = result[2]
                checked = result[3]
                checked = int.from_bytes(checked, byteorder='big', signed=False)

                option_sort.append(o_number)
                id = str(q_id) + str(o_id)

                if 5 == len(result):
                    a_score = result[4]
                    xycur.execute(pg_sql1, (id, checked + 1, o_content, q_id, a_score))
                else:
                    xycur.execute(pg_sql1, (id, checked + 1, o_content, q_id, 0))
                xycon.commit()

                print("*************11111*********")
            xycur.execute(pg_sql, (q_id, 0, 0, q_content, 1, score, str(option_sort)))
            xycon.commit()

        elif many_c > 1:
            option_sort = []
            for result in results:
                result = list(result)
                o_id = result[0]
                o_content = result[1]
                o_number = result[2]
                checked = result[3]
                checked = int.from_bytes(checked, byteorder='big', signed=False)

                option_sort.append(o_number)
                id = str(q_id) + str(o_id)

                if 5 == len(result):
                    a_score = result[4]
                    xycur.execute(pg_sql1, (id, checked + 1, o_content, q_id, a_score))
                else:
                    xycur.execute(pg_sql1, (id, checked + 1, o_content, q_id, 0))
                xycon.commit()

                print("**************25343262547**********")
            xycur.execute(pg_sql, (q_id, 0, 0, q_content, 2, score, str(option_sort)))
            xycon.commit()

    elif pg_count > 0:
        print("已有本条数据")
    else:
        print("插入失败")
