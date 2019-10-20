# 2.	檔案的練習-add_emp
# 在emp.txt文字檔中設定五筆employee的資料，將之新增至資料庫中。
# 註1：一筆資料一列，每個資料欄的資料以逗號(,)隔開
# 註2：建議使用cursor.executemany(sql, seq_of_params)來實作
import mysql.connector
from mysql.connector import errorcode

cursor = None
conn = None
try:
    conn = mysql.connector.connect(database='db01', user='root', password='dfgh0147')
    cursor = conn.cursor()

    with open('emp.txt', 'rt', encoding='utf-8') as f:
        context = f.readlines()
        ins_data = []
        for i in range(len(context)):
            ins_data.append(list(repr(context[i]).replace('"', '').replace("'", "").replace("\\n", "").split(",")))
            for j in range(len(ins_data[i])):
                ins_data[i][j] = ins_data[i][j].strip()
            ins_data[i] = tuple(ins_data[i])
            print(ins_data[i])
    print('read', len(context), "employees from file")

    ins = "INSERT INTO employee VALUES(%s, %s, %s, %s, %s, %s)"
    cursor.executemany(ins, ins_data)
    # conn.commit()
    print('insert', cursor.rowcount, "employees into database")

    query = "SELECT * FROM employee"
    cursor.execute(query)
    emps = cursor.fetchall()

    for emp in emps:
        for i in range(len(emp)):
            print(emp[i], end=',') if i != len(emp) - 1 else print(emp[i])
            pass
    print('total', cursor.rowcount, "employees read form database")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('user or password error')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("database doesn't existed")
    else:
        print(err)

finally:
    if cursor:
        print('cursor is closed')
        cursor.close()

    if conn:
        print('database is closed')
        conn.close()
