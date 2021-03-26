import nba_scraper.nba_scraper as ns

# if you want to return a dataframe
# you can pass the function a list of strings or integers
# all nba game ids have two leading zeros but you can omit these
# to make it easier to create lists of game ids as I add them on
nba_df = ns.scrape_game([21800001])

# if you want a csv if you don't pass a file path the default is home
# directory
# ns.scrape_game([21800001], data_format='csv', data_dir='file/path')