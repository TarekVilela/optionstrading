import numpy as np
import pandas as pd
from scipy.stats import norm
from aux_functions import *

N = norm.cdf
N_ = norm.pdf


class BlackandScholes:
    '''
    Black and Scholes class.
    Calculate option price.
    Calculate implied volatility
    '''

    def __init__(self, asset, option):
        self.asset = asset
        self.option = option

    def black_and_scholes(self, St, K, sigma, T, r, t=0):
        if self.option.type == 'call':
            return N(d1(St, K, sigma, T, t, r)) * St - N(d2(St, K, sigma, T, t, r)) * K * np.exp(-r * (T - t))
        
        elif self.option.type == 'put':
            return N(-d2(St, K, sigma, T, t, r)) * K * np.exp(-r * (T - t)) - N(-d1(St, K, sigma, T, t, r)) * St

    def price(self, T, r, t=0):
        return self.black_and_scholes(self.asset.St, self.option.K, self.asset.sigma, T, r, t)

    def change_with_vol(self, T, r, t=0):
        sigmas = np.arange(0.005, 0.70, 0.005)

        ps = [self.price(s, T, r, t) for s in sigmas]

        df = pd.DataFrame()
        df['sigmas'] = sigmas
        df['price'] = ps

        return df.set_index('sigmas')

    def smiles(self, T, r, t=0):
        pass