"""
Enmum for the citrex package
"""

from enum import Enum


class Environment(Enum):
    """
    Enum for the environment of the client.
    """

    PROD = "prod"
    TESTNET = "testnet"
    DEVNET = "local"


class OrderSide(Enum):
    """
    Enum for the order side.
    """

    BUY = True
    SELL = False


class OrderType(Enum):
    """
    Enum for the order type.
    """

    LIMIT = 0
    LIMIT_MAKER = 1
    MARKET = 2


class SupportedChains(Enum):
    """
    Enum for supported chains
    """

    ARBITRUM = "ARBITRUM"
    BLAST = "BLAST"
    SEI = "SEI"
    CUSTOM = "CUSTOM"


class TimeInForce(Enum):
    """
    Enum for the time in force.
    """

    GTC = 0
    FOK = 1
    IOC = 2
