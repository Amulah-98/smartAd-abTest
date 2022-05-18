import sys
import os
import unittest
import numpy as np
import pandas as pd
import pandas.api.types as ptypes

sys.path.insert(0, '../scripts/')
sys.path.append(os.path.abspath(os.path.join('scripts')))

from data_info import dataframeInfo
from data_preProcess import data_preProcess


