import os
import re

from pytvdbapi import api


__author__ = 'Jamie Fujimoto'


# Globals
# TheTVDB.com Username: hayntopdawg
# TheTVDB.com API key: F35F04BF0C63B299
# TheTVDB.com Account Identifier: 1466EB44A268D300
api_key = 'F35F04BF0C63B299'
DB = api.TVDB(api_key)

VIDEOTYPE = ('avi', 'mkv', 'mp4')


# TODO: Create Episode class
class Episode(object):
    """
    A TV Show episode.  Episodes have the following properties:

    Attributes:
        series:   Name of the TV Show
        season:   Season number
        episode:  Episode number
        name:     Episode name
        filename: Filename for the episode
    """
    # TODO: resolve issue of multiepisode filename

    def __init__(self, series, season, episode):
        self.series = series
        self.season = season
        self.episode = episode

    def get_filename(self):
        # TODO: If series begins with an article, reformat
        pass


# TODO: Open TV Shows folder and print contents
def walker(root):
    """
    Touches every subfolder and file in given directory
    """
    for dir_path, sub_dir_names, filenames in os.walk(root):
        # TODO: Hard-coded; consider revising
        if 'Sample' in sub_dir_names:
            sub_dir_names.remove('Sample')

        for filename in filenames:
            # Only look at video files
            if filename.endswith(VIDEOTYPE):
                print(filename)  # TODO: Use debug
                filename_to_episode(filename)

        # if dir_path != root:
            # print(os.path.basename(dir_path))  # Current folder name
            # current_dir = os.path.basename(dir_path)

            # TODO: If current_dir is Season folder, ensure named correctly

            # TODO: Elif current_dir is Show folder, ensure named correctly

            # TODO: Else move video file from current_dir to correct folder and delete current_dir

        # for subdir in sorted(dirnames):
            # TODO: If show name formated as "Show, The": reformat

            # print("Verifying that {} is a TV Show".format(subdir))

            # TODO: Verify the name of the TV Show with DB
            # show = search_for_show(subdir)
            # print("Series: {}".format(show.SeriesName))

            # TODO: Change/Format name of folder as necessary

            # break
        # break


def filename_to_episode(filename):
    # TODO: Break up filename into parts (show, season, episode)
    s = re.match("(.+)\.S([0-9]+)E([0-9]+)", filename)
    print(s)
    print(s.group(1))
    show = s.group(1).replace(".", " ")
    print(show)
    result = search_for_show(show)
    series = result.SeriesName
    print(s.group(2))
    season = s.group(2)
    print(s.group(3))
    episode = s.group(3)

    return Episode(series, season, episode)


def search_for_show(request, language="en"):
    # TODO: If show not in results list

    results = DB.search(request, language)  # should use a try except for the case that a show is not found

    # TODO: Make this check a pop-up window
    if len(results) > 1:
        for num, result in enumerate(results):
            print(num, result.SeriesName)
        n = input("Enter number for correct show: ")
        return results[int(n)]
    else:
        return results[0]


if __name__ == "__main__":
    # tv_folder = os.path.join("c:", os.sep, "Users", "FujNasty", "Desktop", "Test")  # "C:\Users\FujNasty\Desktop\Test"
    #
    # # tv_folder = os.path.join("p:", os.sep, "TV Shows")
    # # print(tv_folder)
    #
    # walker(tv_folder)

    # filename_to_episode('The.Flash.2014.S01E08.HDTV.x264-LOL.avi')
    pass