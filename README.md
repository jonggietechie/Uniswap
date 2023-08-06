# Uniswap Arbitrage Calculation

This repository contains a Python implementation of an arbitrage calculation for two Uniswap pools, Pool A and Pool B. The code allows users to find potential arbitrage opportunities between the two pools and perform non-blocking benchmarking for concurrent arbitrage calculations.

# UniswapPool Class

The UniswapPool class represents a Uniswap pool with DAI and ETH balances. It includes the following methods:

<ol>

<li>__init__(self, dai_balance, eth_balance): Initializes the Uniswap pool with the provided DAI and ETH balances and sets the swap fee to 0.3%.</li>
    
<li>get_relative_price(self): Calculates and returns the relative price of ETH in terms of DAI for the pool.</li>

<li>add_liquidity(self, dai_amount, eth_amount): Adds liquidity to the pool by increasing the DAI and ETH balances by the specified amounts.</li>

<li>remove_liquidity(self, liquidity_tokens): Removes liquidity from the pool by providing the number of liquidity tokens. It returns the amount of DAI and ETH removed from the pool.</li>

<li>calculate_swap(self, dai_amount_in): Calculates the amount of ETH obtained by swapping a given amount of DAI in the pool, considering the swap fee.</li>
</ol>

# ArbitrageOpportunity Class

The ArbitrageOpportunity class facilitates finding arbitrage opportunities between Pool A and Pool B. It includes the following methods:

<ol>
<li>__init__(self, pool_a, pool_b): Initializes the class with references to Pool A and Pool B.</li>

<li>find_arbitrage_opportunity(self, dai_amount_in): Calculates the potential arbitrage profit in ETH for a given amount of DAI.</li>

<li>find_arbitrage_opportunity_non_blocking(self, dai_amount_in): Simulates a non-blocking calculation by adding a 0.1-second delay before calling the regular find_arbitrage_opportunity method. This method can be used to benchmark the non-blocking performance.</li>
</ol>

# Test Cases

<ol>
<li>The test cases in the if __name__ == "__main__": block showcase the functionalities of the implemented classes:</li>

<li>Test swapping 100 DAI to ETH in Pool A: This test simulates a swap of 100 DAI to ETH in Pool A and prints the resulting amount of ETH obtained.</li>

<li>Test finding arbitrage opportunity: This test calculates the potential arbitrage profit in ETH by comparing the amount of ETH obtained through swaps in Pool A and Pool B.</li>

<li>Test for benchmarking non-blocking calculation: This test demonstrates the benchmarking of the non-blocking calculation by measuring the time it takes to perform concurrent non-blocking calculations for 100 iterations using timeit.</li>
</ol>

# How to Use

<ol>
<li> Clone the repository or copy the provided code into a Python script.</li>

<li>Modify the initial DAI and ETH balances for Pool A and Pool B (X1, Y1, X2, Y2) to match your specific Uniswap pools.</li>

<li>Update the liquidity amounts added to Pool A and Pool B in the test cases as needed.</li>

<li>Run the script using "python uniswap.py" to execute the test cases and see the results.</li>
</ol>
