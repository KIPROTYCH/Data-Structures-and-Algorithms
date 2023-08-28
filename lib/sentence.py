import string

def word_frequency(sentence):
    words = sentence.lower().split()  # Convert sentence to lowercase and split into words
    words = [word.strip(string.punctuation) for word in words]  # Remove punctuation from words
    frequency = {}  # Create an empty dictionary to store word frequency
    
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1  # Increment word frequency in dictionary
        
    return frequency

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
