# get_score takes a dictionary of student scores and a student's name.
# It returns the score for that student.
#
# Examples:
#   get_score({"Alice": 90, "Bob": 85}, "Alice") -> 90
#
# Requirements:
#   - Assume the key exists in the dictionary
#   - Do NOT print anything
#
def get_score(scores: dict, name: str) -> int:
    pass


# add_score takes a dictionary of scores, a name, and a score.
# It adds the name and score to the dictionary and returns the updated dictionary.
#
# Examples:
#   add_score({"Alice": 90}, "Bob", 85) -> {"Alice": 90, "Bob": 85}
#
# Requirements:
#   - Modify the dictionary
#   - Return the dictionary
#
def add_score(scores: dict, name: str, score: int) -> dict:
    pass


# update_score takes a dictionary of scores, a name, and a new score.
# It updates the student's score and returns the dictionary.
#
# Examples:
#   update_score({"Alice": 90}, "Alice", 95) -> {"Alice": 95}
#
# Requirements:
#   - Assume the key exists
#   - Return the updated dictionary
#
def update_score(scores: dict, name: str, new_score: int) -> dict:
    pass


# count_items takes a dictionary and returns the number of key-value pairs.
#
# Examples:
#   count_items({"a": 1, "b": 2}) -> 2
#   count_items({}) -> 0
#
# Requirements:
#   - Do NOT use len()
#   - Use a loop
#
def count_items(d: dict) -> int:
    pass


# get_keys returns a list of all keys in the dictionary
#
# Example:
#   get_keys({"a": 1, "b": 2}) -> ["a", "b"]
#
def get_keys(d: dict) -> list:
    pass


# get_values returns a list of all values in the dictionary
#
# Example:
#   get_values({"a": 1, "b": 2}) -> [1, 2]
#
def get_values(d: dict) -> list:
    pass