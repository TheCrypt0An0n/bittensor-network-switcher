#!/usr/bin/env python3
import os
import sys
import json
import argparse

class BittensorNetworkSwitcher:
    def __init__(self):
        # Default config paths
        self.home_dir = os.path.expanduser('~')
        self.bittensor_dir = os.path.join(self.home_dir, '.bittensor')
        self.config_path = os.path.join(self.bittensor_dir, 'network_config.json')
        
        # Ensure bittensor directory exists
        os.makedirs(self.bittensor_dir, exist_ok=True)

    def read_config(self):
        """Read existing config or create a default one."""
        try:
            with open(self.config_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {'network': 'Not set'}

    def write_config(self, config):
        """Write configuration to network_config.json."""
        with open(self.config_path, 'w') as f:
            json.dump(config, f, indent=4)

    def switch_network(self, network):
        """
        Switch between mainnet and testnet.
        
        :param network: 'mainnet' or 'testnet'
        """
        # Validate network input
        if network not in ['mainnet', 'testnet']:
            print(f"Error: Invalid network '{network}'. Choose 'mainnet' or 'testnet'.")
            sys.exit(1)

        # Update configuration
        config = self.read_config()
        config['network'] = network
        self.write_config(config)
        
        print(f"✅ Successfully set network to {network}")
        print("Note: You may need to restart your Bittensor services to apply this change.")

    def check_current_network(self):
        """Check and display current network."""
        config = self.read_config()
        current_network = config.get('network', 'Not set')
        print(f"Current network: {current_network}")

    def interactive_mode(self):
        """Interactive network switching."""
        print("🌐 Bittensor Network Switcher")
        print("1. Switch to Mainnet")
        print("2. Switch to Testnet")
        print("3. Check Current Network")
        print("4. Exit")

        while True:
            try:
                choice = input("Enter your choice (1-4): ").strip()

                if choice == '1':
                    self.switch_network('mainnet')
                elif choice == '2':
                    self.switch_network('testnet')
                elif choice == '3':
                    self.check_current_network()
                elif choice == '4':
                    break
                else:
                    print("Invalid choice. Please try again.")
            except KeyboardInterrupt:
                print("\nOperation cancelled.")
                break

def main():
    parser = argparse.ArgumentParser(description='Bittensor Network Switcher')
    parser.add_argument('--network', choices=['mainnet', 'testnet'], 
                        help='Switch to specific network')
    parser.add_argument('--check', action='store_true', 
                        help='Check current network')
    
    args = parser.parse_args()

    switcher = BittensorNetworkSwitcher()

    if args.network:
        switcher.switch_network(args.network)
    elif args.check:
        switcher.check_current_network()
    else:
        switcher.interactive_mode()

if __name__ == '__main__':
    main()
