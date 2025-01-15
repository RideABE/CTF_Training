def custom_base_decode(ciphertext, base_table):
    """
    Decode the given ciphertext using a custom base table with variable length.

    Args:
        ciphertext (str): The encoded string.
        base_table (str): The custom base table string.

    Returns:
        bytes: Decoded byte sequence.
    """
    base = len(base_table)
    if base < 2:
        raise ValueError("Base table must have at least 2 unique characters.")
    
    # Map characters in the base table to their respective values
    base_map = {char: index for index, char in enumerate(base_table)}
    
    # Convert ciphertext to an integer value using the custom base
    decoded_value = 0
    for char in ciphertext:
        if char not in base_map:
            raise ValueError(f"Character {char} is not in the base table.")
        decoded_value = decoded_value * base + base_map[char]
    
    # Convert the integer value to bytes
    byte_array = []
    while decoded_value > 0:
        byte_array.append(decoded_value & 0xFF)
        decoded_value >>= 8
    
    return bytes(reversed(byte_array))

# Example usage
base_table = "9876543210qwertyuiopasdfghjklzxcvbnmMNBVCXZLKJHGFDSAPOIUYTREWQ"  # Custom base table
ciphertext = "7dFRjPItGFkeXAALp6GMKE9Y4R4BuNtIUK1RECFlU4f3PomCzGnfemFvO"  # Encoded ciphertext

# Decode
decoded_bytes = custom_base_decode(ciphertext, base_table)
print("Decoded bytes:", decoded_bytes)
print("Decoded string:", decoded_bytes.decode('utf-8', errors='ignore'))
