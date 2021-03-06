from clove.network.bitcoin import Bitcoin


class Debitcoin(Bitcoin):
    """
    Class with all the necessary Debitcoin network information based on
    https://github.com/Debitcoin/debitcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'debitcoin'
    symbols = ('DBTC', )
    seeds = ("wallet.cryptolife.net",
             "explore.cryptolife.net",
             "seed1.cryptolife.net",
             "seed2.cryptolife.net",
             "seed3.cryptolife.net")
    port = 30112
	
# Has no testnet