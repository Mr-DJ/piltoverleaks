import os
import json
import random
import string

def main():
    # Read the flag from the environment variable
    flag = os.getenv('FLAG', 'HEXTECH{default_flag_value}')
    flag = "picoCTF{d0n1_l34k_st4t35_" + ''.join(random.choices(string.ascii_letters, k=7)) + "}"
	
    # Create metadata dictionary
    metadata = {
        'flag': flag
    }

    # Write metadata to json file
    with open('/challenge/metadata.json', 'w') as f:
        json.dump(metadata, f)

    # Update the config.py file with the flag
    config_path = '/challenge/config.py'
    with open(config_path, 'r') as f:
        config_content = f.read()

    config_content = config_content.replace(
        "FLAG = os.getenv('FLAG', 'HEXTECH{default_flag_value}')",
        f"FLAG = '{flag}'"
    )

    with open(config_path, 'w') as f:
        f.write(config_content)

if __name__ == "__main__":
    main()
