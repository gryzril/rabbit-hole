import WordCount
import user_input

neededInput = 'Please Enter URL:\n'

text = user_input.get_user_input(neededInput)

words = WordCount.list_popular_words(text)
print(words)