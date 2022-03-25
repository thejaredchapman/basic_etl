# example queries, will be unique for different database platforms

sqlserver_extract = ('''
  SELECT sqlserver_col_1, sqlserver_col_2, sqlserver_col_3
  FROM sqlserver_1_table
''')
sqlserver_insert = ('''
  INSERT INTO table_demo (col_1, col_2, col_3)
  VALUES (?, ?, ?)  
''')
mysql_extract = ('''
  SELECT mysql_col_1, mysql_col_2, mysql_col_3
  FROM mysql_demo_table
''')
mysql_insert = ('''
  INSERT INTO table_demo (col_1, col_2, col_3)
  VALUES (?, ?, ?)  
''')

# Queries getting exported
class Sql_Query:
  def __init__(self, extract_query, load_query):
    self.extract_query = extract_query
    self.load_query = load_query   
# create instances for Sql_Query class
sqlserver_query = SqlQuery(sqlserver_extract, sqlserver_insert)
mysql_query = SqlQuery(mysql_extract, mysql_insert)
# creating a list for iterating through values
mysql_queries = [mysql_query]
sqlserver_queries = [sqlserver_query]