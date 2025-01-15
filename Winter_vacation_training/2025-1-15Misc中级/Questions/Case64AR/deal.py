import base64

def caesar_cipher_base64(text, base_table, shift, mode="encode"):
    """
    Perform Caesar cipher encoding/decoding on a Base64 string.

    Args:
        text (str): Input text (Base64 encoded or decoded).
        base_table (str): Base64 character table.
        shift (int): Offset for the Caesar cipher.
        mode (str): "encode" for encoding, "decode" for decoding.

    Returns:
        str: Encoded or decoded text.
    """
    if mode == "decode":
        shift = -shift  # Reverse the shift for decoding

    # Map input characters through the Base64 table with the shift
    transformed_text = ""
    for char in text:
        if char in base_table:
            # Find the character index and apply the shift
            index = (base_table.index(char) + shift) % len(base_table)
            transformed_text += base_table[index]
        else:
            # Preserve characters not in the base table (e.g., padding '=' or newlines)
            transformed_text += char
    return transformed_text


# Base64 character table
base_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# Input Base64-encoded string
ciphertext = "OoDVP4LtFm7lKnHk+JDrJo2jNZDROl/1HH77H5Xv"  # Replace with your text

# Loop through all possible shifts
for shift in range(1, 65):
    # Decode using the current shift
    decoded_text = caesar_cipher_base64(ciphertext, base_table, shift, mode="decode")
    try:
        # Try decoding Base64 to see if it is valid
        original_data = base64.b64decode(decoded_text).decode('utf-8', errors='ignore')
        print(f"Shift: {shift}, Decoded Base64: {decoded_text}, Original Text: {original_data}")
    except Exception as e:
        # If decoding fails, print the shifted Base64 text
        print(f"Shift: {shift}, Decoded Base64: {decoded_text} (Invalid Base64)")
