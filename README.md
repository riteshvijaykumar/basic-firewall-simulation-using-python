# basic-firewall-simulation-using-python

# Firewall

The Firewall is a Python script that simulates a basic firewall functionality. It generates random IP addresses and checks them against a predefined set of rules to determine the appropriate action (allow or block) for each IP address.

## Installation

To use the Firewall script, you will need to have Python installed on your system. You can download the latest version of Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

Once you have Python installed, you can download the `firewall.py` file and save it to your desired location.

## Usage

To run the Firewall script, open a terminal or command prompt and navigate to the directory where you saved the `firewall.py` file. Then, run the following command:

```
python firewall.py
```

This will execute the `main()` function, which will generate 15 random IP addresses, check them against the predefined rules, and print the IP address, the action (allow or block), and the packet number for each IP address.

## API

The Firewall script provides the following functions:

1. `createipaddr(random)`:
   - This function generates a random IP address in the format `192.168.63.{random}`.
   - It takes a single parameter `random`, which is an integer used to generate the last octet of the IP address.
   - The function returns the generated IP address as a string.

2. `checkiprules(ip, rules)`:
   - This function checks the given IP address against the predefined rules.
   - It takes two parameters: `ip`, which is the IP address to be checked, and `rules`, which is a dictionary containing the IP addresses and their corresponding actions (block or allow).
   - If the IP address is found in the `rules` dictionary, the function returns the corresponding action. Otherwise, it returns `"allow"`

## Testing

To test the Firewall script, you can modify the `ip_rules` dictionary in the `main()` function to include different IP addresses and actions. You can also add more test cases to ensure the script is working as expected.
