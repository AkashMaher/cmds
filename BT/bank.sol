// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0;

contract bank_account{

    mapping(address => uint) public user_balance;
    mapping(address => bool) public is_user;

    function create_account() public {
        require(!is_user[msg.sender], "Account already exist");
        is_user[msg.sender] = true;
    }

    function deposit(uint256 amount) external payable {
        require(is_user[msg.sender],"User Account Not Found");
        require(msg.value>=amount,"You don't have sent enough amount to deposit");
        user_balance[msg.sender] += amount;  
    }

    function withdraw(uint256 amount) external payable {
        require(is_user[msg.sender],"User Account Not Found");
        require(user_balance[msg.sender]>=amount,"You don't have enough balance to withdraw");
        require(payable(msg.sender).send(amount));
        user_balance[msg.sender] -= amount; 
    }
}