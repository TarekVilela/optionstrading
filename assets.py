import numpy as np
import pandas as pd

class Asset:
    def __init__(self, St: float, sigma: float) -> None:

        '''
        Initialize Asset
        St: spot price
        t: current time
        sigma: annualized volatility
        '''

        self.St = St
        self.sigma = sigma

    def payoff(self, *args):
        start = 0
        end = self.St * 2 + 0.01

        St_vector = np.arange(start, end, 0.01)
        df = pd.DataFrame()
        df['St'] = St_vector

        df['payoff'] = [p - self.St for p in St_vector]

        return df.set_index('St')


class Option:
    def __init__(self, K: float,
                 call_or_put: str, 
                 kind: str = 'european') -> None:

        '''

        Initialize Option
        K: strike price
        call_or_put: option type - call or put 
        kind: european or american (default is european)
        '''

        self.K = K
        self.type = call_or_put
        self.kind = kind

    def payoff(self, premium=0, end=0):
        start = 0

        if end == 0:
            end = self.K * 2 + 0.01

        print(end)
        St_vector = np.arange(start, end, 0.01)
        df = pd.DataFrame()
        df['St'] = St_vector

        if self.type == 'call':
            df['payoff'] = [max(0, p - self.K) - premium for p in St_vector]

            return df.set_index('St')

        if self.type == 'put':
            df['payoff'] = [max(0, self.K - p) - premium for p in St_vector]

            return df.set_index('St')


class EuropeanCall(Option):
    def __init__(self, K):
        Option.__init__(self, K, call_or_put='call', kind='european')


class EuropeanPut(Option):
    def __init__(self, K):
        Option.__init__(self, K, call_or_put='put', kind='european')


class AmericanCall(Option):
    def __init__(self, K):
        Option.__init__(self, K, call_or_put='call', kind='american')
        

class AmericanPut(Option):
    def __init__(self, K):
        Option.__init__(self, K, call_or_put='put', kind='american')