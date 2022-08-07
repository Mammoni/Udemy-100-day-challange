from replit import clear
import art

run_program = True
question = "yes"
bidders  =  {}
winner = 0
winner_name = ""

def add_bidder(name, bid):
  bidders[name] = int(bid)

def who_win(bidders,winner,winner_name):  
  for bid in bidders.keys():
    if bidders[bid] > winner:
      winner = bidders[bid]
      winner_name = bid
  print(f'The winner is {winner_name} with total money {winner}$')
    
print(art.logo)
while run_program != False:
  name = input("name: ")
  bid = input("bid: ")
  add_bidder(name,bid)
  question = input("add another bidder y/n?: ")
  if question.lower() == "no" or question.lower() == "n":
    run_program = False
    clear()
    who_win(bidders,winner,winner_name)
  elif question.lower() == "yes" or question.lower() == "y":
    run_program = True
    clear()
  
    

