import numpy as np
import os
from tensorflow.keras.preprocessing.text import Tokenizer

def tokenize_captions(captions):
    """
    Tokenize captions using TensorFlow Tokenizer.

    Args:
        captions (list): List of captions.

    Returns:
        tokenizer (Tokenizer): Tokenizer object fitted on the captions.
        sequences (list): List of tokenized sequences.
    """
    # Initialize Tokenizer
    tokenizer = Tokenizer()
    
    # Fit Tokenizer on Captions
    tokenizer.fit_on_texts(captions)
    
    # Tokenize Captions
    sequences = tokenizer.texts_to_sequences(captions)
    
    return tokenizer, sequences

# Example usage
if __name__ == "__main__":
    captions = []
    for filename in os.listdir('./data/captions'):
        if not filename.endswith('.txt'):
            continue
        with open(os.path.join('./data/captions', filename), 'r') as file:
            caption = file.read().strip()
            captions.append(caption)

    # Tokenize captions
    tokenizer, sequences = tokenize_captions(captions)

    # Print tokenized sequences
    print("Tokenized Sequences:")
    for seq in sequences:
        print(seq)

    # Vocabulary size
    vocab_size = len(tokenizer.word_index) + 1
    print("Vocabulary Size:", vocab_size)
