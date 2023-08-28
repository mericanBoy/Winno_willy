# Write your code here :-)
print('Welcome to Wino Willy!')
print('You are a vagrant named willy and you have to get to\nthe rehab center before midnight!')

choice_one = input('You are on your way to the center and\ncome accross an alleyway, go IN or CONTINUE? ')

if choice_one.lower() == 'continue':
  print('You continue down the street on your\nway to the center')

  choice_two = input('You are approached by a dealer, he offers\nyou some PRIMO DRUGS, do you ACCEPT or CONTINUE to the center? ')

  if choice_two.lower() == 'continue':
    print('You brush past the dealer and continue\nto the center')

    choice_three = input('You come before a POLICE STATION, a BAR\nand the REHAB CENTER, which do you enter? ')
    if choice_three.lower() == 'rehab' or choice_three.lower() == 'rehab center':
      print('Congrats! you made it to the center! YOU WIN!')
    elif choice_three.lower() == 'bar':
      print('You enter the bar, after drinking 62 beers\nyou start a barfight in which you die. GAME OVER')


    else:
      print('You enter the police station, there you are\narrested due to your 62 outstanding\nwarrants. GAME OVER')
  else:
    print("You overdose and don't make it to\nthe center, GAME OVER")
else:
  print('You get mugged by another vagrant, GAME OVER')


