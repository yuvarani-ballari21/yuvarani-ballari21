# import redis
# r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# print(r)
# print(type(r))
# #Connect to localhost on port 6379, set a value in Redis, and retrieve it. 
# # All responses are returned as bytes in Python. 
# # To receive decoded strings, set decode_responses=True
# r.set('foo', 'bar')
# # True
# x = r.get('foo')
# print(x)
import clickhouse_connect

client = clickhouse_connect.get_client(host='localhost', password='',database='db')
# print(client)
x = "create table IF NOT EXISTS my_table(id Int8, name String) ENGINE = MergeTree Order By id"
client.command(x)
row1 = [1, 'krish']
row2 = [2, 'sony']
data = [row1, row2]
client.insert('my_table', data,column_names=['id','name'])
# result = client.query("select id, name from my_table")
# print(result.result_rows)

# result = client.insert("insert into my_table values(2,'abcd')")
# print(result)
