# Lab 6 – Code and Branch Coverage Analysis

## 1\. Aim

To perform code coverage and branch coverage analysis on a Python application using Pytest and Coverage.py. The objective is to design test cases that execute all statements and decision branches in the application.

## 2\. Project Description

This lab implements a Traffic Fine Management System that calculates speeding fines, determines driving license actions based on penalty points, and calculates the total fine amount.

The application contains three main functions:

1. `speeding\_fine()` – Calculates fines based on vehicle speed, speed limit, and zone.
2. `license\_action()` – Determines the license action based on penalty points, commercial vehicle status, and repeat offender status.
3. `total\_penalty()` – Calculates the total penalty, handles negative fines, and limits the maximum penalty to 10,000.

## 3\. Tools and Technologies

* Python
* Pytest
* Coverage.py
* Visual Studio Code
* Git and GitHub

## 4\. Project Files

```text
lab6/
├── traffic\_fine.py
├── test\_traffic\_fine.py
├── CodeCoverageTest\_XXXX\_application.py
├── BranchCoverageTest\_XXXX\_application.py
├── README.md
├── code\_coverage.png
└── branch\_coverage.png
```

## 5\. Code Coverage Analysis

Code coverage measures how many executable statements in the application are executed by the test cases.

### Test File

`CodeCoverageTest\_XXXX\_application.py`

### Command

```bash
pytest --cov=traffic\_fine --cov-report=term-missing CodeCoverageTest\_XXXX\_application.py
```

### Result

* Total test cases: 17
* Passed test cases: 17
* Failed test cases: 0
* Total statements: 35
* Missed statements: 0
* Code coverage: 100%

### Screenshot

!\[Code Coverage](code\_coverage.png)

## 6\. Branch Coverage Analysis

Branch coverage measures whether each possible outcome of a decision statement has been executed by the test cases. It ensures that both true and false outcomes of conditional statements are tested.

### Test File

`BranchCoverageTest\_XXXX\_application.py`

### Command

```bash
pytest --cov=traffic\_fine --cov-branch --cov-report=term-missing BranchCoverageTest\_XXXX\_application.py
```

### Result

* Total test cases: 20
* Passed test cases: 20
* Failed test cases: 0
* Total statements: 35
* Missed statements: 0
* Total branches: 26
* Partial branches: 0
* Branch coverage: 100%

### Screenshot

!\[Branch Coverage](branch\_coverage.png)

## 7\. Overall Results

|Coverage Type|Test Cases|Coverage|
|-|-:|-:|
|Code Coverage|17|100%|
|Branch Coverage|20|100%|
|Total|37|100%|

Both code coverage and branch coverage achieved 100%.

## 8\. Conclusion

In this lab, code coverage and branch coverage analysis were successfully performed on the Traffic Fine Management System using Pytest and Coverage.py.

A total of 37 test cases were executed successfully. All 35 executable statements and all 26 decision branches were covered.

Therefore, the application achieved 100% statement coverage and 100% branch coverage, demonstrating that all identified statements and decision outcomes were exercised by the test cases.

## 9\. Repository

GitHub Repository: https://github.com/ashaamrut227-cmyk/SE-lab6

