import praw,OAuth2Util,time
def make_output(stats):
    output = {}
    for flair,count in stats.items():
        name = flair
        output[name] = count
    sorted_output = sorted(output.keys())
    
    filename = 'C:/Users/adost1/Documents/GitHub/leagueoflegends/flairstats/flairstats%s.csv'%(time.strftime("-%H-%d-%m-%Y"))
    f = open(filename, 'w')
    for name in sorted_output:
        f.write('%s,%d\n' % (name,output[name]))
    f.write('\n\n')
    #f.write('%s,%d' % ('Total',stats['total']))
    f.close()

r = praw.Reddit("Flair PDF Analyze")
o = OAuth2Util.OAuth2Util(r)
c = ['Aatrox', 'Ahri', 'Akali', 'Alistar', 'Amumu', 'Anivia', 'Annie', 'Ashe', 'Azir', 'Bard', 'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Cassiopeia', 'Chogath', 'Corki', 'Darius', 'Diana', 'DrMundo', 'Draven', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'FiddleSticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 'Hecarim', 'Heimerdinger', 'Irelia', 'Janna', 'JarvanIV', 'Jax', 'Jayce', 'Jinx', 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kennen', 'Khazix', 'KogMaw', 'Leblanc', 'LeeSin', 'Leona', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar', 'Maokai', 'MasterYi', 'MissFortune', 'MonkeyKing', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus', 'Nautilus', 'Nidalee', 'Nocturne', 'Nunu', 'Olaf', 'Orianna', 'Pantheon', 'Poppy', 'Quinn', 'Rammus', 'RekSai', 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Sejuani', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona', 'Soraka', 'Swain', 'Syndra', 'TahmKench', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere', 'TwistedFate', 'Twitch', 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar', 'Velkoz', 'Vi', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Xerath', 'XinZhao', 'Yasuo', 'Yorick', 'Zac', 'Zed', 'Ziggs', 'Zilean', 'Zyra']
#flair = r.get_flair_list('leagueoflegends',limit = None)
flairlist = {}
def build(category,column):
    return {category,column}
flair = r.get_flair_list('leagueoflegends',limit = 100)    
data_list = []
deleted = []
active = []
total = 0
for f in flair:
    if f['flair_css_class'] == '' or f['flair_css_class'] == None:
        pass
    elif f['flair_css_class'] not in list(flairlist.keys()):
        flairlist[f['flair_css_class']] = 1
        data_list.append({"category": f["flair_css_class"],"column-1": 1})
    else:
        flairlist[f['flair_css_class']] =  flairlist[f['flair_css_class']] + 1
        for a in data_list:
            if a['category'] == f['flair_css_class']:
                a["column-1"] = a["column-1"] + 1
    total+=1
    
make_output(flairlist)
def dict_build(team,count):
    return '''{"category":"%s", "column-1": %d}''' % (team,count)
x = []
for a in data_list:
    if a['category'] == '':
        pass
    else:
        x.append(dict_build(a['category'],a['column-1']))
s = ''
for a in x:
    s+=a + ','
html = '''
<!DOCTYPE html>
<html>
	<head>
		<title>chart created with amCharts | amCharts</title>
		<meta name="description" content="chart created using amCharts live editor" />

		<!-- amCharts javascript sources -->
		<script type="text/javascript" src="http://www.amcharts.com/lib/3/amcharts.js"></script>
		<script type="text/javascript" src="http://www.amcharts.com/lib/3/serial.js"></script>
		<script type="text/javascript" src="http://www.amcharts.com/lib/3/themes/black.js"></script>

		<!-- amCharts javascript code -->
		<script type="text/javascript">
			AmCharts.makeChart("chartdiv",
				{
					"type": "serial",
					"categoryField": "category",
					"startDuration": 1,
					"theme": "black",
					"categoryAxis": {
						"gridPosition": "start"
					},
					"chartCursor": {},
					"chartScrollbar": {},
					"trendLines": [],
					"graphs": [
						{
							"fillAlphas": 1,
							"id": "AmGraph-1",
							"title": "graph 1",
							"type": "column",
							"valueField": "column-1"
						}
					],
					"guides": [],
					"valueAxes": [
						{
							"id": "ValueAxis-1",
							"title": "Axis title"
						}
					],
					"allLabels": [],
					"balloon": {},
					"titles": [
						{
							"id": "Title-1",
							"size": 15,
							"text": "Chart Title"
						}
					],
					"dataProvider": [
'''

final_html = html + s[:-1]
footer = ''']
				}
			);
		</script>
	</head>
	<body>
		<div id="chartdiv" style="width: 100%; height: 400px; background-color: #222222;" ></div>
	</body>
</html>'''
res = final_html + footer
HTML_FILE = open('index.html','w')
HTML_FILE.write(res)
HTML_FILE.close()
