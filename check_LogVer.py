#
#
#

##########################################################################
## This script performs the following checks on all the MySQL instances:
##      - Binary-log saving enabled/disabled
##      - Running MySQL version
##########################################################################

## Missing instances giving "Bad Handshake" error ##
import mysql.connector

ports = [3307,3309,3308,3306,3306,3306,3306,3306,3306,3306,3306,3306,3306,
3306,3306,3306,3306,3306,3306,3306,3307,3306,3306,3306,3306,3306,3306,3306]

hosts = ["lximydb22v1","mydwcl01","mydwcl02","mydbcl01","myalcl01","mysuapcl01.sim.infocamere.it",
"myigovcl01.sim.infocamere.it","myigovpr01.sim.infocamere.it","mylifepr01.sim.infocamere.it","myipecpr01.sim.infocamere.it","mysuappr01.sim.infocamere.it","mysuappr02.sim.infocamere.it","lximydb002v1","mydbpr01","mydbicep01","mydwpr01","mydwpr03","mydwpr05","mysqlicpr01","mydbcontpr02","lximydb003v1","mydbpr02","myalpr01","mydwpr02","mydwpr04","mydbcontpr01","vlxidb01","lximydb001"]

ls = zip(hosts, ports)

for elem in ls:

        host_name = elem[0]
        port_number = elem[1]

        conn = mysql.connector.connect(user='read-only', password='', host=host_name, port=port_number)
        
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

        if val>0:
                print("\n >>Log-bin ENABLED on instance " + host_name + "\n")
        else:
                print("\n >>Log-bin NOT ENABLED on instance " + host_name + "\n")
        print("   MySQL version: " + str(ver))

        conn.close()
