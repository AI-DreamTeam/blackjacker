import sys

classTable = {
'2':
[],
'3':
[1,1,1],
'4':
[1,2,1],
'5':
[1,3,1,2,2,1],
'6':
[1,4,1,2,3,1,2,2,2],
'7':
[1,5,1,2,4,1,3,3,1,2,3,2],
'8':
[1,6,1,2,5,1,3,4,1,2,4,2,3,3,2],
'9':
[1,7,1,2,6,1,3,5,1,4,4,1,2,5,2,3,4,2,3,3,3],
'10':
[1,8,1,2,7,1,3,6,1,4,5,1,2,6,2,3,5,2,4,4,2,3,4,3],
'11':
[1,9,1,2,8,1,3,7,1,4,6,1,5,5,1,2,7,2,3,6,2,4,5,2,3,5,3,4,4,3],
'12':
[1,10,1,2,9,1,3,8,1,4,7,1,5,6,1,2,8,2,3,7,2,4,6,2,5,5,2,3,6,3,4,5,3,4,4,4],
'13':
[1,11,1,2,10,1,3,9,1,4,8,1,5,7,1,6,6,1,2,9,2,3,8,2,4,7,2,5,6,2,3,7,3,4,6,3,5,5,3,4,5,4],
'14':
[2,11,1,3,10,1,4,9,1,5,8,1,6,7,1,2,10,2,3,9,2,4,8,2,5,7,2,6,6,2,3,8,3,4,7,3,5,6,3,4,6,4,5,5,4],
'15':
[3,11,1,4,10,1,5,9,1,6,8,1,7,7,1,2,11,2,3,10,2,4,9,2,5,8,2,6,7,2,3,9,3,4,8,3,5,7,3,6,6,3,4,7,4,5,6,4,5,5,5],
'16':
[4,11,1,5,10,1,6,9,1,7,8,1,3,11,2,4,10,2,5,9,2,6,8,2,7,7,2,3,10,3,4,9,3,5,8,3,6,7,3,4,8,4,5,7,4,6,6,4,5,6,5],
'17':
[5,11,1,6,10,1,7,9,1,8,8,1,4,11,2,5,10,2,6,9,2,7,8,2,3,11,3,4,10,3,5,9,3,6,8,3,7,7,3,4,9,4,5,8,4,6,7,4,5,7,5,6,6,5],
'18':
[6,11,1,7,10,1,8,9,1,5,11,2,6,10,2,7,9,2,8,8,2,4,11,3,5,10,3,6,9,3,7,8,3,4,10,4,5,9,4,6,8,4,7,7,4,5,8,5,6,7,5,6,6,6],
'19':
[7,11,1,8,10,1,9,9,1,6,11,2,7,10,2,8,9,2,5,11,3,6,10,3,7,9,3,8,8,3,4,11,4,5,10,4,6,9,4,7,8,4,5,9,5,6,8,5,7,7,5,6,7,6],
'20':
[8,11,1,9,10,1,7,11,2,8,10,2,9,9,2,6,11,3,7,10,3,8,9,3,5,11,4,6,10,4,7,9,4,8,8,4,5,10,5,6,9,5,7,8,5,6,8,6,7,7,6],
'21':
[9,11,1,10,10,1,8,11,2,9,10,2,7,11,3,8,10,3,9,9,3,6,11,4,7,10,4,8,9,4,5,11,5,6,10,5,7,9,5,8,8,5,6,9,6,7,8,6,7,7,7]
}

class1Probability = 8 / 19
class2Probability = 7 / 19
class3Probability = 4 / 19
currCount_C1 = 93
currCount_C2 = 309
currCount_C3 = 210
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

    if not sum(cardArray) > 21:
        naiveBayes(cardArray)
    else:
        print('Hand cannot be more than 21! Try with a different hand.\n\n')

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

    probArray1Acc = 1
    probArray2Acc = 1
    probArray3Acc = 1

    for element in class1ProbArray:
        probArray1Acc *= element

    for element in class2ProbArray:
        probArray2Acc *= element

    for element in class3ProbArray:
        probArray3Acc *= element

    probClass1 = class1Probability * probArray1Acc
    probClass2 = class1Probability * probArray2Acc
    probClass3 = class1Probability * probArray3Acc

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
