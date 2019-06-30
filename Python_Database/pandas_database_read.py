import pymysql
import pandas as pd


connection = pymysql.connect(host='localhost',port=3306,user='root',database='lsb',autocomit=True,passwd='')


query = 'select * from Book'


dataset = pd.read_sql_query(query,connection)


print(dataset)

book_id = 1
book_title = "Name"
book_price = 23.06
book_author = 'Ravi Shastri'
cursor = connection.cursor()
query = "insert into books values (%s,%s,%s,%s)"

cursor.execute(query,(book_id,book_title,book_price,book_author))

