# Raspberry Pi Pico Duino Coin Miner
Contains instructions on how to mine Duino Coin on the Raspberry Pi Pico.
Completed for a Repl.it bounty.

**Instructions:**

-First, make sure python is installed on your main computer.

-The python Requests dependency will allow you to send HTTP/1.1 requests extremely easily, and in this case it is necessary to get the job details from the Duino Coin server. To install the required dependency, run the following command in your main computer terminal: "pip install requests"

-Also, ensure that the DUCO Coin software is installed on your Raspberry Pi via running the following command into your raspberry pi terminal (automatic download):

wget https://raw.githubusercontent.com/revoxhere/duino-coin/master/Tools/duco-install-rpi.sh
sudo chmod a+x duco-install-rpi.sh
./duco-install-rpi.sh

-Before running the program, ensure that you have connected your Raspberry Pi Pico to your computer and identified the correct serial port. Modify the 'pico_serial' variable accordingly.

-Replace "your_username" and "your_password" in the code username and password variables with your actual Duino Coin wallet credentials.

-Once everything is set up, run the program, and it will start mining Duino Coin using the Duino Coin API with the Raspberry Pi Pico interface. The Pico will display the current nonce being processed for visualization. When a solution is found, the program will print the mining statistics, and the mining process will stop.
