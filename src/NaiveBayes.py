import sys

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
currCount_C1 = 40
currCount_C2 = 58
currCount_C3 = 12
vocabularyLength = 11

#Empty arrays, same size as the hand
class1ProbArray = list()
class2ProbArray = list()
class3ProbArray = list()

def main():
    args = sys.argv
    cardArray = list()

    for element in args:
        if element != args[0]:
            cardArray.append(int(element))

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

        class1ProbArray.append( (currCount_W_C + 1) / (currCount_C1 + vocabularyLength))

        currCount_W_C = 0

        #Class 2
        for i in range(11, 17):
            for card in classTable[str(i)]:
                if card == currentCard:
                    currCount_W_C += 1

        class2ProbArray.append( (currCount_W_C + 1) / (currCount_C2 + vocabularyLength))

        currCount_W_C = 0

        #Class 3
        for i in range(18, 21):
            for card in classTable[str(i)]:
                if card == currentCard:
                    currCount_W_C += 1

        class3ProbArray.append( (currCount_W_C + 1) / (currCount_C3 + vocabularyLength))


        currCount_W_C = 0
        cardArrayIndex += 1


    print('Conditional probabilities for hand: \'' + str(cardArray) + '\'\n')
    print('Class 1: ' + str(class1ProbArray))
    print('Class 2: ' + str(class2ProbArray))
    print('Class 3: ' + str(class3ProbArray))

    #Choosing a class

    probArray1Sum = 1
    probArray2Sum = 1
    probArray3Sum = 1

    for element in class1ProbArray:
        probArray1Sum *= element

    for element in class2ProbArray:
        probArray2Sum *= element

    for element in class3ProbArray:
        probArray3Sum *= element

    probClass1 = class1Probability * probArray1Sum
    probClass2 = class1Probability * probArray2Sum
    probClass3 = class1Probability * probArray3Sum

    chosenClass = 1
    maxClass = probClass1

    if probClass2 > maxClass:
        maxClass = probClass2
        chosenClass = 2

    if probClass3 > maxClass:
        maxClass = probClass3
        chosenClass = 3

    print('\nChoosing a class:')
    print('Class 1: ' + str(probClass1))
    print('Class 2: ' + str(probClass2))
    print('Class 3: ' + str(probClass3))
    print('\nChosen class: \'' + str(chosenClass) + '\'')
    print('\nMax class: \'' + str(maxClass) + '\'')


    return chosenClass, maxClass


if __name__ == '__main__':
    main()
