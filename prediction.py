def predict_match(home_team, away_team):
    """
    Basic PredictAI prediction engine.
    """

    # Temporary rule-based engine
    # We'll connect real football data + ML later.

    return {
        "home_team": home_team,
        "away_team": away_team,
        "prediction": "Home Win",
        "confidence": 50,
        "status": "success"
    }