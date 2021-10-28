from django.http import HttpResponse
from django.shortcuts import render, redirect

from xyDB.connect.closeConnect import closeconn
from xyDB.connect.getConnect import getconn
from xyDB.connect.pgsql_getConnect import getpgconn

from createSql.createSql_b import selectSql_b1, selectSql_b2
from createSql.createSql_p import selectSql_p1, selectSql_p2
from createSql.createSql_t import selectSql_t1, selectSql_t2
from createSql.createSql_x import selectSql_x1, selectSql_x2

from xyDB.ruku.biancheng.insert_biancheng import insert_biancheng, insert_biancheng1
from xyDB.ruku.panduan.insert_panduan import insert_panduan1, insert_panduan2
from xyDB.ruku.tiankong.insert_tiankong import insert_tiankong1, insert_tiankong2
from xyDB.ruku.xuanze.insert_xuanze import insert_xuanze1, insert_xuanze2
from xyDB.ruku.xuanze.get_all_data import get_all_tables, get_all_ziduanming
from xyDB.test.testCon import testCon
import json


# , HttpResponseH, redirect

# Create your views here.
# def login(request):
#     #  业务逻辑
#     request.method  # 请求方式 GET POST
#     request.POST  # POST请求提交的数据  {}
#     request.GET  # url上的查询参数  ?k1=v1&k2=v2  {}
#
#     return HttpResponse('字符串')  # 返回字符串
#     return render(request, 'login.html')  # 返回HTML页面
#     return redirect('地址')  # 重定向


def index(request):
    if request.method == 'POST':
        global scon, scur, xycon, xycur
        print(request.POST)
        OJsourceDatabase = request.POST.get('OJsourceDatabase')
        OJdatabaseName = request.POST.get('OJdatabaseName')
        # OJhost = request.POST.get('OJhost')
        OJport = request.POST.get('OJport')
        OJuser = request.POST.get('OJuser')
        OJpwd = request.POST.get('OJpwd')

        XYsourceDatabase = request.POST.get('XYsourceDatabase')
        XYdatabaseName = request.POST.get('XYdatabaseName')
        XYport = request.POST.get('XYport')
        XYuser = request.POST.get('XYuser')
        XYpwd = request.POST.get('XYpwd')

        print(OJsourceDatabase, OJdatabaseName, OJport, OJuser, OJpwd)  # mysql exam 3306 root root
        print(XYsourceDatabase, XYdatabaseName, XYport, XYuser, XYpwd)  # postgres  postgres 5432 postgres root

        # 连接源数据库
        if OJsourceDatabase == "mysql":
            # 连接源数据库mysql
            scon, scur = getconn(port=int(OJport), user=OJuser, passwd=OJpwd, db=OJdatabaseName)
        elif OJsourceDatabase == "postgres":
            # 连接源数据库postgres
            scon, scur = getpgconn(database=OJdatabaseName, user=OJuser, password=OJpwd, port=int(OJport))
        else:
            return redirect('../options')

        # 连接小雅postgres数据库
        xycon, xycur = getpgconn(database=XYdatabaseName, user=XYuser, password=XYpwd, port=int(XYport))

        return redirect('../xuanze')  # 这里其实是重定向到了view.py中的xuanze 函数
    else:
        return render(request, 'index.html')


def options(request):
    if request.method == 'POST':
        value = request.POST.get('amount')
        print(value)

        if value == '9':
            return redirect('../biancheng')
        elif value == '0' or value == '1':
            return redirect('../xuanze')
        elif value == '2' or value == '3':
            return redirect('../tiankong')
        elif value == '4':
            return redirect('../panduan')
        else:
            return render(request, 'app01/../templates/options.html')
    else:
        return render(request, 'app01/../templates/options.html')


def biancheng(request):
    if request.method == 'GET':
        names = [{'en': 'id', 'cn': 'id'}, {'en': 'title', 'cn': '题目'}, {'en': 'score', 'cn': '分数'},
                 {'en': 'input', 'cn': '输入'}, {'en': 'output', 'cn': '输出'},
                 {'en': 'test', 'cn': '测试用例ID'}]
        tables = get_all_tables()  # 这里以后记得改一下 加上scur
        # print(tables)
        return render(request, 'biancheng.html', {'tables': tables, 'names': names})

    if request.method == 'POST':
        if request.POST.get('table_chose'):
            table1_name = request.POST.get('table_chose')
            ziduan_list = get_all_ziduanming(table1_name)
            return HttpResponse(json.dumps({
                "table_choosed": table1_name,
                "ziduan_list": ziduan_list
            }))
        if request.POST.get('data[id][table]'):
            # 在这里写代码！！

            print(request.POST)
            return redirect('../show')
    #
    # sub1 = request.POST.get('sub1')
    # sub2 = request.POST.get('sub2')
    #
    # if sub1 == '提交1':
    #     select_sql, count_sql, select_sql2 = selectSql_b1(request)
    #     print(select_sql)
    #     print(count_sql)
    #     print(select_sql2)
    #     insert_biancheng1(scur, xycur, xycon, select_sql, count_sql, select_sql2)
    #
    # elif sub2 == '提交2':
    #     select_sql1, count_sql, select_sql2 = selectSql_b2(request)
    #     print(select_sql1)
    #     print(count_sql)
    #     print(select_sql2)
    #     insert_biancheng(scur, xycur, xycon, select_sql1, count_sql, select_sql2)

    # testCon(scur, select_sql)
    # closeconn(xycon, xycur)
    # closeconn(scon, scur)

    return redirect('../show')


