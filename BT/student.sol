//SPDX-License-Identifier: Unlicensed
pragma solidity >=0.8.0;

contract Student{

    struct student{
        uint prn;
        string name;
        string class;
        string department;
    }
    uint256 PRN;
    mapping(uint => student)  studentMap;

    function addStudent(string memory name, string memory class, string memory department) public {
        PRN +=1;
        studentMap[PRN] = student(PRN,name, class, department);
        
    }

    function getStudent(uint256 _id) public view returns( student memory ){     
        return studentMap[_id] ;
    }

    function totalStudents() public view returns(uint256){
        return(PRN);
    }

    fallback() external {
        addStudent("Unknown","FE","CSE");
	}
}