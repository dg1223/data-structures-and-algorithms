class Solution:
    def fill_freq_array(self, string, array):
        for char in string:
            index = ord(char) - 97
            array[index] += 1
            
    def canConstruct(self, ransom_note: str, magazine: str) -> bool:
        num_alphabets = 26
        freq_ransom = [0] * num_alphabets
        freq_magazine = [0] * num_alphabets

        self.fill_freq_array(ransom_note, freq_ransom)
        self.fill_freq_array(magazine, freq_magazine)

        return all(freq_ransom[idx] <= freq_magazine[idx] for idx in range(num_alphabets))

        # for idx in range(num_alphabets):
        #     if freq_ransom[idx] > 0 and freq_ransom[idx] > freq_magazine[idx]:
        #         return False

        # return True