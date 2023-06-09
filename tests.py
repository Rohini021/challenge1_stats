import unittest
from stats import add_entry_to_stats, merge_stats


class TestTask1(unittest.TestCase):

    maxDiff = None

    def test_add_entry_to_stats(self):
        stats = {
            "count": 15,
            "amount": 425,
            "num_items": 12,
            "gender": {
                "F": {"count": 5, "amount": 225, "num_items": 7},
                "M": {"count": 10, "amount": 200, "num_items": 5},
            },
            "currency": {
                "EUR": {"count": 13, "amount": 175, "num_items": 6},
                "USD": {"count": 2, "amount": 250, "num_items": 6},
            },
        }

        entry = {
            "gender": "M",
            "amount": 17,
            "num_items": 2,
            "currency": "EUR",
            "week_of_year": 42,
            "country_code": "GB",
        }

        expected_stats = {
            "count": 16,
            "amount": 442,
            "num_items": 14,
            "gender": {
                "F": {"count": 5, "amount": 225, "num_items": 7},
                "M": {"count": 11, "amount": 217, "num_items": 7},
            },
            "currency": {
                "EUR": {"count": 14, "amount": 192, "num_items": 8},
                "USD": {"count": 2, "amount": 250, "num_items": 6},
            },
            "week_of_year": {42: {"count": 1, "amount": 17, "num_items": 2}},
            "country_code": {"GB": {"count": 1, "amount": 17, "num_items": 2}},
        }

        updated_stats = add_entry_to_stats(stats, entry)
        self.assertDictEqual(updated_stats, expected_stats)

    # test case: empty stats dict
    def test_add_entry_to_stats_empty_stats(self):
        entry = {
            "gender": "M",
            "amount": 17,
            "num_items": 2,
            "currency": "EUR",
            "week_of_year": 42,
            "country_code": "GB",
        }

        expected_stats = {
            "count": 1,
            "amount": 17,
            "num_items": 2,
            "gender": {
                "M": {"count": 1, "amount": 17, "num_items": 2},
            },
            "currency": {
                "EUR": {"count": 1, "amount": 17, "num_items": 2},
            },
            "week_of_year": {42: {"count": 1, "amount": 17, "num_items": 2}},
            "country_code": {"GB": {"count": 1, "amount": 17, "num_items": 2}},
        }

        updated_stats = add_entry_to_stats({}, entry)
        self.assertDictEqual(updated_stats, expected_stats)


class TestTask2(unittest.TestCase):

    maxDiff = None

    def test_merge_stats(self):
        stats1 = {
            "count": 15,
            "amount": 425,
            "num_items": 12,
            "gender": {
                "F": {"count": 5, "amount": 225, "num_items": 7},
                "M": {"count": 10, "amount": 200, "num_items": 5},
            },
            "currency": {
                "EUR": {"count": 13, "amount": 175, "num_items": 6},
                "USD": {"count": 2, "amount": 250, "num_items": 6},
            },
        }

        stats2 = {
            "count": 15,
            "amount": 425,
            "num_items": 12,
            "gender": {
                "F": {"count": 5, "amount": 225, "num_items": 7},
                "M": {"count": 10, "amount": 200, "num_items": 5},
            },
            "currency": {
                "EUR": {"count": 13, "amount": 175, "num_items": 6},
                "USD": {"count": 2, "amount": 250, "num_items": 6},
            },
            "something_deep": {"deeper": {"the_deepest": {"hidden_treasure": 41}}},
            "empty_object": {},
        }

        stats3 = {
            "count": 15,
            "amount": 450,
            "num_items": 12,
            "something_else": 30,
            "gender": {
                "F": {"count": 5, "amount": 225, "num_items": 7},
                "M": {"count": 10, "amount": 200, "num_items": 5},
            },
            "currency": {
                "EUR": {"count": 13, "amount": 175, "num_items": 6},
                "USD": {"count": 2, "amount": 250, "num_items": 6},
            },
            "country_code": {"GB": {"count": 2, "amount": 10, "num_items": 2}},
            "something_deep": {"deeper": {"the_deepest": {"hidden_treasure": 1}}},
            "empty_object": {},
        }

        expected_stats = {
            "count": 45,
            "amount": 1300,
            "num_items": 36,
            "something_else": 30,
            "gender": {
                "F": {"count": 15, "amount": 675, "num_items": 21},
                "M": {"count": 30, "amount": 600, "num_items": 15},
            },
            "currency": {
                "EUR": {"count": 39, "amount": 525, "num_items": 18},
                "USD": {"count": 6, "amount": 750, "num_items": 18},
            },
            "country_code": {"GB": {"count": 2, "amount": 10, "num_items": 2}},
            "something_deep": {"deeper": {"the_deepest": {"hidden_treasure": 42}}},
            "empty_object": {},
        }

        merged_stats = merge_stats(stats1, stats2, stats3)

        self.assertDictEqual(merged_stats, expected_stats)


if __name__ == "__main__":
    unittest.main()
