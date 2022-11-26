import random 
    
def check_rules(user_option,computer_option,user_wins,computer_wins):
  if user_option == computer_option:
    print('Empate')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('user wins')
      print('piedra gana a tijera')
      user_wins += 1
    else:
      print('computer wins')
      print('papel gana a piedra')
      computer_wins += 1
      
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('user wins')
      print('tijera gana a papel')
      user_wins += 1
    else:
      print('computer wins')
      print('piedra gana a tijera')
      computer_wins += 1
  
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('user wins')
      print('papel gana a piedra')
      user_wins += 1
    else:
      print('computer wins')
      print('tijera gana a papel')
      computer_wins += 1
  return user_wins,computer_wins
  
def choose():
  options = ('piedra','papel','tijera')
  
  user_option = input(' elige una opcion: piedra,papel o tijera -> ')
  user_option = user_option.lower()
    
  if not user_option in options:
    print('esa opcion no es valida')
    #continue
    return None,None 
    
  computer_option = random.choice(options)
    
  print(f'USER_OPTION -> {user_option}\n COMPUTER_OP -> {computer_option}')

  return user_option,computer_option



  

def run_game():
  user_wins = 0
  computer_wins = 0
  rounds = 1
  
  while True:
    if computer_wins == 2 or user_wins == 2:
      print('*'*25)
      print('Juego Terminado')
      print('*'*25)
      break
    
    print('*' * 25)
    print(f'ROUND {rounds}')
    print(f'puntos computador: {computer_wins} \npuntos usuario: {user_wins}')
    print('*' * 25)
  
    user_option, computer_option = choose()

    user_wins,computer_wins = check_rules(user_option,computer_option,user_wins,computer_wins)
  
    rounds += 1    

run_game()