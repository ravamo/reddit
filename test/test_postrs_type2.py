import unittest2
from unittest.mock import patch


class testpostRS(unittest2.TestCase):

    @patch('main.RedditChallenge.postrs', return_value=9)
    def test_postRS(self, postrs):
        ob = self.calc("Test",351,3875,0)
        self.assertEqual(postrs(ob), 0.09058064516129032)

    @patch('main.RedditChallenge.subrs', return_value=9)
    def test_subrs(self, subrs):
        ob = self.calc("Test",351,3875,0)
        self.assertEqual(subrs(0.0906274206041828,ob), 0.0002581977794990963)

    if __name__ == '__main__':
        unittest2.main()