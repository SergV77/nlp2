#!flask/bin/python
from locLib import *

def concept2Indexes(concepts, vocabulary, maxConceptCount):
    '''
      concept2Indexes - Функция создание индексов концептов
      вход:
        concepts - концепты
        vocabulary - словарь концептов
        maxConceptCount - максимальное количество всех концептов словаря
      выход:
        список индексов всх концептов
    '''

    conceptsIndexes = []

    for concept in concepts:
        conceptIndex = 0
        conceptInVocabulary = concept in vocabulary

        if (conceptInVocabulary):
            index = vocabulary[concept]
            if (index < maxConceptCount):
                conceptIndex = index

        conceptsIndexes.append(conceptIndex)

    return conceptsIndexes


def changeXTo01(trainVector, conceptsCount):
    '''
        changeXTo01 - Функция создания words of bag (преобразование одного короткого вектора
        в вектор из 0 и 1)
        вход:
            trainVector - обучающий ветор
            conceptsCount - длина библиотеки концептов
        выход:
            words of bag xTrain, yTrain
    '''

    out = np.zeros(conceptsCount)
    for x in trainVector:
        out[x] = 1
    return out

def changeSetTo01(trainSet, conceptsCount):
    '''
        changeSetTo01 - Функция создания words of bag обучающей и проверочной выборки
        (преобразование одного короткого вектора в вектор из 0 и 1)
        вход:
            trainVector - обучающий ветор
            conceptsCount - длина библиотеки концептов
        выход:
            массив words of bag xTrain, yTrain
    '''

    out = []
    for x in trainSet:
        out.append(changeXTo01(x, conceptsCount))
    return np.array(out)



