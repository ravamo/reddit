import unittest2
from RedditModel import Reddit
from RedditChallenge import RedditChallenge


class testpostRS(unittest2.TestCase):


    def setUp(self):
        self.calc = Reddit()
        self.server = RedditChallenge()

    def test_postrs(self):
        ob = self.calc("Test",351,3875,0)
        answer = self.server.postrs(ob)
        self.assertEqual(answer, 0.09058064516129032)

    def test_subrs(self):
        ob = self.calc("Test",351,3875,0)
        answer = self.server.subrs(0.0906274206041828,ob)
        self.assertEqual(answer, 0.0002581977794990963)

    if __name__ == '__main__':
        unittest2.main()