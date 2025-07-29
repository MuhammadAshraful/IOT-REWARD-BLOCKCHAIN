# 🌱 NRC Coin – IoT Reward System on Ethereum

This project implements a smart contract-based reward system using a custom ERC-20 token (**NRC Coin**) deployed on the **Ethereum Sepolia Testnet**. The system is designed for use cases like **smart farming**, where IoT sensors (e.g., soil moisture or temperature sensors) are rewarded with tokens for providing accurate, real-time data.

---

## 📌 Project Objectives

- ✅ Create and deploy an ERC-20 token (NRC Coin)
- ✅ Simulate an IoT-based environment where devices are rewarded for sharing data
- ✅ Interact with the blockchain using **Python** and **Web3.py**
- ✅ Store token transaction logs securely on Ethereum (Sepolia)
- ✅ Test automated token transfers using smart contracts

---

## ⚙️ Technologies Used

| Tool | Purpose |
|------|---------|
| **Solidity (v0.8.20)** | Smart Contract development |
| **Remix IDE** | Writing, compiling, and deploying the contract |
| **OpenZeppelin ERC-20** | Secure and standard ERC-20 implementation |
| **MetaMask Wallet** | Interact with the Ethereum Sepolia Testnet |
| **Python (Web3.py)** | Backend interaction with smart contract |
| **Infura** | Accessing Sepolia node as Web3 provider |
| **Etherscan** | Viewing transaction and token data |

---

## 🪙 Smart Contract

### 📄 Contract Name: `NRCCoin.sol`

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract NRCCoin is ERC20 {
    constructor(uint256 initialSupply) ERC20("NRC Coin", "NRC") {
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    function reward(address to, uint256 amount) public {
        _transfer(msg.sender, to, amount * (10 ** decimals()));
    }
}
```

# 🌾 Blockchain-based IoT Sensor Reward System using NRC Tokens

This project demonstrates how smart contracts on Ethereum (Sepolia testnet) can be used to reward IoT devices (e.g., soil moisture sensors) with NRC Tokens. Python interacts with the blockchain via Web3.py and MetaMask using a private key (secured via `.env`). It simulates real-world applications such as smart farming.

---

## 🖥️ Python Interaction Script

The `iot_reward.py` script does the following:

- Connects to Ethereum testnet (Sepolia) using **Infura endpoint**
- Loads **ABI** from Remix IDE export
- Interacts with deployed NRC token contract
- Calls the `reward()` function to simulate giving tokens to a sensor
- Uses a **MetaMask private key** (stored in `.env`) to sign transactions securely

> ⚠️ **Warning:** Never commit or upload your `.env` file or private keys to GitHub.

---

## 🛰️ Use Case: Smart Farming Example

This project simulates a smart agriculture scenario where:

- Soil moisture sensors track data and report to the blockchain
- The smart contract's `reward()` function distributes tokens to working sensors
- Rewards can be customized based on:
  - Sensor uptime
  - Data accuracy
  - Reporting frequency or time intervals

This incentivizes uptime, trust, and transparency in remote agriculture environments.

---

## 📸 Project Demonstrations

All screenshots and supporting evidence are in the `/screenshots/` folder:

- ✅ Remix smart contract deployment
- ✅ Verified transaction hash on Etherscan
- ✅ MetaMask token and balance screenshots
- ✅ Infura project setup screenshot
- ✅ Python Jupyter Notebook backend interaction
- ✅ ETH faucet proof on Sepolia testnet

---

## 🚧 Limitations and Challenges

| Challenge | Description |
|----------|-------------|
| ⛽ Gas Fees | Transactions on mainnet could be expensive |
| 🕒 Latency | Blockchain confirmations are slower than real-time systems |
| 🧱 Hardware Gap | Requires actual IoT devices for full testing |
| 📡 No Oracles | Real-time sensor validation isn't included (no Chainlink used yet) |

---

## 📚 Future Improvements

- 🔌 Integrate real sensors (e.g., **Raspberry Pi** + soil sensor)
- ⛓️ Add **oracles** (e.g., Chainlink) to verify off-chain data
- ⬆️ Upgrade to Layer 2 networks like **Polygon**, **Arbitrum** to reduce fees
- 🌐 Build a frontend **DApp** for farmer dashboard or reward claim interface

---

## 📄 License

This project is open-sourced under the [MIT License](https://opensource.org/licenses/MIT).  
© 2025

---

## 🙋 Author & Supervisor

- **Author:** [Your Full Name]  
- **Supervisor:** [Lecturer’s Name]

---

## 📬 Contact

For questions, suggestions, or collaboration:

- GitHub: [your-github-username]  
- Email: [your-email]


