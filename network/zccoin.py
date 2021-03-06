from clove.network.bitcoin import Bitcoin


class ZcCoin(Bitcoin):
    """
    Class with all the necessary ZcCoin network information based on
    https://github.com/zccoin/zccoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'zccoin'
    symbols = ('ZCC', )
    seeds = ("seed1.zhaocaibi.com",
             "seed2.zhaocaibi.com",
             "seed3.zhaocaibi.com")
    port = 10583
	
