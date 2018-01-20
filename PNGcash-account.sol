pragma solidity ^0.4.18;

contract Courses {
    
    struct Account {
        uint balance;
        address owner;
        string fName;
        string lName;
    }

    modifier onlyOwner {
       require(msg.sender == owner);
       _;
   }

   function 
    
    mapping (address => Account) accounts;
    address[] public accountAccts;
    
    function setInstructor(address _address, uint _age, string _fName, string _lName) onlyOwner public {
        var account = accounts[_address];
        
        account.age = _age;
        account.fName = _fName;
        account.lName = _lName;
        
        accountAccts.push(_address) -1;
    }
    
    function getAccounts() view public returns(address[]) {
        return accountAccts;
    }
    
    function getAccount(address _address) view public returns (uint, string, string) {
        return (accounts[_address].age, accounts[_address].fName, accounts[_address].lName);
    }
    
    function countAccounts() view public returns (uint) {
        return accountAccts.length;
    }
    
}