def xuanze(request):
    if request.method == 'GET':
        tables = get_all_tables()  # 这里以后记得改一下 加上scur
        return render(request, 'xuanze.html', {'tables': tables, })
    elif request.method == 'POST':
        if request.POST.get('table'):
            table1_name = request.POST.get('table')
            ziduan_list = get_all_ziduanming(table1_name)
            return HttpResponse(json.dumps({
                "table_choosed": table1_name,
                "ziduan_list": ziduan_list
            }))

    # if request.method == 'POST':
    #     sub1 = request.POST.get('sub1')
    #     sub2 = request.POST.get('sub2')
    #
    #     if sub1 == '提交1':
    #         select_sql, count_sql, select_sql2 = selectSql_x1(request)
    #         print(select_sql)
    #         print(count_sql)
    #         print(select_sql2)
    #         insert_xuanze1(scur, xycur, xycon, select_sql, count_sql, select_sql2)
    #
    #     elif sub2 == '提交2':
    #         select_sql, count_sql, select_sql2 = selectSql_x2(request)
    #         print(select_sql)
    #         print(count_sql)
    #         print(select_sql2)
    #         insert_xuanze2(scur, xycur, xycon, select_sql, count_sql, select_sql2)
    #
    #     closeconn(xycon, xycur)
    #     closeconn(scon, scur)
    #     return redirect('../show')
    # else:
    #     return render(request, 'app01/xuanze.html')


def tiankong(request):
    if request.method == 'GET':
        names = [{'en': 'id', 'cn': 'id'}, {'en': 'title', 'cn': '题目'}, {'en': 'score', 'cn': '分数'},
                 {'en': 'answer', 'cn': '正确答案'}]
        tables = get_all_tables()  # 这里以后记得改一下 加上scur
        # print(tables)
        return render(request, 'tiankong.html', {'tables': tables, 'names': names})

    if request.method == 'POST':
        if request.POST.get('table_chose'):
            table1_name = request.POST.get('table_chose')
            ziduan_list = get_all_ziduanming(table1_name)
            return HttpResponse(json.dumps({
                "table_choosed": table1_name,
                "ziduan_list": ziduan_list
            }))
        if request.POST.get('data[id][table]'):
            # 在这里写代码！！

            print(request.POST)
            return redirect('../show')

    #
    # if request.method == 'POST':
    #     sub1 = request.POST.get('sub1')
    #     sub2 = request.POST.get('sub2')
    #
    #     if sub1 == '提交1':
    #         select_sql, count_sql, select_sql2 = selectSql_t1(request)
    #         print(select_sql)
    #         print(count_sql)
    #         print(select_sql2)
    #         insert_tiankong1(scur, xycur, xycon, select_sql, count_sql, select_sql2)
    #
    #     elif sub2 == '提交2':
    #         select_sql, count_sql, select_sql2 = selectSql_t2(request)
    #         # SELECT q.q_id,q.q_content,q.score FROM q,a3 WHERE q.q_id=a3.q_id;
    #         print(select_sql)
    #         # SELECT COUNT(*) FROM a3 WHERE a3.q_id=%s;
    #         print(count_sql)
    #         # SELECT a3.a_id,a3.a_content FROM a3 WHERE a3.q_id=%s;
    #         print(select_sql2)
    #         insert_tiankong2(scur, xycur, xycon, select_sql, count_sql, select_sql2)
    #
    #     closeconn(xycon, xycur)
    #     closeconn(scon, scur)
    #
    #     return redirect('../show')
    # else:
    #     return render(request, 'app01/../templates/tiankong.html')


def panduan(request):
    if request.method == 'GET':
        names = [{'en': 'id', 'cn': 'id'}, {'en': 'title', 'cn': '题目'}, {'en': 'score', 'cn': '分数'},
                 {'en': 'answer', 'cn': '正确答案'},{'en': 'answer_id', 'cn': '答案id'}]
        tables = get_all_tables()  # 这里以后记得改一下 加上scur
        # print(tables)
        return render(request, 'panduan.html', {'tables': tables, 'names': names})

    if request.method == 'POST':
        if request.POST.get('table_chose'):
            table1_name = request.POST.get('table_chose')
            ziduan_list = get_all_ziduanming(table1_name)
            return HttpResponse(json.dumps({
                "table_choosed": table1_name,
                "ziduan_list": ziduan_list
            }))
        if request.POST.get('data[id][table]'):
            # 在这里写代码！！

            print(request.POST)
            return redirect('../show')
    # if request.method == 'POST':
    #     sub1 = request.POST.get('sub1')
    #     sub2 = request.POST.get('sub2')
    #
    #     if sub1 == '提交1':
    #         select_sql, select_sql2 = selectSql_p1(request)
    #         print(select_sql)
    #         print(select_sql2)
    #         insert_panduan1(scur, xycur, xycon, select_sql, select_sql2)
    #
    #     elif sub2 == '提交2':
    #         select_sql, select_sql2 = selectSql_p2(request)
    #         print(select_sql)
    #         print(select_sql2)
    #         insert_panduan2(scur, xycur, xycon, select_sql, select_sql2)
    #
    #     closeconn(xycon, xycur)
    #     closeconn(scon, scur)
    #     return redirect('../show')
    # else:
    #     return render(request, 'app01/../templates/panduan.html')


def show(request):
    return HttpResponse('开始工作！！！')
