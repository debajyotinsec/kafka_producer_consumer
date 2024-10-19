import configparser
import psycopg2

def pg_conn(pg_connection_parameters):
    hostname = pg_connection_parameters['hostname'] 
    port     = pg_connection_parameters['port']
    database = pg_connection_parameters['database']
    username = pg_connection_parameters['username']
    password = pg_connection_parameters['password']

    connection_id = None
    connection_id = psycopg2.connect(
        host=hostname,
        port=port,
        database=database,
        user=username,
        password=password
    )
    print ("Connected to Postgres ---> {}".format(connection_id))
    return connection_id


def pg_conn_setup(db_conf_file):

    config = configparser.ConfigParser()
    config.read(db_conf_file)
    pg_connection_parameters = dict()
    if config.has_section('POSTGRES'):
        pg_connection_parameters['hostname'] = config['POSTGRES']['hostname']
        pg_connection_parameters['port']     = config['POSTGRES']['port']
        pg_connection_parameters['database'] = config['POSTGRES']['database']
        pg_connection_parameters['username'] = config['POSTGRES']['username']
        pg_connection_parameters['password'] = config['POSTGRES']['password']
        pg_connection_parameters['schema']   = config['POSTGRES']['schema']
        pg_connection_parameters['table']    = config['POSTGRES']['table']
    else:
        print ("Postgres connection details not found.")

    connection_id = pg_conn(pg_connection_parameters)
    return connection_id, pg_connection_parameters

