"""
You want to build a word cloud, an infographic where the size of a word corresponds to how 
often it appears in the body of text.

To do this, you'll need data. Write code that takes a long string and builds its word cloud data 
in a dictionary, where the keys are words and the values are the number of times the words occurred.

Think about capitalized words. For example, look at these sentences:

'After beating the eggs, Dana read the next step:'
'Add milk and eggs, then add flour and sugar.'

What do we want to do with "After", "Dana", and "add"? In this example, your final dictionary 
should include one "Add" or "add" with a value of 2. Make reasonable (not necessarily perfect) 
decisions about cases like "After" and "Dana".

Assume the input will only contain words and standard punctuation.

You could make a reasonable argument to use regex in your solution. We won't, mainly because performance is difficult to measure and can get pretty bad.
"""

# 1. split words from input string
# 2. populate the dictionary
# 3. handling uppercase and lowercase words


class WordCloudData:
    def __init__(self, input_string):
        self.word_cloud_dict = {}
        self.populate_word_cloud_dict(input_string)

    def populate_word_cloud_dict(self, input_string):

        current_word_start_index = 0
        current_word_length = 0

        for i, char in enumerate(input_string):

            if i == len(input_string) - 1:
                if char.isalpha():
                    current_word_length += 1
                if current_word_length > 0:
                    word = input_string[
                        current_word_start_index : current_word_start_index
                        + current_word_length
                    ]
                    self.add_word(word)

            elif char == " " or char == "\u2014":
                if current_word_length > 0:
                    word = input_string[
                        current_word_start_index : current_word_start_index
                        + current_word_length
                    ]
                    self.add_word(word)
                    current_word_length = 0

            elif char == ".":
                if i < len(input_string) - 1 and input_string[i + 1] == ".":
                    if current_word_length > 0:
                        word = input_string[
                            current_word_start_index : current_word_start_index
                            + current_word_length
                        ]
                    self.add_word(word)
                    current_word_length = 0

            elif char.isalpha() or char == "'":
                if current_word_length == 0:
                    current_word_start_index = i
                current_word_length += 1

            elif char == "-":
                if (
                    i > 0
                    and input_string[i - 1].isalpha()
                    and input_string[i + 1].isalpha()
                ):
                    if current_word_length == 0:
                        current_word_start_index = i
                    current_word_length += 1
                else:
                    if current_word_length > 0:
                        word = input_string[
                            current_word_start_index : current_word_start_index
                            + current_word_length
                        ]
                        self.add_word(word)
                        current_word_length = 0

    def add_word(self, word):

        # If word is already in the dictionary we increment its count
        if word in self.word_cloud_dict:
            self.word_cloud_dict[word] += 1

        # If lower case of the word is in the dictionary, then the input word is uppercase but
        # since we only include uppercase if they are always uppercase, so we'll just increment the
        # lowercase version's count
        elif word.lower() in self.word_cloud_dict:
            self.word_cloud_dict[word.lower()] += 1

        # If the uppercase case of the word is in the dictionary, then the input word is lowercase but
        # since we only increment uppercase if they are always uppercase, we add the lowercase version
        # and give it the uppercase count
        elif word.capitalize() in self.word_cloud_dict:
            self.word_cloud_dict[word] = 1
            self.word_cloud_dict[word] += self.word_cloud_dict[word.capitalize()]
            del self.word_cloud_dict[word.capitalize()]

        # Else the word is not in the dictionary
        else:
            self.word_cloud_dict[word] = 1


input_string = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake. The bill came to five dollars"
wcd = WordCloudData(input_string)
print(wcd.word_cloud_dict)
