from xyDB.connect.closeConnect import closeconn
from xyDB.connect.getConnect import getconn

get_tables = """show tables;"""
get_ziduanming = """DESC %s"""
import pandas as pd
def get_all_tables():
    scon, scur = getconn(port=int(3306), user='root', passwd='root', db='exam')
    scur.execute(get_tables)
    results = scur.fetchall()
    closeconn(scon, scur)

    tables = []
    for res in results:
        tables.append(res[0])
    # print(tables)
    return tables

def get_all_ziduanming(table_name):
    scon, scur = getconn(port=int(3306), user='root', passwd='root', db='exam')
    scur.execute(get_ziduanming % (table_name))
    results = scur.fetchall()
    closeconn(scon, scur)

    ziduan_list = [] #字段名列表
    for result in results:
        ziduan_list.append(result[0])
    # print(ziduan_list)
    return ziduan_list

# get_all_ziduanming('q')