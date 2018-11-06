import os
import re
import six
import praw
import copy
import requests
import pytablewriter
import constants as CON

STATS = requests.get(CON.URL).json()['data']
COMMAND = re.compile('!stats (.+)', re.IGNORECASE)

def stats(players):
    players = list(map(lambda p: p.lower(), players))
    player_names = []
    teams = {}
    roles = {}
    table = [copy.copy(CON.TABLE)]
    for player in STATS:
        if player['name'].lower() in players:
            player_names.append(player['name'])
            teams[player['name']] = CON.TEAMS.get(player['team'], player['team'])
            roles[player['name']] = player['role']
            table.append([
                player['eliminations_avg_per_10m'],
                player['deaths_avg_per_10m'],
                player['hero_damage_avg_per_10m'],
                player['healing_avg_per_10m'],
                player['ultimates_earned_avg_per_10m'],
                player['final_blows_avg_per_10m'],
                player['time_played_total'] / 60 / 60
            ])
    writer = pytablewriter.MarkdownTableWriter()
    writer.stream = six.StringIO()
    writer.header_list  = ["Statistics"] + player_names
    writer.value_matrix = list(map(list, zip(*table)))
    writer.write_table()
    reply = "# Statistics for " + ', '.join(player_names) + "\n\n"
    reply += ''.join([
        f"{name}: {roles[name]} for {teams[name]}.  \n"
        for name in player_names
    ]) + "\n---\n\n"
    return reply + writer.stream.getvalue() + CON.FOOTER

def login():
    print('logging in ...')
    client = praw.Reddit(
        username      = os.environ.get('REDDIT_USER'),
        password      = os.environ.get('REDDIT_PASS'),
        client_id     = os.environ.get('CLIENT_ID'),
        client_secret = os.environ.get('CLIENT_SECRET'),
        user_agent    = 'OWL-StatsBot responder'
    )
    return client

def run(client):
    print('running ...')
    for comment in client.subreddit(CON.SUBREDDIT).stream.comments():
        if comment.saved or comment.author == client.user.me():
            continue

        bot_call = COMMAND.search(comment.body)
        if bot_call is None:
            continue

        print('found comment: https://reddit.com' + comment.permalink)
        print('command:', bot_call.group(0))
        terms = bot_call.group(1).strip().split(' ')
        reply = stats(terms[:5])

        if reply is not None:
            comment.reply(reply)
            comment.save()
            print('replied')
        else:
            print('failed')


if __name__ == "__main__":
    client = login()
    run(client)
