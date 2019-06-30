import pymysql
import pandas as pd


conn = pymysql.connect(host='localhost',port=3306,database='lms',user='root',passwd='12345',autocomit=True)

# Reading from mysql db through pandas which convert it into DataFrames by Default
# reqd : connection

query = 'select * from Books'

dataset = pd.read_sql(query,conn)


#  query executed through pymysql:cursor
# not reqd. :  connection
# sql - " %s "
# sqlite3 - " ? "

cursor = conn.cursor()

query = 'insert into Books values(%s,%s,%s,%s)'

book_title = 'Numbers'
book_price = 23.04
book_author = 'Rafa Nogues'
book_id = 123456789

cursor.execute(query,(book_id,book_title,book_price,book_author))








