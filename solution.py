import pandas as pd
import numpy as np
import scipy.stats as st

chat_id = 436734951 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    n1 = x_cnt
    n2 = y_cnt
    X1 = x_success
    X2 = y_success
    p1 = X1 / n1
    p2 = X2 / n2
    p_combined = (X1 + X2) / (n1 + n2)
    E1 = n1 * p_combined
    E2 = n2 * p_combined
    chi_squared_stat = ((X1 - E1)**2 / E1) + ((X2 - E2)**2 / E2)
    p_value = 1 - st.chi2.cdf(chi_squared_stat, 1)
    return p_value < 0.1
