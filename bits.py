class DecodeError(Exception):
    pass
class ChunkError(Exception):
    pass

class BitList:
    def __init__(self, binarystring):
        try:
            for digit in binarystring:
                if (digit != '0' and digit != '1'):
                    raise ValueError
            self.decimal = int(binarystring, 2)
            print(self.decimal)
            self.binary = binarystring
            print('Object Created!')
        except ValueError:
            print("Format is invalid; does not consist of only 0 and 1")

        
    def __eq__(self, other):
        return self.binary == other.binary

    @staticmethod
    def from_ints(*args):
        combined_ints = ''
        for integer in args:
            combined_ints += str(integer)
        try:
            b = BitList(combined_ints)
            return b
        except ValueError:
            return ("Error")

        
    def __str__(self):
        return self.binary

    def arithmetic_shift_left(self):
        shifted_str = self.binary[1:]
        shifted_str += '0'
        self.binary = shifted_str
        
    
    def arithmetic_shift_right(self):
        shifted_str = self.binary[:-1]
        shifted_str = shifted_str[0] + shifted_str
        self.binary = shifted_str

    def bitwise_and(self, otherBitList):
        if len(self.binary) == len(otherBitList.binary):
            i = 0
            newBinary = ''
            while (i<len(self.binary)):
                    if((self.binary[i] == otherBitList.binary[i]) and self.binary[i] != '0'):
                        newBinary += '1'
                    else:
                        newBinary += '0'
                    i+=1
            return BitList(newBinary)

    def chunk(self, chunk_length):
        try:
            if (len(self.binary) % chunk_length == 0):
                chunks = []
                temp = []
                for i in range(0, len(self.binary)):
                    temp.append(int(self.binary[i]))
                    if (i!= 0 and (i+1) % chunk_length == 0):
                        chunks.append(temp)
                        temp = []
                return chunks
            else:
                raise ChunkError
        except ChunkError:
            return ("Series of bits cannot be split up into evenly sized chunks of bits!")


    def decode(self, encoding='utf-8'):
        bytes = (self.decimal.bit_length() + 7) // 8
        temparray = self.decimal.to_bytes(bytes, "big")
        decoded_value = temparray.decode()
        return decoded_value
    
    



