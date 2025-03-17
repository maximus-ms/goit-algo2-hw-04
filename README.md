# Algo2. Home work 4
## "Prefix Trees".

### Task 1. Extending the Functionality of a Prefix Tree

Implement two additional methods for the `Trie` class:

- `count_words_with_suffix(pattern)` to count the number of words that end with a given pattern;
- `has_prefix(prefix)` to check for the existence of words with a given prefix.

#### Technical Conditions

 1. The `Homework` class must inherit from the base `Trie` class.
 2. The methods should handle incorrect input data errors.
 3. The input parameters for both methods must be strings.
 4. The `count_words_with_suffix` method should return an integer.
 5. The `has_prefix` method should return a boolean value.

#### Requirements:

 1. The `count_words_with_suffix` method returns the number of words that end with the given pattern. Returns 0 if no such words exist. It is case-sensitive.
 2. The `has_prefix` method returns True if there is at least one word with the given prefix. Returns False if no such words exist. It is case-sensitive.
 3. The code passes all tests.
 4. Incorrect input data is handled.
 5. The methods work efficiently on large datasets.


#### Solution is done in file `task1.py`



### Task 2. Find the longest common prefix

Create a class LongestCommonWord that inherits from the Trie class and implement the find_longest_common_word method, which finds the longest common prefix for all words in the input array of strings strings.

#### Technical Conditions

 1. The `LongestCommonWord` class must inherit from `Trie`.
 2. The input parameter of the `find_longest_common_word` method, `strings` is an array of strings.
 3. The `find_longest_common_word` method must return a string - the longest common prefix.
 4. Execution time - O(S), where S is the total length of all strings.


#### Acceptance Criteria

1. The `find_longest_common_word` method:
    - returns the longest prefix common to all words,
    - returns an empty string if there is no common prefix,
    - correctly handles an empty array or incorrect input data.
2. The code passes all tests.

#### Solution is done in file `task2.py`
