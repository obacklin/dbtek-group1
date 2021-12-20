from main import *

#user_department = input("Enter department:")
new_query = f"SELECT * FROM DEPARTMENT WHERE 1="
q_show_all = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'PRODUCT'"
show_prod = f'SELECT ProductTitle FROM PRODUCT'

#results = read_query(connection, new_query)
res2 = read_query(connection,show_prod)
for result in res2:
    print(result)
