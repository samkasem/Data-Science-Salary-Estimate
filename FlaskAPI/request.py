# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 09:30:24 2022

@author: Ahmed.k
"""

import requests 
from data_input import data_in

URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": data_in}

r = requests.get(URL,headers=headers, json=data) 

r.json()