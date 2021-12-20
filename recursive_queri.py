import main

db_connection = main.connection

def list_child_departments(dept):
    query = f"SELECT DeptTitle FROM DEPARTMENT WHERE DTitle = '{dept}' "
    response = main.read_query(db_connection, query)
    for res in response:
        print(res[0])
        list_child_departments(res[0])

if __name__ == '__main__':
    dept = 'Homepage'
    list_child_departments(dept)