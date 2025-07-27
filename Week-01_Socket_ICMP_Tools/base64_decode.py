import base64 as b

try:
    print(f"Enter the base 64 string to decode : ")
    input_str = input(f">>> ")
    print(f"\nDecoded string : {b.b64decode(input_str).decode('utf-8')}")
except Exception as e:
    print(f"Error {e} \noccured while running the program.\nPlease try again! ")
