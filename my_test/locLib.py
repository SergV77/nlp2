#!/usr/bin/env python

import os # Модуль функций для работы с операционной системой, не зависящие от используемой операционной системы
import collections #Модуль специализированных типов данных, на основе словарей , кортежей , множеств , списков
import math # Библиотека математических функций
import numpy as np # Библиотека работы с массивами
import requests
import json
import pickle

from tensorflow.keras import utils # Утилиты для to_categorical
from tensorflow.keras.models import load_model # загрузка сохраненных моделей


from sklearn.preprocessing import LabelEncoder, StandardScaler # Функции для нормализации данных
from sklearn import preprocessing # Пакет предварительной обработки данных
from sklearn.model_selection import train_test_split

from flask import Flask
from flask import request