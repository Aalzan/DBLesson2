import psycopg2

conn = psycopg2.connect(host = 'localhost',
                       database = 'postgres',
                       port = '5432',
                       user = 'postgres',
                       password = '1234' )

cursor = conn.cursor()

def binary_search(target_id):
    cursor.execute("SELECT name FROM names WHERE id = %s", (target_id,))
    result = cursor.fetchone()

    if not result:
        return f"no {target_id} such id"

    name = result[0]
    return f"id {target_id} found{name}"
target_id = int(input("ID: "))
result_message = binary_search(target_id)
print(result_message)
cursor.close()
conn.close()
