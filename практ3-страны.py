import collections
import json
from functools import reduce

# 1
# Opening JSON file
f = open('countries.json') 
# returns JSON object as 
# a dictionary
countries = json.load(f)
#print(list(conreies))

# 2
upercaseContries = map(lambda x: x.upper(), countries)
#print(list(upercaseContries))

# 3
landContries = filter(lambda x: 'land' in x, countries)
#print(list(landContries))

# 4
sixLengthContries = filter(lambda x: len(x) == 6, countries)
#print(list(sixLengthContries))

# 5
bigLengthContries = filter(lambda x: len(x) >= 6 , countries)
#print(list(bigLengthContries))


# 6
EContries = filter(lambda x: x.startswith('E'), countries)
#print(list(EContries))

# 7
#print( reduce(lambda a, b: a + ', ' + b, ['Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']) + ' are countries of North Europe')

#8
# не совсем понял задание
# фильтр из условий 3 и 4  
unionFilteredContries = filter(lambda x: 'land' in x and len(x) == 6, countries)
#print(list(unionFilteredContries))

#9

def categorize_countries(str1, countries):
    def greet(str2):
        def greet2(str3):
            def greet3(str4):
                list1 = list(filter( lambda x: str1 in x, countries))
                list2 = list(filter( lambda x: str2 in x, countries))
                list3 = list(filter( lambda x: str3 in x, countries))
                list4 = list(filter( lambda x: str4 in x, countries))

                return list1 + list2 + list3 + list4
            return greet3
        return greet2
    return greet

unionContries = categorize_countries('land', countries)('ia')('island')('stan')
#print(list(unionContries))
# Closing file
f.close()

#10
f = open('countries-data.json') 
countriesData = json.load(f)

#10.1
sortedByName = sorted(countriesData, key=lambda x: x['name'])
sortedByCapital = sorted(countriesData, key=lambda x: x['capital'])
sortedByPopulation = sorted(countriesData, key=lambda x: x['population'])

#10.2
languages = sum(map(lambda x: x['languages'], countriesData), [])
counter = collections.Counter(languages)
print(counter.most_common()[:10])

#10.3
mostPopulation = sorted(countriesData, key=lambda x: x['population'], reverse=True)[:10]
#print(list(mostPopulation))



