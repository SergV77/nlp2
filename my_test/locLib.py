#!/usr/bin/env python

import os # Модуль функций для работы с операционной системой, не зависящие от используемой операционной системы
import collections #Модуль специализированных типов данных, на основе словарей , кортежей , множеств , списков
import math # Библиотека математических функций
import requests
import json
import pickle

from flask import Flask
from flask import request

from sklearn.model_selection import train_test_split
