# OWL-StatsBot

[OWL-StatsBot user profile](https://reddit.com/user/OWL-StatsBot)

This is a basic reddit bot that provides users with player statistics from the Overwatch League. Operates in [r/competitiveoverwatch](https://reddit.com/r/competitiveoverwatch).

`!stats <up to 5 players>` will provide stats for the players in a table format (e.g. `!stats Gesture` or `!stats akm libero`).  

All statistics sourced from [here](https://api.overwatchleague.com/stats/players?stage_id=regular_season).

## Requirements

- praw
- six
- pytablewriter
