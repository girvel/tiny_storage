import unittest

from tiny_storage.internals import pull, push


class InternalsCase(unittest.TestCase):
    def test_pull(self):
        self.assertEqual(
            (False, None),
            pull(
                {'a': {'something': None}, 'b': 4, 'c': [1, 2, 3]},
                ['a', 'something'],
                123
            )
        )

    def test_push(self):
        data = {'a': {}}
        result = push(data, ['a', 'b', 'c'], 4)

        self.assertEqual((True, 4), result)
        self.assertEqual({'a': {'b': {'c': 4}}}, data)


if __name__ == '__main__':
    unittest.main()
