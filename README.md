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

* Install Python on your machine: https://www.python.org/

* Download all files of this repository by clicking the green button above named "<> Code", and then "Download ZIP" or you can clone this project using the GIT command bellow;

```bash
    git clone https://github.com/andre-kumagae/desafio-tekna-rocks.git
```

* Install the required Google libraries:

```bash
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
* Open the Spreadsheet: https://docs.google.com/spreadsheets/d/1hoY87CzLOdPwfl31fR1gFkP7SJvvwz0Mm9_W5ht9OF8/edit?gid=0#gid=0

* Run the file main.py on a Python IDE/editor or on a console by using this command below: 

```bash
    python main.py
```

## API Documentation

## Packages

* Packages required to connect to the Google Sheets API according to the documentation:

```
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
```

* Package used to round up the average result:

```
import math
```

* Package used to generate and update the log file:

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

Authorize the access to the spreadsheet with the credentials.json and token.js files.

## References

 - [Python quickstart](https://developers.google.com/sheets/api/quickstart/python)
 - [Google Sheets API Overview](https://developers.google.com/sheets/api/guides/concepts)

