import { Student } from './models/Student';

// Create an instance of the Student class
const student1 = new Student('Alice', 90);
const student2 = new Student('Bob', 85);

// Display student information
console.log(`Student Name: ${student1.name}, Score: ${student1.score}`);
console.log(`Student Name: ${student2.name}, Score: ${student2.score}`);