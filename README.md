# pfr_metadata_pull

All of your favorite pfr_metadata_pull code, now in package form!  Usage is a simple as:  
  
1. Clone this repo  
2. Make sure your local copy of the repo lives in a directory that's in your PYTHONPATH  
3. Open up python in your manner of choice and type the following:  
```python
import pfr_metadata_pull as meta

meta.scrape_links(start_year, end_year, output_path) # creates a file "game_links_startyear_to_endyear.csv" in the 'output_path' directory
meta.pull_data_from_links("game_links_startyear_to_endyear.csv", output_path) # creates a file "game_meta_data.csv" in the 'output_path' directory
meta.fix_weeks("game_meta_data.csv", output_path)  # creates a file "game_meta_data_weeks_fixed.csv" in the 'output_path' directory
meta.format_data("game_meta_data_weeks_fixed.csv", output_path)  # creates two files in the 'output_path' directory
```
The final format_data function makes two files - one, "game_meta_data_formatted.csv", is a nice pretty version of the metadata.  
The other file, __"game_meta_data_ready_to_merge.csv"__ is what you'll need to add metadata to an existing play-by-play file.  
Say you have a file "pbp.csv" that spans some range of seasons, and you just created "game_meta_data_ready_to_merge.csv" for that same range of seasons.  Now you can do:
```python
import pandas as pd
pbp = pd.read_csv('pbp.csv')
meta = pd.read_csv('game_meta_data_ready_to_merge.csv')
pbp_meta = pd.merge(pbp, meta, on=['season','week','home_team','away_team'], how='outer')
```
Or maybe you do this part in R:
```R
library(tidyverse)
pbp <- read_csv('pbp.csv')
meta <- read_csv('game_meta_data_ready_to_merge.csv')
pbp_meta <- left_join(pbp, meta, by = c("season", "week", "home_team", "away_team"))
```

These changes made by [Dennis Brookner](https://github.com/dennisbrookner); direct concerns to me, or to [Puntalytics](https://twitter.com/ThePuntRunts) on twitter.

### Original README from greerre

This repo contains the set of scripts used to create the dataset referenced here:

https://twitter.com/greerreNFL/status/1146519422527389696

The dataset takes metadata from pro-football-reference and merges it with the game files from the nflscrapR pbp data package.
This matches pfr's game id to the NFL API's game id, allowing for more interesting analysis. For instance, passing EPA by depth of target (nflscrapR data) can be viewed against windspeed or stadium (from p-f-r).

This repo has three scipts with the following purposes:
- pfr_game_link_scraper.py // creates a csv with all p-f-r boxscores dating to 1960
- pfr_meta_data_pull.py    // uses the box score links to pull metadata for each game
- pfr_meta_data_format.py  // formats the metadata to make it 1) more structured and 2) joinable to nflscrapR

These scripts are pretty hacky, but the hope is to turn it into a package that can be update the dataset on an ongoing basis
