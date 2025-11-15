ocr_numbers = {" _ | ||_|   " : "0",
               "     |  |   " : "1",
               " _  _||_    " : "2",
               " _  _| _|   " : "3",
               "   |_|  |   " : "4",
               " _ |_  _|   " : "5",
               " _ |_ |_|   " : "6",
               " _   |  |   " : "7",
               " _ |_||_|   " : "8",
               " _ |_| _|   " : "9",}

def convert(ocr):
    if len(ocr) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    
    if not all(len(ocr[i]) % 3 == 0 for i in range(len(ocr))):
        raise ValueError("Number of input columns is not a multiple of three")

    result = ""
    if len(ocr) == 4:
        for row in range(0, len(ocr[0]), 3):
            single_num = ""
            for index in range(len(ocr)):
                single_num += ocr[index][row:row+3]
            result += ocr_numbers.get(single_num, "?")
            
    if len(ocr) > 4:
         for i in range(0, len(ocr), 4):
             result += convert(ocr[i:i+4])
             if i+4 != len(ocr):
                 result += ","

    return result