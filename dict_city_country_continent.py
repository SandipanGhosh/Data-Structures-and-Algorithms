"""
Should output -

1
['Atlanta', 'Mountain View']
2
['Bangalore-India', 'Shanghai-China']

"""

locations = {'North America' : {'USA' : ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India' : ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt' : ['Cairo']}

print 1
usa_sorted = sorted(locations['North America']['USA'])
print usa_sorted

print 2
asia_cities = []
for countries, cities in locations['Asia'].items():
	city_country = cities[0] + "-" + countries
	asia_cities.append(city_country)
asia_sorted = sorted(asia_cities)
print asia_sorted