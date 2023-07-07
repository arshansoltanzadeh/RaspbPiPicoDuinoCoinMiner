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
