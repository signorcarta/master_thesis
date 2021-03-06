#
#
#
#
#

import mysql.connector

ports = []

hosts = []

psw = ''

ls = zip(hosts, ports)

for elem in ls:

        host_name = elem[0]
        port_number = elem[1]

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

        print("\n.\n.\n.\nExamined instance: " + host_name)
        ## Separate InnoDB and non-InnoDB tables
        inno_tables = []
        other_tables = []
        nonInnoDBengine = []
        InnoDBengine = [] # This list is left empty on purpose

        for elem in info_list:
                engine= elem[1]
                table = elem[0]
                if(engine != 'InnoDB' and engine != None):
                        other_tables.append(table)
                        nonInnoDBengine.append(engine)
                else:
                        inno_tables.append(table)

                nonInnoS = zip(other_tables, nonInnoDBengine)

        name_file = host_name + "_" + str(port_number) +  ".txt"
        output = open(name_file, "w")

        ## Print non-InnoDB tables ##
        for elem in nonInnoS:
                print("\n   Table [" + str(elem[0]) + "] type is: " + elem[1], file = output)

        ## Print InnoDB tables ##
        #for elem in inno_tables:
        #        print("\n   Table [" + str(elem) + "] type is InnoDB")

        print("\n###### SUMMARY ######", file = output)
        print("_____________________", file = output)
        print("| Total:      | " + str(len(table_name)) + " |", file = output)
        print("| InnoDB:     | " + str(len(inno_tables)) + " |",file = output)
        print("| Non-InnoDB: | " + str(len(other_tables)) + " |",file = output)
        print("_____________________", file = output)
