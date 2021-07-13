import numpy as np
import pandas as pd
from scipy.stats import norm
from aux_functions import *

N = norm.cdf
N_ = norm.pdf

class Greeks:
    def __init__(self, option) -> None:
        '''
        Initialize Greeks
        option: Option object
        '''

        self.option = option
        self.d1 = d1()
        self.d2 = d2()

    @property
    def Delta(self):
        if self.option.type == 'call':
            return N(self.d1)

        elif self.option.type == 'put':
            return N(self.d1) - 1

    @property
    def Gamma(self):
        return N_(self.d1) / (self.option.asset.St * self.option.asset.sigma * np.sqrt(self.option.T - self.option.t))

    @property
    def Vega(self):
        return self.option.asset.St * N_(self.d1) * np.sqrt(self.option.T - self.option.t)

    @property
    def Theta(self):
        first_term = -(self.option.asset.St * N_(self.d1) * self.option.asset.sigma) / (2 * np.sqrt(self.option.T - self.option.t))
        second_term = self.option.r * self.option.K * np.exp(-self.option.r * (self.option.T - self.option.t))
        
        if self.option.type == 'call':
            return first_term - second_term * N(self.d2)

        elif self.option.type == 'put':
            return first_term + second_term * N(-self.d2)

    @property
    def Rho(self):
        first_term = self.option.K * (self.option.T - self.option.t) * np.exp(-self.option.r * (self.option.T - self.option.t))

        if self.option.type == 'call':
            return first_term * N(self.d2)

        elif self.option.type == 'put':
            return -first_term * N(-self.d2)