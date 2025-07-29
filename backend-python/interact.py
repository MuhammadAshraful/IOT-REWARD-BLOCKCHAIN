from web3 import Web3
import json
import os
from dotenv import load_dotenv

load_dotenv()

infura_url = os.getenv("INFURA_URL")
web3 = Web3(Web3.HTTPProvider(infura_url))

print("✅ Connected" if web3.is_connected() else "❌ Not connected")

contract_address = Web3.to_checksum_address(os.getenv("CONTRACT_ADDRESS"))
wallet_address = Web3.to_checksum_address(os.getenv("WALLET_ADDRESS"))
recipient = Web3.to_checksum_address(os.getenv("RECIPIENT"))
private_key = os.getenv("PRIVATE_KEY") 

# Get the folder where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
abi_path = os.path.join(script_dir, "abi.json")

# Open the file safely
with open(abi_path) as f:
    abi = json.load(f)



contract = web3.eth.contract(address=contract_address, abi=abi)

def simulate_sensor(sensor_id, recipient):
    print(f"📡 Sensor {sensor_id} uploading...")

    nonce = web3.eth.get_transaction_count(wallet_address)

    txn = contract.functions.reward(recipient, 1).build_transaction({
        'chainId': 11155111,
        'gas': 200000,
        'gasPrice': web3.to_wei('3', 'gwei'),
        'nonce': nonce
    })

    signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)

    # ✅ FIX HERE: Use raw_transaction (all lowercase)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)

    print("✅ Tx sent. Hash:", tx_hash.hex())
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=300)
    print("⛏️ Mined in block:", tx_receipt.blockNumber)

    if tx_receipt.status == 1:
        print("✅ Transaction succeeded")
    else:
        print("❌ Transaction failed")

    

simulate_sensor("Sensor-A", "0x7f76b4015e08b24313c56Cc5e34489001144BDE7")
