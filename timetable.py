import pickle

time_table = pickle.load(open('class_timetable.db', 'rb'))
try:
    for x in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        time_table[x] = {}
        for y in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            time_table[x][y] = []
            for z in [['8AM','9AM'], ['9AM', '10AM'], ['10AM', '11AM'], ['11AM', '12PM'], ['1:15PM', '2:15PM'], ['2:15PM', '3:15PM'], ['3:15PM', '4:15PM'], ['4:15PM', '5:15PM']]:
                print 'Enter', x, y, '-'.join(z),': '
                time_table[x][y] = z.append(raw_input())

except KeyboardInterrupt:
    pickle.dump(time_table, open('class_timetable.db', 'wb'))
    print 'Type everything next time!'
