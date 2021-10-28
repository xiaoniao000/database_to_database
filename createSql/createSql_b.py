def selectSql_b1(request):
    table = request.POST.get('table')
    id = request.POST.get('id')
    title = request.POST.get('title')
    score = request.POST.get('score')
    input = request.POST.get('input')
    output = request.POST.get('output')
    t_id = request.POST.get("t_id")

    word_id = '' + table + '.' + id
    word_title = '' + table + '.' + title
    word_score = '' + table + '.' + score
    word_input = '' + table + '.' + input
    word_output = '' + table + '.' + output
    word_t_id = '' + table + '.' + t_id

    select_sql = "SELECT " + word_id + "," + word_title + "," + word_score + "," + word_input + "," + \
                 word_output + "," + word_t_id + " FROM " + table + ";"

    count_sql = "SELECT COUNT(*) FROM " + table + " WHERE " + word_id + "=%s;"

    # my_sql2 = """select t.t_id,t.q_id,t.t_input,t.t_output,t.score
    #             from t
    #             where t.q_id= %s """

    # SELECT problem.id,problem.description,problem.total_score,problem.input_description,
    # problem.output_description,problem.test_case_id FROM problem;

    select_sql2 = "SELECT " + word_t_id + "," + word_id + "," + word_input + "," + word_output + "," + word_score + \
                  " FROM " + table + " WHERE " + word_id + "=%s;"

    return select_sql, count_sql, select_sql2


def selectSql_b2(request):
    table1 = request.POST.get('table1')
    id1 = request.POST.get('id1')
    title1 = request.POST.get('title1')
    score1 = request.POST.get('score1')
    input1 = request.POST.get('input1')
    output1 = request.POST.get('output1')
    t_id1 = request.POST.get("t_id1")
    equal1 = request.POST.get("equal1")
    t_score1 = request.POST.get("t_score1")

    table2 = request.POST.get('table2')
    id2 = request.POST.get('id2')
    title2 = request.POST.get('title2')
    score2 = request.POST.get('score2')
    input2 = request.POST.get('input2')
    output2 = request.POST.get('output2')
    t_id2 = request.POST.get("t_id2")
    equal2 = request.POST.get("equal2")
    t_score2 = request.POST.get("t_score2")

    word_id = ('' + table1 + '.' + id1) if (id2 == "") else ('' + table2 + '.' + id2)
    word_title = ('' + table1 + '.' + title1) if (title2 == "") else ('' + table2 + '.' + title2)
    word_score = ('' + table1 + '.' + score1) if (score2 == "") else ('' + table2 + '.' + score2)
    word_input = ('' + table1 + '.' + input1) if (input2 == "") else ('' + table2 + '.' + input2)
    word_output = ('' + table1 + '.' + output1) if (output2 == "") else ('' + table2 + '.' + output2)
    word_t_id = ('' + table1 + '.' + t_id1) if (t_id2 == "") else ('' + table2 + '.' + t_id2)
    t_score = ('' + table1 + '.' + t_score1) if (t_score2 == "") else ('' + table2 + '.' + t_score2)
    equal1 = '' + table1 + '.' + equal1
    equal2 = '' + table2 + '.' + equal2

    select_sql = "SELECT " + word_id + "," + word_title + "," + word_score + "," + word_input + "," + word_output + \
                 " FROM " + table1 + "," + table2 + " WHERE " + equal1 + "=" + equal2 + ";"

    table = word_input.split('.', 1)
    table = table[0]
    id = equal2.split('.', 1)
    id = id[1]
    new_word_id = table + '.' + id

    count_sql = "SELECT COUNT(*) FROM " + table + " WHERE " + new_word_id + "=%s;"

    select_sql2 = "SELECT " + word_t_id + "," + new_word_id + "," + word_input + "," + word_output + "," + t_score + \
                  " FROM " + table + " WHERE " + new_word_id + "=%s;"

    return select_sql, count_sql, select_sql2
