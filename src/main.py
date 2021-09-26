from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()




def output_of_coins(Coin):
    print(Coin['name'], "current price:", Coin['current_price'], "$\n")

for i in range(1):
    ali = int(input("Type the number to show the top: "))
    ali1 = cg.get_coins_markets("usd")[:ali]
    for Сoin in ali1:
        output_of_coins(Сoin)
