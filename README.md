# Raspberry Pi Pico Duino Coin Miner
Contains Python script and instructions on how to mine Duino Coin on the Raspberry Pi Pico.
Completed for a Repl.it bounty.

**Instructions:**

-The python Requests dependency will allow you to send HTTP/1.1 requests extremely easily, and in this case it is necessary to get the job details from the Duino Coin server. To install the required dependency, run the following command in your terminal:

pip install requests

-Also, ensure that the DUCO Coin software is installed on your Raspberry Pi via the following command (automatic download):

wget https://raw.githubusercontent.com/revoxhere/duino-coin/master/Tools/duco-install-rpi.sh
sudo chmod a+x duco-install-rpi.sh
./duco-install-rpi.sh

-Before running the program, ensure that you have connected your Raspberry Pi Pico to your computer and identified the correct serial port. Modify the 'pico_serial' variable accordingly.

-Replace "your_username" and "your_password" in the username and password variables with your actual Duino Coin credentials.

-Once everything is set up, run the program, and it will start mining Duino Coin using the Duino Coin API with the Raspberry Pi Pico interface. The Pico will display the current nonce being processed for visualization. When a solution is found, the program will print the mining statistics, and the mining process will stop.

**Code:**

# Import required libraries 
''' 
-'requests' dependency to make Duino Coin server job requests.
-'hashlib' module to implement a common interface to many different secure hash and message digest algorithms, 
including the FIPS secure hash algorithm SHA1, which will be required because the DUCO-S1 Duino Coin mining algorithm is based off of the SHA1 hash chain.
-'time' module to keep track of the time during mining operations.
'''

import requests
import hashlib
import time

# Duino Coin mining parameters
username = "your_username"  # Replace with your Duino Coin username
password = "your_password"  # Replace with your Duino Coin password
server_url = "https://server.duinocoin.com"  # Duino Coin server URL
pico_serial = "/dev/ttyACM0"  # Replace with the serial port of your Raspberry Pi Pico

# Connect to the Raspberry Pi Pico
pico = open(pico_serial, "wb")

# Function to send serial data to the Pico
def send_serial_data(data):
    pico.write(data.encode())

# Function to mine Duino Coin
def mine_duino_coin():
    try:
        # Get job details from the Duino Coin server
        job = requests.get(f"{server_url}/miner.json").json()
        difficulty = job["difficulty"]
        block = job["block"]
        start_time = time.time()

        # Mine the coin by iterating through the nonces
        for nonce in range(1000000000):
            # Generate the hash of the job details and nonce
            data = f"{block}{nonce}".encode()
            hash_result = hashlib.sha1(data).hexdigest()

            # Check if the generated hash meets the difficulty requirement
            if int(hash_result, 16) < difficulty:
                # Solution found! Send it to the server
                response = requests.get(
                    f"{server_url}/mine.php?username={username}&password={password}&"
                    f"algorithm=ducos1&hashrate=0&private_key=0&public_key=0"
                    f"&nonce={nonce}&argon=0&bip32=0"
                ).json()

                if "success" in response and response["success"]:
                    # Print mining statistics
                    print(f"\nSolution found!\n"
                          f"Hashrate: {response['hashrate']} H/s\n"
                          f"Difficulty: {response['difficulty']}\n"
                          f"Block value: {response['block_value']} DUCO\n"
                          f"Elapsed time: {round(time.time() - start_time, 2)} seconds\n"
                          f"Response: {response['accepted']}")
                else:
                    # Error in API response
                    print("Error in API response:", response.get("message"))

                # Stop mining
                break

            # Print mining progress
            if nonce % 1000000 == 0:
                print(f"Mining... Nonce: {nonce}")

            # Send the nonce to the Pico for visualization
            send_serial_data(str(nonce))

    except requests.exceptions.RequestException as e:
        # Error in making the request to the server
        print("Error in making the request:", str(e))

# Start mining
mine_duino_coin()

# Close the Pico connection
pico.close()
