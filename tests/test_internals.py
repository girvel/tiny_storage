import unittest

from tiny_storage.internals import pull, push


class InternalsCase(unittest.TestCase):
    def test_pull(self):
        self.assertEqual(
            (False, 3),
            pull(
                {'a': {'something': 3}, 'b': 4, 'c': [1, 2, 3]},
                ['a', 'something'],
                None
            )
        )

    def test_push(self):
        data = {'a': {}}
        result = push(data, ['a', 'b', 'c'], 4)

        self.assertEqual((True, 4), result)
        self.assertEqual({'a': {'b': {'c': 4}}}, data)


if __name__ == '__main__':
    unittest.main()
