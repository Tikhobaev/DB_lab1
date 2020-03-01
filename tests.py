from time import time

from database import FilmsDatabase

###################################################################
# INSERT operation validation
###################################################################
db = FilmsDatabase('for_tests_10.hdb')
insert_times = []
start = time()
for i in range(0, 10):
    db.add(['Film' + str(i), '1990', '7', str(1000000 + i)])
end = time()
insert_times.append(end - start)

db.save_to_xlsx()

db = FilmsDatabase('for_tests_100.hdb')
start = time()
for i in range(0, 100):
    db.add(['Film' + str(i), '1990', '7', str(1000000 + i)])
end = time()
insert_times.append(end - start)

db = FilmsDatabase('for_tests_1000.hdb')
start = time()
for i in range(0, 1000):
    db.add(['Film' + str(i), '1990', '7', str(1000000 + i)])
end = time()
insert_times.append(end - start)

db = FilmsDatabase('for_tests_10000.hdb')
start = time()
for i in range(0, 10000):
    db.add(['Film' + str(i), '1990', '7', str(1000000 + i)])
end = time()
insert_times.append(end - start)

for i in range(0, 4):
    print('Count of INSERT operations =', 10 ** (i+1), 'Time:', insert_times[i])


###################################################################
# DROP operation validation
###################################################################

db = FilmsDatabase('for_tests_10.hdb')
search_times = []
start = time()
for i in range(0, 10):
    result = db.search_by_id(1000000 + i)
    if not result:
        print("Cannot find id:", 1000000 + i)
end = time()
search_times.append(end - start)

db = FilmsDatabase('for_tests_100.hdb')
start = time()
for i in range(0, 100):
    result = db.search_by_id(1000000 + i)
    if not result:
        print("Cannot find id:", 1000000 + i)
end = time()
search_times.append(end - start)

db = FilmsDatabase('for_tests_1000.hdb')
start = time()
for i in range(0, 1000):
    result = db.search_by_id(1000000 + i)
    if not result:
        print("Cannot find id:", 1000000 + i)
end = time()
search_times.append(end - start)

db = FilmsDatabase('for_tests_10000.hdb')
start = time()
for i in range(0, 10000):
    result = db.search_by_id(1000000 + i)
    if not result:
        print("Cannot find id:", 1000000 + i)
end = time()
search_times.append(end - start)

print('\n')
for i in range(0, 4):
    print('Count of SEARCH operations =', 10 ** (i+1), 'Time:', search_times[i])

###################################################################
# DROP operation validation
###################################################################

db = FilmsDatabase('for_tests_10.hdb')
drop_times = []
start = time()
for i in range(0, 10):
    db.delete_node(1000000 + i)
end = time()
drop_times.append(end - start)

db = FilmsDatabase('for_tests_100.hdb')
start = time()
for i in range(0, 100):
    db.delete_node(1000000 + i)
end = time()
drop_times.append(end - start)

db = FilmsDatabase('for_tests_1000.hdb')
start = time()
for i in range(0, 1000):
    db.delete_node(1000000 + i)
end = time()
drop_times.append(end - start)

db = FilmsDatabase('for_tests_10000.hdb')
start = time()
for i in range(0, 10000):
    db.delete_node(1000000 + i)
end = time()
drop_times.append(end - start)

print('\n')
for i in range(0, 4):
    print('Count of DROP operations =', 10 ** (i+1), 'Time:', drop_times[i])

with open('validation_results.txt', 'w') as file:
    file.write('INSERT:')
    for i in range(0, 4):
        file.write(f'\n\tCount of INSERT operations = {10 ** (i + 1)} Time: {insert_times[i]}')
    file.write('\nSEARCH:')
    for i in range(0, 4):
        file.write(f'\n\tCount of SEARCH operations = {10 ** (i + 1)} Time: {search_times[i]}')
    file.write('\nDROP:')
    for i in range(0, 4):
        file.write(f'\n\tCount of DROP operations = {10 ** (i + 1)} Time: {drop_times[i]}')



