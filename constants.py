URL = "https://api.overwatchleague.com/stats/players?stage_id=regular_season"
SUBREDDIT = 'competitiveoverwatch'

TABLE = [
    "Average eliminations per 10min",
    "Average deaths per 10min",
    "Average hero damage per 10min",
    "Average healing per 10min",
    "Average ultimates earned per 10min",
    "Average final blows per 10min",
    "Total Time Played (hours)"
]

FOOTER = (
    "\n\nAll stats sourced from [here]({data_link}).\n\n"
    "---\n"
    "^(I am a bot and this action was performed automatically)  \n"
    "[^Send ^my ^creator ^a ^PM]({pm_link}) ^(to provide feedback)\n\n"
    "    usage:\n"
    "        !stats <up to 5 players>\n"
    "        e.g. !stats fissure gesture mano\n"
    "        command needs to be on it's own line"
).format(data_link = URL, pm_link="https://www.reddit.com/message/compose/?to=NobleLordOfLaziness")

TEAMS = {
    'BOS': 'Boston Uprising',
    'GLA': 'Los Angeles Gladiators',
    'HOU': 'Houston Outlaws',
    'SFS': 'San Fransisco Shock',
    'LDN': 'London Spitfire',
    'SHD': 'Shanghai Dragons',
    'NYE': 'New York Excelsior',
    'PHI': 'Philadelphia Fusion',
    'DAL': 'Dallas Fuel',
    'VAL': 'Los Angeles Valiant',
    'FLA': 'Florida Mayhem',
    'SEO': 'Seoul Dynasty'
}
