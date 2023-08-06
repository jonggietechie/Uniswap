import time
import timeit

class UniswapPool:
    def __init__(self, dai_balance, eth_balance):
        self.dai_balance = dai_balance
        self.eth_balance = eth_balance
        self.swap_fee = 0.003  # 0.3% swap fee

    def get_relative_price(self):
        return self.eth_balance / self.dai_balance

    def add_liquidity(self, dai_amount, eth_amount):
        self.dai_balance += dai_amount
        self.eth_balance += eth_amount

    def remove_liquidity(self, liquidity_tokens):
        if liquidity_tokens > 0:
            liquidity_ratio = liquidity_tokens / (self.dai_balance * self.eth_balance)
            dai_amount = self.dai_balance * liquidity_ratio
            eth_amount = self.eth_balance * liquidity_ratio
            self.dai_balance -= dai_amount
            self.eth_balance -= eth_amount
            return dai_amount, eth_amount

    def calculate_swap(self, dai_amount_in):
        if dai_amount_in <= self.dai_balance:
            dai_amount_in_after_fee = dai_amount_in * (1 - self.swap_fee)
            eth_amount_out = self.eth_balance - (self.dai_balance / (self.dai_balance + dai_amount_in_after_fee)) * self.eth_balance
            return eth_amount_out
        return 0


class ArbitrageOpportunity:
    def __init__(self, pool_a, pool_b):
        self.pool_a = pool_a
        self.pool_b = pool_b

    def find_arbitrage_opportunity(self, dai_amount_in):
        eth_amount_out_pool_a = self.pool_a.calculate_swap(dai_amount_in)
        eth_amount_in_pool_b = self.pool_b.calculate_swap(dai_amount_in)

        if eth_amount_out_pool_a > eth_amount_in_pool_b:
            return eth_amount_out_pool_a - eth_amount_in_pool_b

        return 0
    def find_arbitrage_opportunity_non_blocking(self,dai_amount_in):
        time.sleep(0.1) #To simulate non-blocking behavior with delay
        return self.find_arbitrage_opportunity(dai_amount_in)


# Test cases
if __name__ == "__main__":
    # Create two Uniswap pools (To modify x1,y1,x2,y2)
    pool_a = UniswapPool(1000, 500) #X1 DAI, Y1 ETH
    pool_b = UniswapPool(2000, 300) #X2 DAI, Y2 ETH

    # Add liquidity to the pools (To modify)
    pool_a.add_liquidity(1000, 2)
    pool_b.add_liquidity(2000, 4)

    # Test swapping 100 DAI to ETH in Pool A
    dai_amount_in = 100
    eth_amount_out_pool_a = pool_a.calculate_swap(dai_amount_in)
    print(f"Swapping {dai_amount_in} DAI to ETH in Pool A results in {eth_amount_out_pool_a} ETH")

    # Test finding arbitrage opportunity
    arbitrage = ArbitrageOpportunity(pool_a, pool_b)
    dai_amount_in_arbitrage = 100
    arbitrage_profit = arbitrage.find_arbitrage_opportunity(dai_amount_in_arbitrage)
    print(f"Arbitrage profit: {arbitrage_profit:.2f} ETH")

    #Test for benchmarking non-blocking calculation
    dai_benchmarking = 100
    non_blocking_time = timeit.timeit(
        lambda: arbitrage.find_arbitrage_opportunity_non_blocking(dai_benchmarking), 
        number= 100 #adjust reptitions to get accurate result
    )
    print(f"Non-blocking calculation time per iteration: {non_blocking_time / 100:.6f} seconds")
