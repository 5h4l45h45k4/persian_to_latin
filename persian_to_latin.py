def persian_to_latin(text):
  """
  Converts a given Farsi text to its closest sounding Latin characters.

  Args:
      text: The Farsi text to be converted.

  Returns:
      The converted Latin text.
  """
  persian_to_latin_dict = {
    'ا': 'a',
    'ب': 'b',
    'پ': 'p',
    'ت': 't',
    'ث': 's',
    'ج': 'dj',
    'چ': 'tsh',
    'ح': 'h',
    'خ': 'kh',
    'د': 'd',
    'ذ': 'z',
    'ر': 'r',
    'ز': 'z',
    'ژ': 'j',
    'س': 's',
    'ش': 'sh',
    'ص': 's',
    'ض': 'z',
    'ط': 't',
    'ظ': 'z',
    'ع': ''',
    'غ': 'gh',
    'ف': 'f',
    'ق': 'q',
    'ک': 'k',
    'گ': 'g',
    'ل': 'l',
    'م': 'm',
    'ن': 'n',
    'و': 'v',
    'ه': 'h',
    'ی': 'y'
  }

  latin_text = ""
  for char in text:
    if char in persian_to_latin_dict:
      latin_text += persian_to_latin_dict[char]
    else:
      # Handle characters not in the mapping (e.g., punctuation)
      latin_text += char

  return latin_text

def main():
  """
  Prompts the user for Farsi text, converts it to Latin characters, and prints the result.
  """
  farsi_text = input("Enter Farsi text: ")
  latin_text = persian_to_latin(farsi_text)
  print("Latin transliteration:", latin_text)

if __name__ == '__main__':
  main()
