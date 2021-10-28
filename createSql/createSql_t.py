def selectSql_t1(request):
    table = request.POST.get('table')
    id = request.POST.get('id')
    title = request.POST.get('title')
    score = request.POST.get('score')
    value = request.POST.get('value')
    a_id = request.POST.get('a_id')
    a_score = request.POST.get('a_score')

    word_id = '' + table + '.' + id
    word_title = '' + table + '.' + title
    word_score = '' + table + '.' + score
    word_value = '' + table + '.' + value
    word_a_id = '' + table + '.' + a_id
    if "如无该字段，请忽略" == a_score:
        word_a_score = ""
    else:
        word_a_score = '' + table + '.' + a_score

    # my_sql = """SELECT DISTINCT q.q_id,q.q_content,q.score
    #             from exam.q q,exam.a3 a3
    #             WHERE q.q_id=a3.q_id"""
    #
    # sql1 = """select count(*) from exam.a3 a3
    #                 where a3.q_id= %s """
    #
    # my_sql2 = """select a3.a_id,a3.q_id,a3.a_content
    #             from exam.a3 a3
    #             where a3.q_id=%s"""

    select_sql = "SELECT " + word_id + "," + word_title + "," + word_score + " FROM " + table + ";"

    count_sql = "SELECT COUNT(*) FROM " + table + " WHERE " + word_id + "=%s;"

    if "" == word_a_score:
        select_sql2 = "SELECT " + word_a_id + "," + word_value + " FROM " + table + " WHERE " + word_id + "=%s;"
    else:
        select_sql2 = "SELECT " + word_a_id + "," + word_value + "," + word_a_score + \
                      " FROM " + table + " WHERE " + word_id + "=%s;"
    return select_sql, count_sql, select_sql2


def selectSql_t2(request):
    table1 = request.POST.get('table1')
    id1 = request.POST.get('id1')
    title1 = request.POST.get('title1')
    score1 = request.POST.get('score1')
    value1 = request.POST.get('input1')
    a_id1 = request.POST.get('a_id1')
    a_score1 = request.POST.get('a_score1')
    equal1 = request.POST.get("equal1")

    table2 = request.POST.get('table2')
    id2 = request.POST.get('id2')
    title2 = request.POST.get('title2')
    score2 = request.POST.get('score2')
    value2 = request.POST.get('value2')
    a_id2 = request.POST.get('a_id2')
    a_score2 = request.POST.get('a_score2')
    equal2 = request.POST.get("equal2")

    word_id = ('' + table1 + '.' + id1) if (id2 == "") else ('' + table2 + '.' + id2)
    word_title = ('' + table1 + '.' + title1) if (title2 == "") else ('' + table2 + '.' + title2)
    word_score = ('' + table1 + '.' + score1) if (score2 == "") else ('' + table2 + '.' + score2)
    word_value = ('' + table1 + '.' + value1) if (value2 == "") else ('' + table2 + '.' + value2)
    word_a_id = ('' + table1 + '.' + a_id1) if (a_id2 == "") else ('' + table2 + '.' + a_id2)
    if "如无该字段，请忽略" == a_score1 and "如无该字段，请忽略" == a_score2:
        word_a_score = ""
    else:
        word_a_score = ('' + table1 + '.' + a_score1) if (a_score2 == "") else ('' + table2 + '.' + a_score2)
    equal1 = '' + table1 + '.' + equal1
    equal2 = '' + table2 + '.' + equal2

    # my_sql = """SELECT DISTINCT q.q_id,q.q_content,q.score
    #             from exam.q q,exam.a3 a3
    #             WHERE q.q_id=a3.q_id"""
    #
    # sql1 = """select count(*) from exam.a3 a3
    #                 where a3.q_id= %s """
    #
    # my_sql2 = """select a3.a_id,a3.q_id,a3.a_content
    #             from exam.a3 a3
    #             where a3.q_id=%s"""

    select_sql = "SELECT " + word_id + "," + word_title + "," + word_score + \
                 " FROM " + table1 + "," + table2 + " WHERE " + equal1 + "=" + equal2 + ";"

    table = word_value.split('.', 1)
    table = table[0]
    id = equal2.split('.', 1)
    id = id[1]
    new_word_id = table + '.' + id

    count_sql = "SELECT COUNT(*) FROM " + table + " WHERE " + new_word_id + "=%s;"

    if "" == word_a_score:
        select_sql2 = "SELECT " + word_a_id + "," + word_value + " FROM " + table + " WHERE " + new_word_id + "=%s;"
    else:
        select_sql2 = "SELECT " + word_a_id + "," + word_value + "," + word_a_score + \
                      " FROM " + table + " WHERE " + new_word_id + "=%s;"

    return select_sql, count_sql, select_sql2
