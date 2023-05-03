#!/usr/bin/python3
"""
Gets the latest 10 github commits by a user rail
in the rail repository, sorted from most recent to
oldest
"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    repo = sys.argv[2]
    # param_data = {'per_page': '10'}
    res = requests.get("https://api.github.com/repos/{}/{}/commits".
                       format(user, repo))
    commits = res.json()
    sub_list = []
    sub_dict = {}
    sorted_list = sorted(commits, key=lambda x: x['commit'].
                         get('author').get('date'), reverse=True)
    """
    for commit in commits:
        sub_dict = {}
        sub_dict['sha'] = commit.get('sha')
        sub_dict['name'] = commit.get('commit').get('author').get('name')
        sub_dict['date'] = commit.get('commit').get('author').get('date')
        sub_list.append(sub_dict)
    # Sort based on date, latest to oldest
    # sorted_list = sorted(sub_list, key=lambda x: x['date'], reverse=True)
    """
    for item in sorted_list[0:10]:
        print("{}: {}".format(item.get('sha'), item.get('commit').
                              get('author').get('name')))
