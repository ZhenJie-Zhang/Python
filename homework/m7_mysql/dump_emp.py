# 1.	檔案的練習-dump_emp
# 將employee表格裡的所有資料dump至檔案中。
# 註：一筆資料一列，每個資料欄的資料以逗號(,)隔開
import mysql.connector
from mysql.connector import errorcode

cursor = None
conn = None
try:
    conn = mysql.connector.connect(database='db01', user='root', password='dfgh0147')
    cursor = conn.cursor()
    query = "SELECT * FROM employee"
    cursor.execute(query)
    emps = cursor.fetchall()

    # for i in range(len(emps)):
        # print(emp for emp in emps[i])
        # print(repr(emps[i]).lstrip("(").rstrip(")"))

    print("=====================================")

    for emp in emps:
        for i in range(len(emp)):
            print(emp[i], end=',') if i != len(emp) - 1 else print(emp[i])
            with open('dump.txt', 'a') as f:
                f.write('{},'.format(emp[i])) if i != len(emp) - 1 else f.write('{}\n'.format(emp[i]))
    print('dump', cursor.rowcount, "employees into file")

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
