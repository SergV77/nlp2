#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
def test():
    return 'Мое Flask приложение в докере'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
