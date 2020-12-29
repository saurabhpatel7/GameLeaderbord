def write_score(score, name, scores, filename, splitter=','):
    """writes a score with a name to a file, in a specified format"""
    score_tuple = (score,name)
    scores.append(score_tuple)
    with open(filename,'w') as f:
        for s in scores:
            f.write(str(s[0]) + splitter + s[1] + '\n')
        f.close()

def read_scores(filename, splitter=','):
    """reads scores and names from a file, and returns a list of each"""
    with open(filename) as f:
        raw_scores = f.read().strip().split('\n')
        f.close()

    scores = []
    names = []

    for score in raw_scores:
        score_split = score.split(splitter)
        scores.append(int(score_split[0]))
        names.append(score_split[1])
    return scores, names

def sort_scores(scores, names,reverse_bool=True):
    """sorts the scores from greatest to least and returns in a list of tuples format"""
    zipped = sorted(list(zip(scores,names)), reverse=reverse_bool)
    return zipped

def print_scores(score_list, seperator=' ', top_amount=5):
    """prints the number of leaderboard scores stated"""
    for score_tuple in score_list[:top_amount]:
        print(str(score_tuple[0]) + seperator + score_tuple[1])

def has_better_score(score, scores, leaderboard_len=5):
    """returns if the score should be written to a file"""
    if (len(scores) > leaderboard_len and score >= scores[leaderboard_len - 1][0]) or len(scores) <= leaderboard_len:
        return True
    return False