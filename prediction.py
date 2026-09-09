def predict_match(home_team, away_team):
    """
    Basic prediction engine.
    This is the starting point; we'll replace it
    with a trained ML model later.
    """

    return {
        "home_team": home_team,
        "away_team": away_team,
        "prediction": "Home Win",
        "confidence": 50
    }