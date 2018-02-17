# import libraries
import os
 
file = 'paragraph_1.txt'
 
letter_count = 0
 
with open(file, 'r') as txtfile:
    
    paragraph = txtfile.read()
 
    # finding word count
    word_count = paragraph.count(" ") + 1 
 
    # finding sentence count
    sentence_count = paragraph.count(".") + paragraph.count("!") + paragraph.count("?")
 
    # finding average letter count
    for character in paragraph:
        if character.isalpha():
            letter_count += 1 
    avg_letter_count = letter_count/word_count
 
    # finding average sentence length
    avg_sentence = word_count/sentence_count
 
print(letter_count)
 
print("Paragraph Analysis")
print("----------------------------------")
print("Approximate Word Count:", word_count)
print("Approximate Sentence Count:", sentence_count)
print("Average Letter Count:", avg_letter_count)
print("Average Sentence Length:", avg_sentence)