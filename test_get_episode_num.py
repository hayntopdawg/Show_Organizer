import unittest
from organizer import get_episode_num

__author__ = 'FujNasty'


class TestGet_episode_num(unittest.TestCase):
    def test_lower_case(self):
        test = 'Series Name s01e01.avi'
        result = get_episode_num(test)
        self.assertEqual(result, 1)

    def test_x(self):
        test = 'Series Name 1x01.avi'
        result = get_episode_num(test)
        self.assertEqual(result, 1)

    def test_period(self):
        test = 'Series.1x01.pilot.avi'
        result = get_episode_num(test)
        self.assertEqual(result, 1)

    def test_year(self):
        test = 'Series.2014.S01E01.HDTV.x264-KILLERS.mp4'
        result = get_episode_num(test)
        self.assertEqual(result, 1)

    def test_no_delim(self):
        test = 'Series.101.hdtv-lol.mp4'
        result = get_episode_num(test)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
