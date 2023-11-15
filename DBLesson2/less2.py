import psycopg2
import csv

conn = psycopg2.connect(host = 'localhost',
                       database = 'postgres',
                       port = '5432',
                       user = 'postgres',
                       password = '1234' )

cursor = conn.cursor()

cursor.execute('SELECT * FROM language limit 10')

n = cursor.fetchall()
for i in n:
    print(i)

csvfile = open('output3.csv', 'w')
csvwriter = csv.writer(csvfile)

for i in n:
    csvwriter.writerow(n)
