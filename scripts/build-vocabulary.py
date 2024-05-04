def build_vocabulary(tokenized_captions):
    """
    Build a vocabulary of unique words from tokenized captions.

    Args:
        tokenized_captions (list): List of tokenized sequences.

    Returns:
        vocabulary (dict): Dictionary mapping words to indices.
    """
    # Combine tokenized captions into a single list
    all_words = [word for seq in tokenized_captions for word in seq]

    # Create vocabulary set (remove duplicates)
    vocabulary_set = set(all_words)

    # Create vocabulary dictionary with word indices
    vocabulary = {word: idx + 1 for idx, word in enumerate(vocabulary_set)}

    return vocabulary

# Example usage
if __name__ == "__main__":
    # Example tokenized sequences (replace with your actual data)
    tokenized_captions = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]

    # Build vocabulary
    vocabulary = build_vocabulary(tokenized_captions)

    # Print vocabulary
    print("Vocabulary:")
    for word, idx in vocabulary.items():
        print(f"{word}: {idx}")
