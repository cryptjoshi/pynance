
from trading import Trading
from utils import readConfig,green,red


def main():
    green('---------------------')
    green('Pynance V.1 by CJ')
    green('---------------------')
    config = readConfig(r'Config.txt')
    trading = Trading(config) #{'User':'Master','token':'xxxxxxxxxx','api_key':'yyyyyyyyyyy','api_secret':'zzzzzzzzzzz'})
    trading.sync_time()
    trading.balance()

 
 