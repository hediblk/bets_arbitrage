def is_arbitrage(odds_a, odds_b):
    """
    Returns True if there is an arbitrage opportunity between two decimal odds.
    """
    return (1/odds_a + 1/odds_b) < 1


def arbitrage_stakes(odds_a, odds_b, total_bankroll):
    """
    Returns (stake_a, stake_b) if arbitrage exists, otherwise None.
    """
    if not is_arbitrage(odds_a, odds_b):
        return None
    stake_a = total_bankroll * (1/odds_a) / ((1/odds_a) + (1/odds_b))
    stake_b = total_bankroll * (1/odds_b) / ((1/odds_a) + (1/odds_b))
    return stake_a, stake_b