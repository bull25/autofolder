# 1 Check to see if directory is empty

import os, sys

if len(os.listdir('/Users/bull/Documents/AutoFolder/temp/')) == 0:
    sys.exit()

# 2 Define variable that lists all video file types
# 3 Loop through folder to remove all non video files

else:
	for root, dirs, files in os.walk("."):
	    for name in files:
	        print(name)
	    for name in dirs:
	        print(name)

# 4 Define whether or not the selected file is a movie or a show
# 5 Grab metadata from moviedb (https://api.themoviedb.org) or showdb (https://api.thetvdb.com/)
# 	Sample movie URL (GET /search/movie) - https://api.themoviedb.org/3/search/movie?api_key=561cf52fc5f92f324673609474039c62&language=en-US&query=fight%20club&page=1&include_adult=true
#	Sample show URL (GET /search/tv) - https://api.themoviedb.org/3/search/tv?api_key=561cf52fc5f92f324673609474039c62&language=en-US&query=friends&page=1
#   	- Need to handle exceptions (no match(exit?), multiple matches(take first match))
# 6 Movie - check to see if folder exists in /videos/movies matching the first "genre:name" (movie_api) from the MD
# 7 Movie - if folder exists, move file to folder, then go to step 1(need to accommodate duration of file transfer/copy)
# 8 Movie - if folder does not exist, create folder, then go to step 7 
# 9 Show - check to see if title folder exists in /videos/shows/ matching the "seriesName" (show_series_api)
# 10 Show   - if title folder exists, check to see if season folder exists in /videos/shows/<show title>/ matching "airedSeason" (show_episode_api)
# 11 Show       - if season folder exists, move file to folder, then go to 1
# 12 Show       - if season folder does not exist, make a folder based on "airedSeason" (show_episode_api), then go to 11
# 13 Show   - if title folder does not exist, make a folder in /videos/shows/ based on "seriesName" (show_series_api), then go to 10
# 14 Write results to a log file - filename, action, date, result
