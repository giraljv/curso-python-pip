def getpopulation():
  keys = ['col','bol']
  values = [300,400]
  return keys,values

Variable = 'pais'

def population_bycountry(data,country):
  result = list(filter(lambda item: item['country'] == country,data))
  return result

data = [
  {
    'country': 'Colombia',
    'Population': 500
  },
  {
    'country': 'Peru',
    'Population': 250
  },
  {
    'country': 'Argentina',
    'Population': 350
  }
]