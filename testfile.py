import unittest
from YouTubeProject import getResponse


class TestFileName(unittest.TestCase):
    def test_function1(self):
        dic = {'viewCount': '0', 'subscriberCount': '0', 'hiddenSubscriberCount': False, 'videoCount': '0'}
        self.assertEqual(getResponse(), dic)

if __name__ == '__main__':
    unittest.main()
