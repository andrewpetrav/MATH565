import random

wins=0
losses=0

def craps(n):
    global wins, losses
    #simulate craps n times
    for i in range(n):
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        result=die1+die2
        if result==7 or result==11:
            wins+=1 #winner! :)
        elif result==2 or result==3 or result==12:
            losses+=1 #loser :(
        else:
            while True:
                die1=random.randint(1,6)
                die2=random.randint(1,6)
                result2=die1+die2
                if result2==result:
                    wins+=1 #winner! :)
                    break
                elif result2==7:
                    losses+=1 #loser :(
                    break

           
craps(30)
print(wins)
print(losses)
print("Win Probability: ",wins/(wins+losses))