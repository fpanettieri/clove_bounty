from clove.network.bitcoin import Bitcoin


class iBank(Bitcoin):
    """
    Class with all the necessary iBank network information based on
    https://github.com/ibankgroup/ibank/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'ibank'
    symbols = ('IBANK', )
    seeds = ('46.166.168.156', '78.153.4.77')
    port = 7619


# Has no testnet
	
	