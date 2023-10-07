import unittest

from ingredient_phrase_tagger.training import tokenizer


class TokenizerTest(unittest.TestCase):
    def test_tokenizer_splits_slash_separated_alternatives(self):
        pairs = [
            (
                "2 tablespoons/30 milliliters milk or cream",
                ["2", "tablespoons", "30", "milliliters", "milk", "or", "cream"],
            ),
            (
                "2 1/2 cups/300 grams all-purpose flour",
                ["2$1/2", "cups", "300", "grams", "all-purpose", "flour"],
            ),
        ]
        for ingredient, tokens_expected in pairs:
            tokens_actual = tokenizer.tokenize(ingredient)
            self.assertEqual(tokens_expected, tokens_actual)

    def test_tokenizer_parens(self):
        expected = ["2", "tablespoons", "milk", "(", "or", "cream", ")"]
        tokens_actual = tokenizer.tokenize("2 tablespoons milk (or cream)")
        self.assertEqual(expected, tokens_actual)

    def test_tokenizer_commas(self):
        expected = [
            "Half",
            "a",
            "vanilla",
            "bean",
            ",",
            "split",
            "lengthwise",
            ",",
            "seeds",
            "scraped",
        ]
        tokens_actual = tokenizer.tokenize(
            "Half a vanilla bean, split lengthwise, seeds scraped"
        )
        self.assertEqual(expected, tokens_actual)

    def test_tokenizer_parens_and_commas(self):
        expected = [
            "1",
            "cup",
            "peeled",
            "and",
            "cooked",
            "fresh",
            "chestnuts",
            "(",
            "about",
            "20",
            ")",
            ",",
            "or",
            "1",
            "cup",
            "canned",
            ",",
            "unsweetened",
            "chestnuts",
        ]
        tokens_actual = tokenizer.tokenize(
            "1 cup peeled and cooked fresh chestnuts (about 20), or 1 cup canned, unsweetened chestnuts"
        )
        self.assertEqual(expected, tokens_actual)

    def test_tokenizer_expands_unit_abbreviations(self):
        pairs = [
            ("100g melted chocolate", ["100", "grams", "melted", "chocolate"]),
            ("100 g melted chocolate", ["100", "grams", "melted", "chocolate"]),
            ("8oz diet coke", ["8", "ounces", "diet", "coke"]),
            ("8 oz diet coke", ["8", "ounces", "diet", "coke"]),
            ("8oz. diet coke", ["8", "ounces", "diet", "coke"]),
            ("8 oz. diet coke", ["8", "ounces", "diet", "coke"]),
            ("15ml coconut oil", ["15", "milliliters", "coconut", "oil"]),
            ("15mL coconut oil", ["15", "milliliters", "coconut", "oil"]),
            ("15 ml coconut oil", ["15", "milliliters", "coconut", "oil"]),
            ("15 mL coconut oil", ["15", "milliliters", "coconut", "oil"]),
        ]
        for ingredient, tokens_expected in pairs:
            tokens_actual = tokenizer.tokenize(ingredient)
            self.assertEqual(tokens_expected, tokens_actual)
