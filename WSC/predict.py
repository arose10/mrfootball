from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
import numpy as np
import WSC
from WSC import Comm
import argparse

def predict(dataPath, modelName):
    X = []
    Y = []
    hasLabel = False

    # Load the data & split it by line breaks
    with open(dataPath) as t:
        new = t.read().split('\n')

    # Split the data again but this time by a tab. This will make 0 the sequence & 1 the label

    for i in range(len(new)):
        grab = new[i].split('\t')
        X.append(grab[0])

        # 
        if len(grab) > 1:
            Y.append(int(grab[1]))
            hasLabel = True

    # 
    dic = WSC.LoadSeq("config/SeqDomain.txt")
    test = WSC.GetAllSeqCount(X, dic)

    # 
    test = np.array(test)

    # 
    model = load_model(f"{modelName}.h5")

    # calculate predictions
    predictions = model.predict(test)

    err = 0

    # 
    for i in range(len(predictions)):
        if hasLabel:
            err += abs(Y[i] - int(round(predictions[i][0])))
            print(f'Ind: {i}\tSeq: {X[i]}\tPred: {predictions[i][0]}\tGuess: {int(round(predictions[i][0]))}\tLabel: {Y[i]}\tError: {abs(Y[i] - int(round(predictions[i][0])))}') 
        else:
            print(f'Ind: {i}\tSeq: {X[i]}\tPred: {predictions[i][0]}\tGuess: {int(round(predictions[i][0]))}') 

    # 
    if hasLabel:
        Comm(f'{round((1-(err/len(predictions)))*10000)/100}% Accurate')