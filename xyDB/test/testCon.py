def testCon(cur, sql):
    cur.execute(sql)
    results = cur.fetchall()
    for result in results:
        print(result)
