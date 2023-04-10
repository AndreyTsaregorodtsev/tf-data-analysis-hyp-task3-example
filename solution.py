import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 297386717 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    p = ttest_ind(x,y).pvalue
    if(p<0.09):
      return True
    else:
      return False
