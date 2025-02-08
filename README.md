To get interactive to the switching tool use this: 
python3 ~/bittensor-network-switcher/bittensor_network_switcher.py


To check which network you are using use this: 
python3 ~/bittensor-network-switcher/bittensor_network_switcher.py --check

To get into bittensor venv :
~/bittensor-network-switcher$ source ~/bittensor-venv/bin/activate

To check Bittensor Version : btcli --version

To see your wallet use this: btcli w list

Then check your specific wallet:
btcli wallet inspect --wallet.name claudetaotensor

We can also check the overview:

btcli wallet overview --wallet.name claudetaotensor

wallet balance:
btcli wallet balance --wallet.name claudetaotensor


