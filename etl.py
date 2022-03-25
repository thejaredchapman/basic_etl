# python-based modules
import pyodbc
import mysql.connector

def etl(query, source_cnx, target_cnx):
  # extract data from demo source database
  source_cursor = source_cnx.cursor()
  source_cursor.execute(query.extract_query)
  data = source_cursor.fetchall()
  source_cursor.close()

  # load data into demo Data Warehouse db
  
if data:
    target_cursor = target_cnx.cursor()
    target_cursor.execute("USE {}".format(name_for_datawarehouse))
    target_cursor.executemany(query.load_query, data)
    print('data loaded to the demo Data Warehouse db')
    target_cursor.close()
  else:
    print('data is empty')

def etl_process(queries, target_cnx, source_db_config, db_platform):

  # configuring demo source database connection
  if db_platform == 'mysql':
    source_cnx = mysql.connector.connect(**source_db_config)
  elif db_platform == 'sqlserver':
    source_cnx = pyodbc.connect(**source_db_config)
  else:
    return 'Error! unrecognised source database platform'
  # loop through sql queries
  for query in queries:
    etl (query, source_cnx, target_cnx)    
  # close the source db connection
  source_cnx.close()