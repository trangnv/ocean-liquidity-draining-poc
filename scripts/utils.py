import brownie


def toBase18(amt: float) -> int:
    return int(amt * 1e18)


def fromBase18(amt_base: int) -> float:
    return amt_base / 1e18


DEPLOYER = brownie.network.accounts[0]
FEE_COLLECTOR = brownie.network.accounts[1]
PUBLISHER = brownie.network.accounts[2]
ATTACKER = brownie.network.accounts[3]
