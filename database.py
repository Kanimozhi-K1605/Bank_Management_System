#Database Management Banking
import mysql.connector as sql
#conn = mysql.connector.connect(host='localhost',password = 'Mithran@18',user='root')
#if conn.is_connected():
#    print('Connection established')

mydb = sql.connect(host='localhost',
                   user='root',
                   password = 'Mithran@18',
                   database = 'BANK')
cursor = mydb.cursor()

def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result

def createcustomertable():
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers
                (username VARCHAR(20) NOT NULL,
                password VARCHAR(20) NOT NULL,
                name VARCHAR(20) NOT NULL,
                age INTEGER NOT NULl,
                city VARCHAR(20) NOT NULL,
                balance INTEGER NOT NULL,
                account_number INTEGER NOT NULL,
                status BOOLEAN NOT NULL)
    ''')
mydb.commit()

if __name__ == "__main__":
    createcustomertable()