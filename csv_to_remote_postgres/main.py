import psycopg2


connection = psycopg2.connect(dbname='dbname', user='username', password='password', host='hostname')
with connection.cursor() as cursor:
    with open('./test_data.csv') as file:
        header = True
        for l in file:
            if header:
                header = False
                continue
            line = l.rstrip()#.replace(',,', ',NULL,')
            line_list = line.split(',')
            string_indexes_list = [6, 7, 8, 9]

            for x in range(len(line_list)):
                if line_list[x] == '':
                    line_list[x] = 'NULL'
                elif x in string_indexes_list:
                    line_list[x] = '\'' + line_list[x] + '\''

            line = my_string = ','.join(line_list)

            if line.endswith(','):
                line = line + 'NULL'
            cursor.execute(f'INSERT INTO cars VALUES ({line})')
    connection.commit()

