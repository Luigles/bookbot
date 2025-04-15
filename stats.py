def num_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_counts = {}
    for char in text:
        # Convert to lowercase
        lowercase_char = char.lower()
        # If character is already in dictionary, increment its count
        if lowercase_char in char_counts:
            char_counts[lowercase_char] += 1
        # Otherwise, add it to dictionary with count of 1
        else:
            char_counts[lowercase_char] = 1
    return char_counts

def sort_char_counts(char_counts):
    # Build list of dictionaries with only alphabetic characters
    sorted_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            sorted_list.append({"char": char, "count": count})
    
    # Sort list by count in descending order
    sorted_list.sort(key=lambda x: x["count"], reverse=True)
    return sorted_list