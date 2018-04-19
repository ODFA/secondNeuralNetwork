import numpy
import random
import string
#Initializing hyperparamaters
inputLayerNodes = 7
hiddenLayerOneNodes = 5
hiddenLayerTwoNodes = 5
outputLayerNodes = 1
purpose = str(raw_input("Value 1: ") + raw_input("Value 2: ") + raw_input("Value 3: "))
trainingDataAmount = 10000
trainingItterations = 10000

def sigmoid(point, derivativeMode = False):
    if (derivativeMode): return (point / (1 - point))
    else: return (1 / (1 + numpy.exp(-point)))

def getLabel(data):
    characters = "abcdefghijklmnopqrstuvwxyz"
    outputString = ""
    for i in data:
        for j in i:
            for k in xrange(len(j)):
                if (j[k] == 1):
                    outputString += characters[k]
                    break
    if (outputString.startswith(purpose)): return 1
    else: return 0
#TEMP
def hotEncode(string):
    characters = "abcdefghijklmnopqrstuvwxyz"
    #array = numpy.array([numpy.zeros(26) for i in xrange(26)])
    #for j in xrange(len(array)): array[j][characters.index(string[j])] = 1
    #return array
    #print(numpy.eye(26)[characters.index(list(string))])
    numbers = [characters.index(i) for i in string]
    return numpy.eye(26)[numbers]
trainingData = numpy.array([hotEncode([string.ascii_lowercase for i in xrange(inputLayerNodes)]) for j in xrange(trainingDataAmount)])
trainingLabels = numpy.array(getLabel(trainingData))

numpy.random.seed(1)
inputLayerSynapses = numpy.random.random((inputLayerNodes, hiddenLayerOneNodes)) * 2 - 1
hiddenLayerOneSynapses = numpy.random.random((hiddenLayerOneNodes, hiddenLayerTwoNodes)) * 2 - 1
hiddenLayerTwoSynapses = numpy.random.random((hiddenLayerTwoNodes, outputLayerNodes)) * 2 - 1

for k in xrange(trainingItterations):
    #Foward propegation
    inputLayerValues = trainingData
    hiddenLayerOneValues = sigmoid(numpy.dot(inputLayerValues, inputLayerSynapses))
    hiddenLayerTwoValues = sigmoid(numpy.dot(hiddenLayerOneValues, hiddenLayerOneSynapses))
    outputLayerValues = sigmoid(numpy.dot(hiddenLayerTwoValues, hiddenLayerTwoValues))
    #Back propegation
    outputLayerError = trainingLabels.T - outputLayerValues
    outputLayerDelta = outputError * sigmoid(outputValues, derivativeMode = True)
    hiddenLayerTwoError = numpy.dot(outputLayerDelta, hiddenLayerTwoSynapses.T)
    hiddenLayerTwoDelta = hiddenLayerTwoError * sigmoid(hiddenLayerTwoValues, derivativeMode = True)
    hiddenLayerOneError = numpy.dot(hiddenlayerTwoDelta, hiddenLayerOneSynapses.T)
    hiddenLayerOneDelta = hiddenLayerOneError * sigmoid(hiddenLayerOneValues, derivativeMode = True)

    inputLayerSynapses += numpy.dot(inputValues.T, hiddenLayerOnelta)
    hiddenLayerOneSynapses += numpy.dot(hiddenLayerOneValues.T, hiddenlayerOneDelta)
    hiddenLayerTwoSynapses += numpy.dot(hiddenLaeyerTwoValues.T, hiddenlayerTwoDelta)

while (True):
    inputLayerValues = [raw_input("value %i" % i) for i in xrange(inputNodes)]
    hiddenLayerOneValues = numpy.dot(inputLayerValues)
