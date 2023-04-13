import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

chat_id = 436734951 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    conv_control = x_success / x_cnt
    expected_sales = conv_control * y_cnt
    obs = [[x_success, x_cnt - x_success], [y_success, expected_sales - y_success]]
    chi2, p, dof, ex = chi2_contingency(obs, correction=False)
    alpha = 0.1
    critical_value = chi2.ppf(1 - alpha, dof)
    return chi2 > critical_value
