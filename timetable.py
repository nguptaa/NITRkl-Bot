import pickle, string, os

time_table = pickle.load(open('class_timetable.db', 'rb'))

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
sections = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
times = [['8AM','9AM'], ['9AM', '10AM'], ['10AM', '11AM'], ['11AM', '12PM'], ['12PM', '1:15PM'], ['1:15PM', '2:15PM'], ['2:15PM', '3:15PM'], ['3:15PM', '4:15PM'], ['4:15PM', '5:15PM']]

bx = ''
by = ''
bz = []

def iterate_save(iterlist, savepoint=''):
    if savepoint == '':
        for x in iterlist:
            yield x
    else:
        i = iterlist.index(savepoint)
        nlist = iterlist[i+1:]
        for x in nlist:
            yield x
if os.path.isfile('savepoint'):
    try:
        arr = pickle.load(open('savepoint', 'rb'))
        bx = arr[0]
        by = arr[1]
        bz = arr[2]
        for x in iterate_save(days, bx):
            time_table[x] = {}
            for y in iterate_save(sections, by):
                time_table[x][y] = []
                for z in iterate_save(times, bz):
                    print 'Enter', x, y, '-'.join(z), ': '
                    time_table[x][y].append(z + [raw_input().upper()])
                    bz = z
                by = y
            bx = x

        pickle.dump(time_table, open('class_timetable.db', 'wb'))
    except KeyboardInterrupt:
        pickle.dump([bx, by, bz], open('savepoint', 'wb'))
        pickle.dump(time_table, open('class_timetable.db', 'wb'))

else:
    try:
        for x in iterate_save(days):
            time_table[x] = {}
            for y in iterate_save(sections):
                time_table[x][y] = []
                for z in iterate_save(times):
                    print 'Enter', x, y, '-'.join(z), ': '
                    time_table[x][y].append(z + [raw_input().upper()])
                    bz = z
                by = y
            bx = x

        pickle.dump(time_table, open('class_timetable.db', 'wb'))
    except KeyboardInterrupt:
        pickle.dump([bx, by, bz], open('savepoint', 'wb'))
        pickle.dump(time_table, open('class_timetable.db', 'wb'))
