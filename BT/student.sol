//SPDX-License-Identifier: Unlicensed
pragma solidity >=0.8.0;


contract student{

    struct stud{
        uint256 id;
        string name;
        string class;
        string department;
    }
    stud[] public Students;
    uint256 _ids;


    function addStudent(uint256 id, string memory name, string memory class, string memory department) public {
        stud memory data = stud(id,name, class, department);
        Students.push(data);
    }

    function getStudent(uint256 _id) public view returns(uint256 id,string memory name, string memory class, string memory department){
        require(_id<_ids,"students Id is not present");
        
        for(uint i; i<Students.length;i++){

            if(Students[i].id == _id){
                id = Students[i].id;
                name = Students[i].name;
                class= Students[i].class;
                department = Students[i].department;
                return(id,name,class,department);
            }
        }
    }

    function totalStudents() public view returns(uint256){
        return(_ids);
    }

    fallback() external payable{
        uint256 id = _ids;
		Students.push(stud(id,"abc","class","department"));
        _ids +=1;
	}
     receive() external payable {
        // contract with fallback function requires receive() function
    }
    

}