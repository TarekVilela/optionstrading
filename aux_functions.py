import numpy as np
from scipy.stats import norm

N = norm.cdf
N_ = norm.pdf


def d1(St, K, sigma, T, t, r) -> float:
    '''

    Calculates d1
    
    St: asset spot price
    K: strike price
    T: time to expiration
    t: time (default is 0)
    r: continuously compoud interest rate
    '''
    
    first_term = 1 / (sigma * np.sqrt(T - t))
    second_term = np.log(St / K) + (r + sigma**2 / 2 * (T - t))

    return first_term * second_term
    

def d2(St, K, sigma, T, t, r) -> float:
    '''

    Calculates d2
    
    St: asset spot price
    K: strike price
    T: time to expiration
    t: time (default is 0)
    r: continuously compoud interest rate
    '''

    return d1(St, K, sigma, T, t, r) - sigma * np.sqrt(T - t)