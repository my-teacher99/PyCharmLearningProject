import os
import sys
import time
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
import websockets as wbs

class TradinfBot:
    api_key = 'CF4rx16U8jnpNING4EPdcQwD4lY9hVV88NEeFOrU4MqYi7nOiw0vbWjK7uRzBNob'
    api_secret = 'wcUqJR6M5C3vl2rLOl4Nb9fRl8igT8s3Iv9EEdnO8pTfXlpPAzQnTERAl4dwa3uj'
    Client.API_URL='https://testnet.binance.vision/api'
    me = Client(api_key, api_secret)
    Flag = False

    def __init__(self, coin_symbol, mony):

        self.aziz_bot(coin_symbol, mony)


    def aziz_bot(self, coin_symbol, amount):
        """
        This function make a trading deal, and it will sell if the price get more 1% or down 5%
        This idea called (compounded interest). """

        order_result = self.me.create_order(
            symbol=coin_symbol,
            side='BUY',
            type='MARKET',
            quantity=amount
        )
        buy_price = float("{:.2f}".format(float(order_result['fills'][0]['price'])))
        print(f"Buy Price of ETH: {buy_price}")
        print(f'OUR TARGET {buy_price + (buy_price * 0.0005)}')
        print(f'You have {me.get_asset_balance(asset=coin_symbol)}')

        while True:

            new_price = float("{:.2f}".format(float(me.futures_mark_price(symbol='ETHUSDT')['markPrice'])))
            if new_price >= buy_price + (buy_price * 0.0005):
                sell_price = me.create_order(
                    symbol=coi0n_symbol,
                    side='SELL',
                    type='MARKET',
                    quantity=amount
                )
                print(f"Target price atchieved for {coin_symbol} !. price selling is : {sell_price} $")
                finish_deal = True
                break

            if new_price <= buy_price - (buy_price * 0.03):
                sell_price = me.create_order(
                    symbol=coin_symbol,
                    side='SELL',
                    type='MARKET',
                    quantity=amount
                )
                print(print(f"Price of {coin_symbol} down 5%!. Sorry I sell on price: {sell_price} $ "))
                finish_deal = True
                break
            else:
                print(f"price: {new_price}")
                time.sleep(0.5)


    def fishing_position(self, coin):
        """
        This function will try to get the best time to enter the trading deal

        :param coin: The coin that we will trying to get best position to buy
        :return: True if the position good to buy

        """




#mony = input("How much your mony? ")
#number_of_bot = input('How many coin will divided on your deal? ')

#info_list = me.get_account()['balances']
#for coin in info_list:
#    if coin['asset'] == 'USDT':
#        print(f'You have : {coin["free"]} $USDT')
#        quantity = coin['free']

#me.get_asset_balance(asset='BTC')
