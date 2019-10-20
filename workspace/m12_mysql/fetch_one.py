import mysql.connector
from mysql.connector import errorcode

cursor = None
conn = None
try:
    conn = mysql.connector.connect(database='db01', user='root', password='dfgh0147')
    cursor = conn.cursor()
    query = "SELECT ename, hiredate, salary FROM employee WHERE empno = %s"
    empno = 1001
    cursor.execute(query, (empno,))
    emp = cursor.fetchone()

    if emp is not None:
        print(emp)
        print('name={}, hiredata={}, salary={}'.format(emp[0], emp[1], emp[2]))
    print('total', cursor.rowcount, "employees")

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
