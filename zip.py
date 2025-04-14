class LZWCompressor:
    def __init__(self):
        self.max_dict_size = 256 
    
    def compress(self, data):

        dictionary = {chr(i): i for i in range(self.max_dict_size)}
        next_code = self.max_dict_size
        compressed = []
        w = ""
        
        for c in data:
            wc = w + c
            if wc in dictionary:
                w = wc
            else:
                compressed.append(dictionary[w])
                dictionary[wc] = next_code
                next_code += 1
                w = c
        
        if w:
            compressed.append(dictionary[w])
        
        
        return compressed
    
    def decompress(self, compressed_data):

        dictionary = {i: chr(i) for i in range(self.max_dict_size)}
        next_code = self.max_dict_size
        decompressed = []
        w = chr(compressed_data.pop(0))
        decompressed.append(w)
        
        for k in compressed_data:
            if k in dictionary:
                entry = dictionary[k]
            elif k == next_code:
                entry = w + w[0]
            else:
                raise ValueError("Некорректный сжатый код: %d" % k)
            
            decompressed.append(entry)
            
            dictionary[next_code] = w + entry[0]
            next_code += 1
            w = entry
        
        return ''.join(decompressed)


if __name__ == "__main__":
    compressor = LZWCompressor()
    
    original_text = "TOBEORNOTTOBEORTOBEORNOT"
    print("Исходный текст:", original_text)
    
    compressed = compressor.compress(original_text)
    print("Сжатые данные:", compressed)

    decompressed = compressor.decompress(compressed.copy())
    print("распакованный текст:", decompressed)
    

    print("совпадение ", original_text == decompressed)
