import mysql.connector as mysql
connection=mysql.connect(host="192.168.1.13",user="nothinormuch",port="3306",passwd="simplecubes")
if connection.is_connected():
    print("Connection Sucessful!")