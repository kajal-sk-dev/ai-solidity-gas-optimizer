// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Vulnerable {
    uint256[] public data;

    function add(uint256 x) public {
        data.push(x);
    }

    function sum() public view returns (uint256) {
        uint256 total = 0;
        for (uint256 i = 0; i < data.length; i++) {
            total += data[i];
        }
        return total;
    }
}
