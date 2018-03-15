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
    if (data.startswith(purpose)): return 1
    else: return 0

trainingData = numpy.array([[string.ascii_lowercase for i in xrange(inputNodes)] for j in xrange(trainingDataAmount)])
trainingLabels = numpy.array(getLabel(trainingData))

numpy.random.seed(1)
inputLayerSynapses = [[]]
hiddenLayerOneSynapses =
hiddenLayerTwoSynapses

for k in xrange(trainingItterations):
    #Foward propegation
    inputLayerValues = trainingData
    hiddenLayerOneValues = numpy.dot(inputLayerValues, inputLayerSynapses)
    hiddenLayerTwoValues = numpy.dot(hiddenLayerOneValues, hiddenLayerOneSynapses)
    outputLayerValues = numpy.dot(hiddenLayerTwoValues, hiddenLayerTwoValues)
    #Back propegation
    outputLayerError = trainingLabels.T - outputLayerValues
    outputLayerDelta = outputError * sigmoid(outputValues, derivativeMode = True)
    hiddenLayerTwoError = numpy.dot(outputLayerDelta, hiddenLayerTwoSynapses.T)
    hiddenLayerTwoDelta = hiddenLayerTwoError * sigmoid(hiddenLayerTwoValues, derivativeMode = False)
    hiddenLayerOneError = numpy.dot(hiddenlayerTwoDelta, hiddenLayerOneSynapses.T)
    hiddenLayerTwoDelta = hiddenLayerOneError * sigmoid(hiddenLayerOneValues, derivativeMode = True)
