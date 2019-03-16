# Hack the Burgh 2019 Liana Ahmed, Kim Stonehouse, Mo Javad, Anu Chowdhury
import numpy as np
from sortData import *

class main:

    dir = ""

    def __init__(self, dir):
        self.dir = dir

        with open(dir, "r") as all:
            file = all.read()

