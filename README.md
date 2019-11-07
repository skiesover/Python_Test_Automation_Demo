# Python_Test_Automation_Demo
Test Automation project written on Python and using Page Object Model.

Author: **Ildar Lutfullin**

Tools used to create the framework:
1. Python
2. Requests API library

## Project Decription
This project uses Page Object Model. It means that test classes themselves do not contain any logic or functions implementations. Instead all logic, functions and locators are stored inside corresponding page classes. 

**This allows page methods to be reusable and test classes to be more readable.**

All we do in test classes is invoke those functions using fluent pattern:
  ```
To achieve Fluent pattern all page-related functions are not void - instead they return page class.
  ```

Each test class contains test case description with steps and test script itself.

Thank you!
