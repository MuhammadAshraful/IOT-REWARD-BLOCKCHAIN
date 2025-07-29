// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract NRCCoin is ERC20 {
    constructor(uint256 initialSupply) ERC20("NRC Coin", "NRC") {
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    // Anyone can call this and send tokens from their own balance
    function reward(address to, uint256 amount) public {
        _transfer(msg.sender, to, amount * (10 ** decimals()));
    }
}
