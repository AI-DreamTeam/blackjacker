classTable = { '3' : [1, 2],
               '4' : [1, 3],
               '5' : [1, 4, 2, 3],
               '6' : [1, 5, 2, 4],
               '7' : [1, 6, 2, 5, 3, 4],
               '8' : [1, 7, 2, 6, 3, 5],
               '9' : [1, 8, 2, 7, 3, 6, 4, 5],
               '10' : [1, 9, 2, 8, 3, 7, 4, 6],
               '11' : [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],
               '12' : [1, 11, 2, 10, 3, 9, 4, 8, 5, 7],
               '13' : [2, 11, 3, 10, 4, 9, 5, 8, 6, 7],
               '14' : [3, 11, 4, 10, 5, 9, 6, 8],
               '15' : [4, 11, 5, 10, 6, 9, 7, 8],
               '16' : [5, 11, 6, 10, 7, 9],
               '17' : [6, 11, 7, 10, 8, 9],
               '18' : [7, 11, 8, 10],
               '19' : [8, 11, 9, 10],
               '20' : [9, 11],
               '21' : [10, 11]
}

class1Probability = 8 / 19
class2Probability = 7 / 19
class3Probability = 4 / 19
currCount_C = 40
vocabularyLength = 11

#Empty arrays, same size as the hand
class1ProbArray = list()
class2ProbArray = list()
class3ProbArray = list()

def main():
    cardArray = 1,4,1
    naiveBayes(cardArray)

def naiveBayes(cardArray):
    cardArrayIndex = 0
    classTableIndex = 0
    currCount_W_C = 0

    currentCard = cardArray[cardArrayIndex]

    #Checks the conditional probabilities
    while True:
        if (cardArrayIndex) > len(cardArray) - 1:
            break

        currentCard = cardArray[cardArrayIndex]

        #Class 1
        for i in range(3, 10):
            for card in classTable[str(i)]:
                if card == currentCard:
                    currCount_W_C += 1

        class1ProbArray.append( (currCount_W_C + 1) / (currCount_C + vocabularyLength))

        currCount_W_C = 0

        #Class 2
        for i in range(11, 17):
            for card in classTable[str(i)]:
                if card == currentCard:
                    currCount_W_C += 1

        class2ProbArray.append( (currCount_W_C + 1) / (currCount_C + vocabularyLength))

        currCount_W_C = 0

        #Class 3
        for i in range(18, 21):
            for card in classTable[str(i)]:
                if card == currentCard:
                    currCount_W_C += 1

        class3ProbArray.append( (currCount_W_C + 1) / (currCount_C + vocabularyLength))


        currCount_W_C = 0
        cardArrayIndex += 1


    print(class1ProbArray)
    print(class2ProbArray)
    print(class3ProbArray)


if __name__ == '__main__':
    main()
