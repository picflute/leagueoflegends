import os
import datetime
from bokeh.charts import Line, output_file, show


path = 'C:/Users/adost1/Documents/Github/leagueoflegends/flairstats'
dated_files = [(os.path.getmtime(fn), os.path.basename(fn))
               for fn in os.listdir(path) if fn.lower().endswith('.csv')]
dated_files.sort()
dated_files.reverse()
#Build titles
titles = {}
times = []
import datetime
for a in dated_files[:4]:
    times.append(a[0])
    f = open(a[1],'r')
    read = f.read().split('\n')
    print(read)
    for s in read:
        temp = s.split(',')
        if temp[0] not in titles and temp[0] != '':
            titles[temp[0]] = [temp[1]]
        elif temp[0]!= '':
            titles[temp[0]].append(temp[1])
    f.close()


sorted_titles = sorted(list(titles.keys()))
data = titles

# output to static HTML file
output_file("lines.html", title="line plot example")

# create a new line chat with a title and axis labels
p = Line(data, title="simple line example", xlabel='x', ylabel='values')

# show the results
show(p)
