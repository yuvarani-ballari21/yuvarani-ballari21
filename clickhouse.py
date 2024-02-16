import clickhouse_connect

import clickhouse_connect

client = clickhouse_connect.get_client(host='localhost', username='default', password='Yuva', database='db')
#QUERY FOR CREATING A TABLE
# client.command('CREATE TABLE new_table (key UInt32, value String, metric Float64) ENGINE MergeTree ORDER BY key')
# #QUERY FOR INSERTING ROWS IN BULK
# row1 = [1000, 'String Value 1000', 5.233]
# row2 = [2000, 'String Value 2000', -107.04]
# data = [row1, row2]
# client.insert('new_table', data, column_names=['key', 'value', 'metric'])
# #INSERTING ROWS IN ONE BY ONE
# sql_query = "INSERT INTO new_table (key, value, metric) VALUES (1, 'String', 5.233)"
# client.query(sql_query)
# #SELECTING DATA FROM TABLE
# result = client.query('SELECT * FROM new_table')
# print(result.result_rows)
#UPDATING THE TABLE DATA Update data using the mutation method
sql_query = "ALTER TABLE new_table UPDATE metric = 10 WHERE key = 1000"
client.query(sql_query)
result = client.query('SELECT * FROM new_table')
print(result.result_rows)
