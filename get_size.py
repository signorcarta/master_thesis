import mysql.connector

host_name=''
port_number=''
psw=''

conn = mysql.connector.connect(user='read-only', password=psw, host=host_name, port=port_number)
cursor = conn.cursor(dictionary=True)
query = ("SELECT sum(data_length+index_length)/1024/1024 ‘Size’ FROM information_schema.TABLES GROUP BY table_schema;")
cursor.execute(query)

row = cursor.fetchone()
key = str(row.keys())
key = key[12:16]

list = []
#Get rows and fill the list with their cast to float
while row is not None:
list.append(float(row.get(key))) 
row = cursor.fetchone()

sum=0
#Get the total sum
for elem in list:
	sum+=elem
print(sum/1024)

conn.close()
