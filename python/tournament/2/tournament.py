def tally(rows):
    # (0,0,0,0,0) -> | MP | W | D | L | P | -> (Played, Won, Drawn, Lost, Points)
    team_scores = {team: (0,0,0,0,0) for line in rows for team in line.split(";")[:2]}
    
    add_stats = lambda a, b: tuple(x + y for x, y in zip(a, b))
    for row in rows:
        data = row.split(";")
        # data -> [Team 1, Team 2, Match result]
        if data[2] == "win":
            score_update = ((1,1,0,0,3),(1,0,0,1,0))
        elif data[2] == "loss":
            score_update = ((1,0,0,1,0),(1,1,0,0,3))
        else:
            score_update = ((1,0,1,0,1),(1,0,1,0,1))
        
        team_scores[data[0]] = add_stats(team_scores[data[0]], score_update[0])
        team_scores[data[1]] = add_stats(team_scores[data[1]], score_update[1])
    
    team_scores = sorted(team_scores.items(), key=lambda i: (-i[1][4], i[0]))
    
    table = ["Team                           | MP |  W |  D |  L |  P"]
    table_data = "{:<30.30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"
    for team, scores in team_scores:
        table.append(table_data.format(team, *scores))
    return table