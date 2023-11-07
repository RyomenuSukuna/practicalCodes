// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract StudentData {
 struct Student {
 uint256 studentId;
 string name;
 uint256 age;
 }
 Student[] public students;
 // Function to add a new student to the array
 function addStudent(uint256 _studentId, string memory _name, uint256 _age) public {
 Student memory newStudent = Student(_studentId, _name, _age);
 students.push(newStudent);
 }
 // Function to get the total number of students
 function getNumberOfStudents() public view returns (uint256) {
 return students.length;
 }
 // Fallback function to receive Ether
 receive() external payable {}
 // Fallback function to reject Ether
 fallback() external {
 revert("This contract does not accept Ether directly.");
 }
}
