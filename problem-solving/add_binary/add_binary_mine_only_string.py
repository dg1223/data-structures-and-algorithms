class Solution:        
    def add_zero_to_beginning(self, string, difference):
        concat_str = '0' * difference
        string = concat_str + string

        return string

    def concat_binary(self, string_1, string_2, result):
        carry = False
        if string_1  != string_2:
            result.insert(0, '1')
        else:
            result.insert(0, '0')
            # We have a carry only when both bits are 1
            if string_1 == '1':
                carry = True

        return result, carry

    def addBinary(self, binary_string_1: str, binary_string_2: str):
        length_1 = len(binary_string_1)
        length_2 = len(binary_string_2)

        if length_2 < length_1:
            difference =  abs(length_1 - length_2)
            binary_string_2 = self.add_zero_to_beginning(binary_string_2, difference)
        elif length_1 < length_2:
            difference =  abs(length_1 - length_2)
            binary_string_1 = self.add_zero_to_beginning(binary_string_1, difference)

        result = []    
        carry = False

        # reverse for loop
        for idx, item in reversed(list(enumerate(binary_string_1))):
            if carry:            
                result, carry = self.concat_binary(item, binary_string_2[idx], result)
                '''
                We are always inserting the resultant bit into the beginning of the 
                'result' string. Therefore, we only care about the 0-th character 
                of 'result' when we have a carry.
                '''
                if result[0] == '0':
                    result[0] = '1'
                else:
                    result[0] = '0'
                    carry = True
            else:
                result, carry = self.concat_binary(item, binary_string_2[idx], result)

        if carry:
            result.insert(0, '1')

        return ''.join(result)
