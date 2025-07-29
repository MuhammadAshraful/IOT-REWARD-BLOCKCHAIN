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
