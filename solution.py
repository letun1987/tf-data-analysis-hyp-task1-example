import pandas as pd
import numpy as np


chat_id = 436734951 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.1
    count = [x_success, y_success]
    nobs = [x_cnt, y_cnt]
    _, p_val = proportions_ztest(count, nobs, alternative='larger')
    return p_val < alpha
