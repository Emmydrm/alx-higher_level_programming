#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    bestScore = None

    for key in a_dictionary:
        if bestScore is None:
            bestScore = key
        else:
            if a_dictionary[key] > a_dictionary[bestScore]:
                bestScore = key
    return bestScore
