__author__ = 'FujNasty'

import os
import re

from pytvdbapi import api


# User inputs name of Movie or TV Show
# Currently only works for TV Shows
def get_input():
    name = input("Show: ")
    # Checks whether Movie or TV Show exists
    show = search_for_series(name)
    season = input("Season: ")
    return show, int(season)


# Parse folder to rename files not named in the correct format
def navigate(path, show, season):
    for count, elem in enumerate(os.listdir(path)):
        # if element is a folder, navigate to folder
        if os.path.isdir(os.path.join(path, elem)):
            new_path = os.path.join(path, elem)
            print('Directory: {}'.format(new_path))
            navigate(new_path, show, season)
            # once returned, delete folder
            for f in os.listdir(new_path):
                os.remove(os.path.join(new_path, f))
            os.rmdir(new_path)
        # if element is a video file, rename to correct format
        elif elem.split('.')[-1] in VIDEOTYPE:
            print('Video: {}'.format(elem))
            new_name = reformat(elem, show, season)
            print('New name: {}'.format(new_name))
            # if video file is not in BASEPATH, move video file to BASEPATH
            os.rename(os.path.join(path, elem), os.path.join(BASEPATH, new_name))


# Naming convention: Series S##E## - EpisodeName
def reformat(filename, show, season):
    series = title_except(show.SeriesName, ARTICLES)
    sea_num = get_season_num(filename)
    if sea_num != season:
        print("Incorrect season")  # Should return an error
        print("sea_num: {} season: {}".format(sea_num, season))
        return
    else:
        epi_num = get_episode_num(filename)
        print(epi_num)
        epi_name = get_episode_name(show, season, epi_num)
        ftype = filename.split('.')[-1]

        return '{0} S{1:02d}E{2:02d} - {3}.{4}'.format(series, season, epi_num, epi_name, ftype)


def get_season_num(filename):
    s = re.search(
        r'''(?ix)               # (i) case-insensitive, (x) verbose regex
            (?:                 # non-grouping pattern
              s|season|\s*|\.   # s or season or whitespace or period
              )                 # end non-grouping pattern
            # \s*                 # 0-or-more whitespaces
            (\d+)               # 1-or-more digits
            (?=                 # if followed by
               e|x|\d{2}\.[a-z]{2,}        # e or x or exactly 2 digits
               )
            ''', filename)
    if s:
        return int(s.group(1))


def get_episode_num(filename):
    e = re.search(
                  r'''(?ix)             # (i) case-insensitive, (x) verbose regex
                  (?:                   # non-grouping pattern
                     e|x|\d{1})         # e or x or episode
                  (\d{2})               # exactly 2 digits
                  (?=\.[a-z]{2,})
                  ''', filename)
    if e:
        return int(e.group(1))


def search_for_series(request):
    results = DB.search(request, 'en')  # should use a try except for the case that a show is not found
    if len(results) > 1:
        for num, result in enumerate(results):
            print(num, result.SeriesName)
        n = input("Enter number for correct show: ")
        return results[int(n)]
    else:
        return results[0]


def get_episode_name(show, season, episode):
    return show[season][episode].EpisodeName


def format_episode_name(name):
    return name.translate({ord(i): None for i in ILLEGAL})


def title_except(s, exceptions):
    words = s.split()
    final = [words[0].capitalize()]
    for word in words[1:]:
        final.append(word if word in exceptions else word.capitalize())
    return ' '.join(final)


# Declare global variables
ARTICLES = ['a', 'an', 'of', 'the', 'is']
VIDEOTYPE = ['avi', 'mkv', 'mp4']
ILLEGAL = '<>:"/\|?*'
FILEPATH = r"P:\TV Shows"

# TheTVDB.com Username: hayntopdawg
# TheTVDB.com API key: F35F04BF0C63B299
# TheTVDB.com Account Identifier: 1466EB44A268D300
api_key = 'F35F04BF0C63B299'
DB = api.TVDB(api_key)

if __name__ == '__main__':
    global BASEPATH
    show, season = get_input()
    title = title_except(show.SeriesName, ARTICLES)
    BASEPATH = os.path.join(FILEPATH, title, "Season {:02d}".format(int(season)))
    # print(path)
    navigate(BASEPATH, show, season)

    ### How it should work ###
    # User inputs title of tv show to have the folder organized
    # Checks to ensure tv show exists in "TV Show" folder
    # Searches for show on TVDB.com sets SeriesName to global variable
    # For each Season folder in Series's folder, organize and rename files
    # Basepath of those files becomes the Season folder