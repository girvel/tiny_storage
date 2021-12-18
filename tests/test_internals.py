import unittest

from tiny_storage.internals import pull, push, put


class InternalsCase(unittest.TestCase):
    def test_pull(self):
        self.assertEqual(
            (False, None),
            pull(
                {"a": {"something": None}, "b": 4, "c": [1, 2, 3]},
                ["a", "something"],
                123,
            ),
        )

    def test_push(self):
        data = {"a": {}}
        result = push(data, ["a", "b", "c"], 4)

        self.assertEqual((True, 4), result)
        self.assertEqual({"a": {"b": {"c": 4}}}, data)

    def test_push_force(self):
        data = {"a": {"b": {"c": 3}}}
        result = push(data, ["a", "b", "c"], 4)

        self.assertEqual((True, 4), result)
        self.assertEqual({"a": {"b": {"c": 4}}}, data)

    def test_put(self):
        data = {"a": {}}
        result = put(data, ["a", "b", "c"], 4)

        self.assertEqual((True, 4), result)
        self.assertEqual({"a": {"b": {"c": 4}}}, data)

    def test_put_force(self):
        data = {"a": {"b": {"c": 3}}}
        result = put(data, ["a", "b", "c"], 4)

        self.assertEqual((False, 3), result)
        self.assertEqual({"a": {"b": {"c": 3}}}, data)


if __name__ == "__main__":
    unittest.main()
