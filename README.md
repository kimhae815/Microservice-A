# Microservice-A

## Overview

This microservice receives a data array containing the number of students and the percentage of students that received each grade.<br />
It will return a different data array that displays the number of students that received each grade.

It communicates via Rest API.

## Communication Contract

## How to Request Data

Make a POST request with a data array in the following format:<br />
{100, {"A": 40, "B": 25, "C": 35}]

Example Request:<br />
POST http://127.0.0.1:5000/statistics HTTP/1.1<br />
content-type: application/json<br />

[100, {"A": 40, "B": 25, "C": 5}]


## How to Receive Data

The POST request will return a dictionary displaying the number of students who received each grade.<br />
The format will be as follows:<br />
{<br />
&emsp;"A": x<br />
&emsp;"B": x<br />
&emsp;"C": x<br />
)<br />

## UML Sequence Diagram

<img src="https://github.com/user-attachments/assets/0e0ce969-fc38-4b22-85a2-8bbb2c8c0977" width="800">
