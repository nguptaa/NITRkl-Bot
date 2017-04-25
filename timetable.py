import pickle, string, os

time_table = pickle.load(open('class_timetable.db', 'rb'))

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
sections = ['H','G']
times = [['8:00AM','9:00AM'], ['9:00AM', '10:00AM'], ['10:00AM', '11:00AM'], ['11:00AM', '12:00PM'], ['12:00PM', '1:15PM'], ['1:15PM', '2:15PM'], ['2:15PM', '3:15PM'], ['3:15PM', '4:15PM'], ['4:15PM', '5:15PM']]
times2 = [['8AM','9AM'], ['9AM', '10AM'], ['10AM', '11AM'], ['11AM', '12PM'], ['12PM', '1:15PM'], ['1:15PM', '2:15PM'], ['2:15PM', '3:15PM'], ['3:15PM', '4:15PM'], ['4:15PM', '5:15PM']]

new_table = {}

for x in days:
    new_table[x] = {}
    for y in sections:
        new_table[x][y] = []
        for z in times:
            for a in times2:
                if times.index(z) == times2.index(a):
                    new_table[x][y].append(z + [time_table[x][y][times.index(z)][2]])

pickle.dump(new_table, open('new_timetable.db', 'wb'))
