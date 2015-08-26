from unittest import TestCase
from organizer import get_season_num

__author__ = 'FujNasty'


class TestGet_season_num(TestCase):
    def test_lower_case(self):
        test = 'Series s01e01.avi'
        result = get_season_num(test)
        self.assertEqual(result, 1)

    def test_no_s(self):
        test = 'Series 1x01.avi'
        result = get_season_num(test)
        self.assertEqual(result, 1)

    def test_period(self):
        test = 'Series.1x01.pilot.avi'
        result = get_season_num(test)
        self.assertEqual(result, 1)

    def test_year(self):
        test = 'Series.2014.S01E01.HDTV.x264-KILLERS.mp4'
        result = get_season_num(test)
        self.assertEqual(result, 1)

    def test_no_delim(self):
        test = 'Series.101.hdtv-lol.mp4'
        result = get_season_num(test)
        self.assertEqual(result, 1)