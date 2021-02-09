#
#
#

###########################################################################
## This script performs the following checks on all the MySQL instances: ##
##      - Binary-log saving enabled/disabled                             ##
##      - Running MySQL version                                          ##
###########################################################################

###########################################################################
## NOTES ##################################################################
###########################################################################
## Missing instances giving "Bad Handshake" error ##                      #


import mysql.connector

ports = []
hosts = [""]
psw == ''

ls = zip(hosts, ports)

for elem in ls:

        host_name = elem[0]
        port_number = elem[1]

        conn = mysql.connector.connect(user='read-only', password=psw, host=host_name, port=port_number)

        ## Retrieve log-bin saving variable ##
        cursor = conn.cursor(dictionary=True)
        log_bin = ("SELECT @@log_bin;")
        cursor.execute(log_bin)
        row = cursor.fetchone()
        cursor.close()

        ## Retrieve MySQL DB Version in use ##
        cursor = conn.cursor(dictionary=True)
        version = ("SELECT VERSION();")
        cursor.execute(version);
        ver = cursor.fetchone()
        cursor.close()

        val = row.values()
        val = list(val)
        val = val[0]

        ver = ver.values()
        ver = list(ver)
        ver = ver[0]

        ## Print status of log-bin variable ##
        if val>0:
                print("\n >>Log-bin ENABLED on instance " + host_name + "\n")
        else:
                print("\n >>Log-bin NOT ENABLED on instance " + host_name + "\n")

        ## Print version of MySQL ##
        print("   MySQL version: " + str(ver))

        conn.close()
