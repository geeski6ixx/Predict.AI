import math


def poisson_probability(lmbda, goals):
    """Calculate the probability of scoring a specific number of goals."""
    if lmbda < 0:
        raise ValueError("Expected goals cannot be negative.")

    return (math.exp(-lmbda) * (lmbda ** goals)) / math.factorial(goals)


def match_probabilities(home_xg, away_xg):
    """
    Calculate Home Win, Draw and Away Win probabilities
    using expected goals (xG).
    """

    if home_xg < 0 or away_xg < 0:
        raise ValueError("Expected goals cannot be negative.")

    home_win = 0.0
    draw = 0.0
    away_win = 0.0

    for home_goals in range(8):
        for away_goals in range(8):

            probability = (
                poisson_probability(home_xg, home_goals)
                * poisson_probability(away_xg, away_goals)
            )

            if home_goals > away_goals:
                home_win += probability
            elif home_goals == away_goals:
                draw += probability
            else:
                away_win += probability

    total = home_win + draw + away_win

    return {
        "home_win": round(home_win / total, 4),
        "draw": round(draw / total, 4),
        "away_win": round(away_win / total, 4)
    }