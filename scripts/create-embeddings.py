from tensorflow.keras.preprocessing.sequence import pad_sequences

def numerical_representation(tokenized_captions, vocabulary, max_length):
    """
    Convert tokenized captions into numerical representations.

    Args:
        tokenized_captions (list): List of tokenized sequences.
        vocabulary (dict): Dictionary mapping words to indices.
        max_length (int): Maximum length of sequences after padding.

    Returns:
        numerical_seqs (numpy.ndarray): Array of numerical sequences.
    """
    # Map words to indices in the vocabulary
    numerical_seqs = [[vocabulary.get(word, 0) for word in seq] for seq in tokenized_captions]

    # Pad sequences to ensure uniform length
    numerical_seqs = pad_sequences(numerical_seqs, maxlen=max_length, padding='post')

    return numerical_seqs

# Example usage
if __name__ == "__main__":
    # Example tokenized sequences (replace with your actual data)
    tokenized_captions = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]

    # Example vocabulary (replace with your actual vocabulary)
    vocabulary = {'<pad>': 0, '<unk>': 1, 'word1': 2, 'word2': 3, 'word3': 4}

    # Maximum sequence length after padding
    max_length = 10

    # Convert tokenized captions to numerical representations
    numerical_seqs = numerical_representation(tokenized_captions, vocabulary, max_length)

    # Print numerical representations
    print("Numerical Representations:")
    print(numerical_seqs)
