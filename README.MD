# POC of liquidity draining attack on Ocean data pools

Transaction example
https://polygonscan.com/tx/0xbd21e9179cb7555137f0aff9f844f454a4c5e234214d41b5d326b4a098875d9d


## Intended behaviors of liquidity pool
- Buying
- Selling

## Attack steps
- Staking Ocean in a data pool
- Buying datatokens
- Unstaking Ocean
- Selling datatokens and take profit

## Run
- Install [Brownie](https://eth-brownie.readthedocs.io/en/stable/toctree.html)
- Run script
```bash
>>> brownie run scripts/exploit.py
Attacker ocean balance before attack 1000000.0
Attacker ocean balance after attack 1007707.1103890418
```
- Change the fee set up [here](https://github.com/trangnv/ocean-liquidity-draining-poc/blob/c4bdbb6bf7178e175e53ad2b57880fe8b77ff6cf/scripts/exploit.py#L207) to e.g. 0.1 (10%) and the exploit is not profitable anymore

## Why staking - unstaking cause issues
Staking makes DT supply increase,less slippage for buying
Unstaking decrease DT supply but spot price remain unchanged


## Next steps
- Track data during the attack
- Parameterization, how to get the most from the exploit
- Write attacking contract
