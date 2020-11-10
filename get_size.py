#
#
#
#
#
#______________________________________________________________________________________________________________________
import mysql.connector

host_name=''
port_number=''
psw=''

#______________________________________________________________________________________________________________________
## Connect to MySQL instance and query the data ##
conn = mysql.connector.connect(user='read-only', password=psw, host=host_name, port=port_number)
cursor = conn.cursor(dictionary=True)
query = ("SELECT sum(data_length+index_length)/1024/1024 ‘Size’ FROM information_schema.TABLES GROUP BY table_schema;")
cursor.execute(query) ## Execute query
row = cursor.fetchone() ## Get first row
#______________________________________________________________________________________________________________________

#______________________________________________________________________________________________________________________
## Extract the key ##
key = str(row.keys())
key = key[12:16]
#key = "\'"+ key + "\'"
#print("\n>> The extracted key is: " + key + " <<\n")
#______________________________________________________________________________________________________________________

#______________________________________________________________________________________________________________________
## Fill the list with the values of DB sizes ##
list = []
#Get rows and fill the list with their cast to float
while row is not None:
	list.append(float(row.get(key))) 
	row = cursor.fetchone()
#______________________________________________________________________________________________________________________

#______________________________________________________________________________________________________________________
## Get the total sum ##
sum=0
#Get the total sum
for elem in list:
	sum+=elem
print("\n>> Size of this instance: " + sum/1024 + " <<\n")

conn.close()
#______________________________________________________________________________________________________________________
#
#
#
#
#
