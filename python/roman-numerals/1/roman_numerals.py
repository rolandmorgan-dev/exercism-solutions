table=((1000, 'M'),(900, 'CM'),(500, 'D'),(400, 'CD'),(100, 'C'),(90, 'XC'),
       (50, 'L'),(40, 'XL'),(10, 'X'),(9, 'IX'),(5, 'V'),(4, 'IV'),(1, 'I'))

# Convert to Roman numeral
def roman(number : int) -> str:
  result = ''
  for num, roman_char in table:
      times, number = divmod(number, num)
      result += roman_char * times
  return result
