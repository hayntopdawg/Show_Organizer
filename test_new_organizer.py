import unittest
from new_organizer import filename_to_episode
#import new_organizer

__author__ = 'Jamie Fujimoto'

class TestNewOrganizer(unittest.TestCase):
    """ Tests for "new_organizer.py". """

    def test_flash(self):
        filename = "The.Flash.2014.S01E08.HDTV.x264-LOL.avi"
        epi = filename_to_episode(filename)
        self.assertEqual(epi.series, "The Flash (2014)")
        self.assertEqual(epi.season, 1)
        self.assertEqual(epi.episode, 8)
        self.assertEqual(epi.name, "Flash vs. Arrow (1)")

    def test_TBBT(self):
        filename = "The Big Bang Theory S01E13 - The Bat Jar Conjecture.avi"
        epi = filename_to_episode(filename)
        self.assertEqual(epi.series, "The Big Bang Theory")
        self.assertEqual(epi.season, 1)
        self.assertEqual(epi.episode, 13)
        self.assertEqual(epi.name, "The Bat Jar Conjecture")

    def test_begins_with_article_flash(self):
        filename = "The.Flash.2014.S01E08.HDTV.x264-LOL.avi"
        epi = filename_to_episode(filename)
        self.assertEqual(epi.get_series_directory(), "Flash, The (2014)")

    def test_begins_with_article_TBBT(self):
        filename = "The Big Bang Theory S01E13 - The Bat Jar Conjecture.avi"
        epi = filename_to_episode(filename)
        self.assertEqual(epi.get_series_directory(), "Big Bang Theory, The")

    def test_get_season_flash(self):
        filename = "The.Flash.2014.S01E08.HDTV.x264-LOL.avi"
        epi = filename_to_episode(filename)
        self.assertEqual(epi.get_season_directory(), "Season 01")

    def test_get_season_TBBT(self):
        filename = "The Big Bang Theory S01E13 - The Bat Jar Conjecture.avi"
        epi = filename_to_episode(filename)
        self.assertEqual(epi.get_season_directory(), "Season 01")

    def test_get_filename_flash(self):
        filename = "The.Flash.2014.S01E08.HDTV.x264-LOL.mp4"
        epi = filename_to_episode(filename)
        self.assertEqual(epi.get_filename(), "The Flash (2014) S01E08 - Flash vs. Arrow (1).mp4")

    def test_get_filename_TBBT(self):
        filename = "The Big Bang Theory S01E13 - The Bat Jar Conjecture.avi"
        epi = filename_to_episode(filename)
        self.assertEqual(epi.get_filename(), "The Big Bang Theory S01E13 - The Bat Jar Conjecture.avi")


if __name__ == "__main__":
    unittest.main()