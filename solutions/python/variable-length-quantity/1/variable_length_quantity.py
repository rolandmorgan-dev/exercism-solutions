def encode(numbers):
    bits = []
    for num in numbers:
        tmp = []
        if num == 0: tmp.append(0)
        
        while num:
            bits_7 = num & 127
            tmp.append(bits_7)
            num >>= 7
        
        bits.extend([b if i == 0 else b + 128 for i,b in enumerate(tmp)][::-1])
    
    return bits

def decode(chunks):
    if not chunks or chunks[-1].bit_length() > 7:
        raise ValueError("incomplete sequence")
    
    result = []
    bin_to_num = 0 
    for bits in chunks:
        bin_to_num <<= 7
        bin_to_num += bits & 127
        
        if bits.bit_length() < 8:
            result.append(bin_to_num)
            bin_to_num = 0
        
    return result