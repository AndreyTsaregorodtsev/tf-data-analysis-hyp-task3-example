import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest

chat_id = 297386717 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    p = ztest(x,y)[1]
    if(p<0.09):
      return False
    else:
      return True
