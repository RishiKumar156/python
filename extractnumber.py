input_str = '1:tengen , 2:jordon, 3:michale , 54:Susie'

# Initialize an empty string to store the extracted integer
extracted_number = ''

# Iterate through each character in the string
for char in input_str:
    # Check if the character is a digit or a minus sign
    if char.isdigit() or (char == '-' and (not extracted_number or extracted_number[-1].isdigit())):
        extracted_number += char
    # else:
    #     # Break the loop if a non-digit character is encountered
    #     break

# Convert the extracted string to an integer
if extracted_number:
    result = int(extracted_number)
    print(result)
else:
    print("No integer found in the string.")
