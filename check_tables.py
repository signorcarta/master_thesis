#
#
#
#
#_________________________________________
import mysql.connector

host_name =''
port_number = 
psw = ''

## Connect to the MySQL instance and query the data ##
conn = mysql.connector.connect(user='read-only', password=psw, host=host_name, port=port_number)
cursor = conn.cursor(dictionary=True)
query = ("SELECT TABLE_NAME, ENGINE FROM information_schema.TABLES;")
cursor.execute(query) # Execute query
row = cursor.fetchone() # Fetch the first row

## Get list with all tables and their engine ##
table_name = []
table_engine = []
while row is not None:
       table_name.append(row.get('TABLE_NAME'))
       table_engine.append(row.get('ENGINE'))
       row = cursor.fetchone()

info_list = zip(table_name, table_engine)

## Save lists of InnoDB and !=InnoDB tables ##
print("\n.\n.\n.\n>> Examined instance: " + host_name + "\n   The following are non-InnoDB tables: ")
inno_tables = []
other_tables = []
## Print non-InnnoDB tables ##
for elem in info_list:
        engine= elem[1]
        table = elem[0]
        if(engine != 'InnoDB' and engine != None):
                print("\n   Table [" + str(table) + "] type is: " + str(engine))
                other_tables.append(table)
        else:
                inno_tables.append(table)

## Print InnoDB tables ##
#for elem in info_list:
#        engine= elem[1]
#        table = elem[0]
#        if(engine == 'InnoDB'):
#                print("\n   Table [" + str(table) + "] type is InnoDB")                     