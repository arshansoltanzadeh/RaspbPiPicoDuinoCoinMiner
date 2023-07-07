# Raspberry Pi Pico Duino Coin Miner
Contains instructions on how to mine Duino Coin on the Raspberry Pi Pico.
Completed for a Repl.it bounty.

**Instructions:**

Here's a step-by-step guide on how to set up the Raspberry Pi Pico for mining Duino Coin and how to install Duino Coin on the Pico:

Setup Raspberry Pi Pico for Mining:

1. Connect the Raspberry Pi Pico to your computer using a USB cable.
2. Identify the serial port assigned to the Pico. On Linux, it is usually /dev/ttyACM0, and on Windows, it appears as a COM port (e.g., COM3). If you need any help, this website helps identify serial ports:  https://software.zaber.com/motion-library/docs/guides/find_right_port
3. The python Requests dependency will allow you to send HTTP/1.1 requests extremely easily, and in this case it is necessary to get the job details from the Duino Coin server. To install the required dependency, run the following command in your main computer terminal: "pip install requests"
4. Use a text editor to create a new Python script and copy and paste the code in this repository "mine.py" to the new python file.
5. Modify the following parameters in the code:
   Set the 'username' variable to your Duino Coin wallet interface username.
   Set the 'password' variable to your Duino Coin wallet interface password.
   Update the 'pico_serial' variable with the serial port identified in step 2.
6. Save the Python script with an appropriate name (e.g., duinocoin_miner.py).

Install Duino Coin on Raspberry Pi Pico:

1. Download the Duino Coin software for the Raspberry Pi Pico by visiting the official Duino Coin GitHub repository at https://github.com/revoxhere/duino-coin.
2. On the repository page, click the green "Code" button and select "Download ZIP" to download the repository as a ZIP archive.
3. Extract the downloaded ZIP archive to a convenient location on your computer.
4. Open the extracted folder and locate the duino-coin.ino file.
5. Connect the Raspberry Pi Pico to your computer using a USB cable.
6. Install the required software for uploading code to the Pico by following the instructions in the official Raspberry Pi Pico documentation at https://datasheets.raspberrypi.org/pico/getting-started-with-pico.pdf.
7. Once the Pico is set up and recognized by your computer, open the duino-coin.ino file with the Arduino IDE.
8. In the Arduino IDE, select "Tools" > "Board" and choose "Raspberry Pi Pico".
9. Click the upload button (right arrow icon) to compile and upload the Duino Coin software to the Pico.

After following these steps, you should have the Raspberry Pi Pico set up for mining Duino Coin, and the Duino Coin software installed on the Pico. You can run the Python script you created earlier to start mining Duino Coin using the Pico, and the Pico will display the mining progress via the connected serial port.
