datawarehouse_name = 'your_dwh_name'
# sql-server (target db, datawarehouse)
datawarehouse_db_config = {
  'Trusted_Connection': 'yes',
  'driver': '{SQL Server}',
  'server': 'datawarehouse_sql_server',
  'database': '{}'.format(datawarehouse_name),
  'user': 'your_db_uname',
  'password': 'your_db_pword',
  'autocommit': True,
}
# source db > sql-server
sqlserver_db_config = [
  {
    'Trusted_Connection': 'yes',
    'driver': '{SQL Server}',
    'server': 'your_db_sql_server',
    'database': 'db_1st',
    'user': 'your_db_uname',
    'password': 'your_db_pword',
    'autocommit': True,
  }
]
# source db > mysql
mysql_db_config = [
  {
    'user': 'your_1_user',
    'password': 'your_1_pword',
    'host': 'db_connection_string_1',
    'database': 'db_1st',
  },
  {
    'user': 'your_2_user,
    'password': 'your_2_password',
    'host': 'db_connection_string_2',
    'database': 'db_2nd',
  },
]