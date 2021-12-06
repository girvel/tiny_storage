import unittest

from tiny_storage.internals import pull


class InternalsTests(unittest.TestCase):
    def test_pull(self):
        self.assertEqual(
            3,
            pull(
                {'a': {'something': 3}, 'b': 4, 'c': [1, 2, 3]},
                ['a', 'something'],
                None
            )
        )


if __name__ == '__main__':
    unittest.main()
