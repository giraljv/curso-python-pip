import utils
import random

data = [
  {
    'country': 'Colombia',
    'Population': 500
    },
  {
    'country': 'suiza',
    'Population': 250
    }
      ]

def run():

  #=========================================#
  keys,values = utils.getpopulation()
  
  print(keys,values)
  #=========================================#
  print(utils.Variable)
  #=========================================#
  country = input('escribe un pais')
  population = utils.population_bycountry(data,country)
  print(population)


if __name__ == '__main__':
  run()