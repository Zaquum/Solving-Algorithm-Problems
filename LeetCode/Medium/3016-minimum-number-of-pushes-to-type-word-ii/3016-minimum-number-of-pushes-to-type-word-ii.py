class Solution:
    def minimumPushes(self, word: str) -> int:
        # From GPT
        # Step 1: Count the frequency of each letter in the word
        freq = Counter(word)

        # Step 2: Sort the letters by their frequency in descending order
        sorted_letters = sorted(freq.items(), key=lambda item: -item[1])

        # Step 3: Assign the letters to keys with the least number of presses
        # We have 8 keys (2-9) and can make use of the key presses optimally
        min_presses = 0
        key_presses = 1
        key_index = 2

        # While we have letters to assign
        for letter, count in sorted_letters:
            min_presses += key_presses * count
            key_index += 1
            if key_index > 9:
                key_presses += 1
                key_index = 2

        return min_presses