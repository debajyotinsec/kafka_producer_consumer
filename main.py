
from pg_conn import *
from read_data_file import *

db_conf_file = 'db_local.conf'
connection_id_pg,  pg_connection_parameters = setup_db_conn(db_conf_file)


input_file_path = 'Toyota_DataDump.txt'
read_file(input_file_path, connection_id_pg)


connection_id_pg.commit()
connection_id_pg.close()
        
        




