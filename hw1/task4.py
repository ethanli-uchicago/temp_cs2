"""
CMSC 14200, Spring 2026
Homework 1, Task 4

People consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

class Card:
    """
    A class for representing cards with features, where each feature's
    name and value are strings. For example, a card could have three
    feature names: color, shape, and number. The values for these features
    could be "red", "circle", and "3", respectively.
    """
    features: dict[str, str]

    def __init__(self, features: dict[str, str]) -> None:
        """
        Constructor. Initializes the card with the provided features.

        Inputs:
            features (dict of str to str): The features of the card,
              with their initial values. For example:
              {"color": "red", "shape": "circle", "number": "3"}
        """
        self.features = features.copy()

    def __str__(self) -> str:
        """
        Returns a string representation of the card.
        """
        s = "[" + ", ".join([f"{k}: {v}" for k, v in self.features.items()]) \
            + "]"
        return s

    def set_feature(self, feature: str, value: str) -> None:
        """
        Set the value of a feature on the card.

        Inputs:
            feature (str): The name of the feature to set.
            value (str): The value to set the feature to.

        Returns: Nothing
        """
        if feature not in self.features:
            raise ValueError(f"Feature '{feature}' not in card")

        self.features[feature] = value

    def get_feature(self, feature: str) -> str:
        """
        Get the value of a feature on the card.

        Inputs:
            feature (str): The name of the feature to get.

        Returns: The value of the feature.
        """
        if feature not in self.features:
            raise ValueError(f"Feature '{feature}' not in card")
        return self.features[feature]

    def compatible(self, other: "Card") -> bool:
        """
        Determine if this card is compatible with another card.

        A card is compatible with another card if the cards have
        no conflicting features and at least one common feature.

        Inputs:
            other (Card): Another card

        Returns: True if the cards are compatible, False otherwise
        """
        return (
            len(self.conflicting_features(other.features)) == 0
            and len(self.common_features(other.features)) > 0
        )

    def common_features(self, other_features: dict[str, str]) -> dict[str, str]:
        """
        Find the common features between this card and some given features.

        A "common feature" is one that has the same name and value in both
        the card and the given features.

        For example, suppose the card has features {"color": "red",
        "shape": "circle", "number": "3"}, and we are given the features
        {"color": "red", "shape": "square", "number": "3"}. The common
        features between the two are {"color": "red", "number": "3"}.

        Inputs:
            other_features (dict of str to str): A dictionary of features to
                compare against.

        Returns (dict of str to str): The common features between the card and
           the given features.
        """
        common = {}
        for feature in self.features:
            if self.features[feature] == other_features.get(feature):
                common[feature] = self.features[feature]
        return common

    def conflicting_features(self, other_features: dict[str, str]) -> dict[str,\
         tuple[str,str]]:
        """
        Find the conflicting features between this card and some given features.

        A "conflicting feature" is one that has the same name but different
        values in the card and the given features.

        For example, if the resulting dictionary maps "number" to ("1", "7"),
        that means this card includes the feature {"number": "1"} but the
        other includes the feature {"number": "7"}.

        Inputs:
            other_features (dict of str to str): A dictionary of features to
                compare against.

        Returns (dict of str to pair of strings): The conflicting features
           between the card and the given features.
        """
        uncommon = {}
        for feature in self.features:
            if feature in other_features:
                if self.features[feature] != other_features[feature]:
                    uncommon[feature] = (self.features[feature], \
                        other_features[feature])
        return uncommon

card1 = Card({"color": "red", "shape": "circle", "number": "3"})
card2 = Card({"color": "red", "shape": "square", "number": "1"})
card3 = Card({"color": "red", "shape": "square", "number": "7"})
card4 = Card({"color": "red", "shape": "square", "hobby": "cooking"})
card5 = Card({"hair": "brown", "eyes": "blue", "expression": "smiling"})
print(card2.common_features(card3.features))
print(card2.conflicting_features(card3.features))
print(card1.conflicting_features(card2.features))