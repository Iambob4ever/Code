#Conventions
#
#    all imports in a Python file should be at the start of the file
#    imports should be split into three groups:
#        imports from the standard library
#        imports from other libraries
#        imports within the project


#examples

 #   urlli = package
 #   urllib.request = module
 #   urllib.request.urlopen = function

#    sys = module
#    sys.path = object

#Typical imports
 #   import module1
 #   import module2
 #   from package3 import module3a, module3b
 #   from module4 import object4a, object4b
 #   from package5.module5 import object5a, object5b

#Specific examples

import os
import sys
from urllib import request, response
from math import sqrt, pi
from http.client import HTTPConnection, HTTPSConnection


#Short names
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

#Importing exerything from module 
    #Don't do this
 #   from math import *