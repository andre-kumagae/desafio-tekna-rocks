# Desafio Tekna.Rocks - Estágio em Programação

This repository was created to propose a solution for the sixth step of the application process for the position of 'Estágio em Programação (Dev Training Program)' at Tekna.Rocks Brazil.

It has a Python code integrated with the Google Sheets API to access and edit an online Spreadsheet, as well as create function to manipulate its data.

## The Challenge

Create an application in a programming language of your choice (if you are applying for a specific programming language position, for example: node.js programmer, use the language/technology of the position). The application must be able to read a Google Sheets spreadsheet, search for the necessary information, calculate, and write the result to the spreadsheet.

### First Step

* Access the example spreadsheet;

* Make a copy of this spreadsheet: "File > Make a copy";

* Change the spreadsheet name to Software Engineer - Challenge [Your Name];

* Then make the spreadsheet public for editing by anyone with access to the link:

* Use this new spreadsheet into make your challenge;

### Link to my spreadsheet

[ Software Engineer - Challenge [André Alexandre Kumagae Pereira]](https://docs.google.com/spreadsheets/d/1hoY87CzLOdPwfl31fR1gFkP7SJvvwz0Mm9_W5ht9OF8/edit?gid=0#gid=0)

## Rules

* Calculate the situation of each student based on the average of the tests (P1, P2, and P3), according to the table below:

![image](https://github.com/user-attachments/assets/02ebd7f5-2802-4c8e-a613-c6ed8efd8ad6)

* In the case of the number of absences being 25% over than the total number of classes, the student should be classified as " AbsentFailed for Absence" regardless of the Average.
* If the student's situation is "Final Test", will be needed to calculate the "Final Grade for Approval" (fga) using this formula:

```
    5 <=(avg + fga)/2
```

* If the student's situation is different from the "Final Test", fill in the field "Final Grade for Approval"(fga) with zero.
* Round the result up to the next whole number (increase) if necessary.
* Use log lines to monitor application activities.
* The source code texts (attributes, classes, functions, and comments) must be written in English, except for the identifiers and texts predefined in this challenge.
* The candidate must specify the commands that should be used to run the application. * Example of a node.js application:

```bash
    npm install
    npm start
```
* The candidate must publish the source code in a Git repository of their choice (e.g., GitHub, GitLab, bitbucket, etc.).


## Installation

1. Install Python on your machine: https://www.python.org/

2. Download all files of this repository by clicking the green button above named "<> Code", and then "Download ZIP" or you can clone this project using the GIT command bellow;

```bash
    git clone https://github.com/andre-kumagae/desafio-tekna-rocks.git
```

3. Install the required Google libraries on your IDE/Editor or if you are using a terminal, run this command:

```bash
    pip install oauth2client google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2 python-dotenv
```
4. Open the Spreadsheet to view the result: https://docs.google.com/spreadsheets/d/1hoY87CzLOdPwfl31fR1gFkP7SJvvwz0Mm9_W5ht9OF8/edit?gid=0#gid=0

5. Run the file main.py on your Python IDE/editor. You can also run it by double-clicking the file or on a console by using this command below: 

```bash
    python main.py
```

## Demonstration

![example](https://github.com/user-attachments/assets/aee30734-0d0f-417f-81cc-4001d4ecaf34)


## API Documentation

## Packages

* Packages required to connect to the Google Sheets API according to the documentation:

```
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import math
import logging
import os
from dotenv import load_dotenv
```

* Package used to round up the average result:

```
import math
```

* Package used to generate and update the log file with the name 'spreadsheet_update.log":

```
import logging
```

### Constants

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `SCOPE` | `string` | Google Sheets API's URL. |
| `SPREADSHEET_ID` | `string` | Spreadsheet's ID. |
| `CLEAR_RANGE` | `string` | Table range to clear before calculation.  |
| `CLEAR_RANGE` | `string` | Table range to calculate.  |
| `SERVICE_ACCOUNT_INFO` | `dictionary` | Dictionary to get the account service's credentials  |

### Methods

#### check_situation(average, absence)

Calculate tests' average and class frequency for each student to set the corresponding situation:

* Absence being 25% over than the total number of the 60 classes: "AbsentFailed for Absence";
* Test's average below 5.0: "Failed by Grade";
* Test's average over 5.0 and below 7: "Final Test";
* Test's average equals or over 7.0: "Approved";

### clear_fields(sheet)

It will clear Situation and Final Grade columns before calculating to prevent exceptions.

#### calculate_grades(creds)

Receive a parameter named creds to get the credential to access the spreadsheet:

* Calculate the average from the three tests;
* Get the course's situation from check_situation's method;
* If the student's situation is "Final Test", it will calculate the final approval grade (fga) with the suggested formula:

```
    5 <= (average + fga)/2
```
* As the grades in the spreadsheet are on a scale from 0 to 100, but the test requires evaluation on a scale from 0 to 10, the average results were divided by 10 to match this criterion;
* Given a student with the average of 5.3, let's multiply both sides by 2 to eliminate the fraction on the right side:
```
    10 <= (5.3 + fga)
```
* Then subtract 5.3 from both sides to isolate fga:
```
    4.7 <= fga
```
* Reverse the sides of the values to get the final result:
```
    fga >= 4.7
```
* And round up the grade:
```
    fga >= 5
```

### main()

Authorize the access to the spreadsheet with the Acoount service's token.json.

## References

 - [Python quickstart](https://developers.google.com/sheets/api/quickstart/python)
 - [Google Sheets API Overview](https://developers.google.com/sheets/api/guides/concepts)
 - [oauth2client — oauth2client 4.1.2 documentation](https://oauth2client.readthedocs.io/en/latest/index.html)
 - [googleapiclient](https://googleapis.github.io/google-api-python-client/docs/epy/googleapiclient-module.html)
 - [Python Documentation contents — Python 3.13.2 documentation](https://docs.python.org/3/contents.html)
 - [python-dotenv · PyPI](https://pypi.org/project/python-dotenv/)

