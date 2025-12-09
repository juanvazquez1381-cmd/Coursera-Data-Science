string = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"

def get_word_frequency_dict(text, phase):
    # 1. Normalize and clean the text: 
    #    - Convert to lowercase (to count 'Mary' and 'mary' together).
    #    - Replace punctuation with a space (to separate 'lamb.Its' into 'lamb' and 'its').
    import re
    cleaned_text = re.sub(r'[^\w\s]', ' ', text.lower())
    
    # 2. Split the cleaned text into a list of words
    words = cleaned_text.split()
    
    # 3. Create the frequency dictionary
    word_freq = {}
    for word in words:
        if word: # Ensure no empty strings from multiple spaces
            # Use the .get() method to increment the count or start it at 1
            word_freq[word] = word_freq.get(word, 0) + 1
            
    return word_freq

# Execute the function
word_dictionary = get_word_frequency_dict(string)
print(word_dictionary)

# Python Program to Count words in a String using Dictionary
def freq(string,passedkey):

    #step1: A list variable is declared and initialized to an empty list.
    words = []

    #step2: Break the string into list of words
    words = string.split() # or string.lower().split()

    #step3: Declare a dictionary
    Dict = {}

    #step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        if(key == passedkey):
            Dict[key] = words.count(key)   
    #step5: Print the dictionary
    print("Total Count:",Dict)
