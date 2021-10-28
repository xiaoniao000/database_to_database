def selectSql_x1(request):
    table = request.POST.get('table')
    id = request.POST.get('id')
    title = request.POST.get('title')
    score = request.POST.get('score')
    o_id = request.POST.get('o_id')
    o_content = request.POST.get('o_content')
    o_number = request.POST.get('o_number')
    checked = request.POST.get('checked')
    a_score = request.POST.get('a_score')

    word_id = '' + table + '.' + id
    word_title = '' + table + '.' + title
    word_score = '' + table + '.' + score
    word_o_id = '' + table + '.' + o_id
    word_o_content = '' + table + '.' + o_content
    word_o_number = '' + table + '.' + o_number
    word_checked = '' + table + '.' + checked
    if "如无该字段，请忽略" == a_score:
        word_a_score = ""
    else:
        word_a_score = '' + table + '.' + a_score

    # my_sql = """SELECT q.q_id,q.q_content,q.score
    #             FROM exam.q q,exam.o o
    #             WHERE q.q_id=o.q_id"""
    #
    # my_sql3 = """select sum(o.checked)
    #                 FROM exam.o o
    #                 where o.q_id=%s"""
    #
    # my_sql2 = """select o.o_id,o.o_content,o.o_number,o.checked
    #             from exam.o o
    #             where o.q_id=%s;"""

    select_sql = "SELECT " + word_id + "," + word_title + "," + word_score + " FROM " + table + ";"

    count_sql = "SELECT SUM(" + word_checked + ")" + " FROM " + table + " WHERE " + word_id + "=%s;"

    if "" == word_a_score:
        select_sql2 = "SELECT " + word_o_id + "," + word_o_content + "," + word_o_number + "," + word_checked + \
                      " FROM " + table + " WHERE " + word_id + "=%s;"
    else:
        select_sql2 = "SELECT " + word_o_id + "," + word_o_content + "," + word_o_number + "," + word_checked + "," + \
                      word_a_score + " FROM " + table + " WHERE " + word_id + "=%s;"
    return select_sql, count_sql, select_sql2


def selectSql_x2(request):
    table1 = request.POST.get('table1')
    id1 = request.POST.get('id1')
    title1 = request.POST.get('title1')
    score1 = request.POST.get('score1')
    o_id1 = request.POST.get('o_id1')
    o_content1 = request.POST.get('o_content1')
    o_number1 = request.POST.get('o_number1')
    checked1 = request.POST.get('checked1')
    a_score1 = request.POST.get('a_score1')
    equal1 = request.POST.get("equal1")

    table2 = request.POST.get('table2')
    id2 = request.POST.get('id2')
    title2 = request.POST.get('title2')
    score2 = request.POST.get('score2')
    o_id2 = request.POST.get('o_id2')
    o_content2 = request.POST.get('o_content2')
    o_number2 = request.POST.get('o_number2')
    checked2 = request.POST.get('checked2')
    a_score2 = request.POST.get('a_score2')
    equal2 = request.POST.get("equal2")

    word_id = ('' + table1 + '.' + id1) if (id2 == "") else ('' + table2 + '.' + id2)
    word_title = ('' + table1 + '.' + title1) if (title2 == "") else ('' + table2 + '.' + title2)
    word_score = ('' + table1 + '.' + score1) if (score2 == "") else ('' + table2 + '.' + score2)
    word_o_id = ('' + table1 + '.' + o_id1) if (o_id2 == "") else ('' + table2 + '.' + o_id2)
    word_o_content = ('' + table1 + '.' + o_content1) if (o_content2 == "") else ('' + table2 + '.' + o_content2)
    word_o_number = ('' + table1 + '.' + o_number1) if (o_number2 == "") else ('' + table2 + '.' + o_number2)
    word_checked = ('' + table1 + '.' + checked1) if (checked2 == "") else ('' + table2 + '.' + checked2)
    if "如无该字段，请忽略" == a_score1 and "如无该字段，请忽略" == a_score2:
        word_a_score = ""
    else:
        word_a_score = ('' + table1 + '.' + a_score1) if (a_score2 == "") else ('' + table2 + '.' + a_score2)
    equal1 = '' + table1 + '.' + equal1
    equal2 = '' + table2 + '.' + equal2

    # my_sql = """SELECT q.q_id,q.q_content,q.score
    #             FROM exam.q q,exam.o o
    #             WHERE q.q_id=o.q_id"""
    #
    # my_sql3 = """select sum(o.checked)
    #                 FROM exam.o o
    #                 where o.q_id=%s"""
    #
    # my_sql2 = """select o.o_id,o.o_content,o.o_number,o.checked
    #             from exam.o o
    #             where o.q_id=%s;"""

    # SELECT q.q_id,q.q_content,q.score
    # FROM q,o
    # WHERE q.q_id=o.q_id;

    # SELECT SUM(o.checked) FROM o WHERE o.q_id=%s;

    # SELECT o.o_id,o.o_content,o.o_number,o.checked
    # FROM o
    # WHERE o.q_id=%s;

    select_sql = "SELECT " + word_id + "," + word_title + "," + word_score + \
                 " FROM " + table1 + "," + table2 + " WHERE " + equal1 + "=" + equal2 + ";"

    table = equal2.split('.', 1)
    table = table[0]

    count_sql = "SELECT SUM(" + word_checked + ")" + " FROM " + table + " WHERE " + equal2 + "=%s;"

    if "" == word_a_score:
        select_sql2 = "SELECT " + word_o_id + "," + word_o_content + "," + word_o_number + "," + word_checked + \
                      " FROM " + table + " WHERE " + equal2 + "=%s;"
    else:
        select_sql2 = "SELECT " + word_o_id + "," + word_o_content + "," + word_o_number + "," + word_checked + "," + \
                      word_a_score + " FROM " + table + " WHERE " + equal2 + "=%s;"

    return select_sql, count_sql, select_sql2
