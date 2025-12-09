string = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"

def improved_word_count(string, phase):
    # 1. Normalize the input string by converting to lowercase and removing punctuation
    import re
    cleaned_string = re.sub(r'[^\w\s]', '', string.lower()) 
    words = cleaned_string.split()
    
    # 2. Normalize the search phrase
    normalized_phase = phase.lower()
    
    # 3. Count matches
    frequent = [word for word in words if word == normalized_phase]
    count = len(frequent)
    return frequent, count

print(improved_word_count(string, "little"))
# Output would be: (['little', 'little', 'little', 'little'], 4)
# (It now counts "Little" as "little")
