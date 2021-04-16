#!/usr/bin/env python

import os # Модуль функций для работы с операционной системой, не зависящие от используемой операционной системы
import collections #Модуль специализированных типов данных, на основе словарей , кортежей , множеств , списков
import math # Библиотека математических функций
import json
import requests
import numpy as np
import pickle

from flask import Flask
from flask import request

from tensorflow.keras import utils # Утилиты для to_categorical
from tensorflow.keras.models import load_model # загрузка сохраненных моделей
