def main():
    #First array is the player's hand and the second array is the house's hand
    print(calculateProbability([1,9],[10]))


def calculateProbability(faceUpPlayerCards, faceUpHouseCards):
    points = 0
    total = 0
    for card in faceUpPlayerCards:
        points += card

    winCard = 21 - points 
    faceUpCards = len(faceUpPlayerCards) + len(faceUpHouseCards)
    nx = 0 

    for i in range(0, winCard):
        for card in faceUpPlayerCards:
            if(card == i):
                nx += 1

        for card in faceUpHouseCards:
            if(card == i):
                nx += 1   

        #nx is the number of cards that has the same value that you need to get 21 points
        #nv is the number of face up cards in the game
        p = (4-nx)
        p = p / (52 - faceUpCards)
        total += p

    return total * 100

if __name__ == '__main__':
    main()
