# variables
from db_credentials import datawarehouse_db_config, sqlserver_db_config, mysql_db_config
from sql_queries import sqlserver_queries, mysql_queries

# methods
from etl import etl_process
def main():
  print('starting the etl data process')
	
  # establish connection for SQL Server, desired destination storage
  target_cnx = pyodbc.connect(**datawarehouse_db_config)
	
  # looping through credentials
  # Database > mysql
  for config in mysql_db_config: 
    try:
      print("loading db: " + config['database'])
      etl_process(mysql_queries, target_cnx, config, 'mysql')
    except Exception as error:
      print("etl for {} has error".format(config['database']))
      print('error message: {}'.format(error))
      continue
	
  # Database > sql-server
  for config in sqlserver_db_config: 
    try:
      print("loading db: " + config['database'])
      etl_process(sqlserver_queries, target_cnx, config, 'sqlserver')
    except Exception as error:
      print("etl for {} has error".format(config['database']))
      print('error message: {}'.format(error))
      continue

  target_cnx.close()
if __name__ == "__main__":
  main()