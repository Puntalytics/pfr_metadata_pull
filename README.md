# pfr_metadata_pull

All of your favorite pfr_metadata_pull code, now in package form!  Usage is a simple as:  
  
1. Clone this repo  
2. Make sure your local copy of the repo lives in a directory that's in your PYTHONPATH  
3. Open up python in your manner of choice and type the following:  
```python
import pfr_metadata_pull as meta

meta.scrape_links(start_year, end_year, output_path)  # creates input_file1
meta.pull_data_from_links(input_file1, output_path)  # creates input_file2
meta.fix_weeks(input_file2, output_path)  # creates input_file3
meta.format_data(input_file3, output_path)  # creates your final file of interest, with metadata for games in the desired range
```
The scrape_links, pull_data_from_links, and format_data methods correlate with the functions of the scripts referenced below, while fix_weeks is a stopgap bug fix that I couldn't quite figure out.

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
