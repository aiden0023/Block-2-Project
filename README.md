# Block 2 Project

## Description
A simple, but fake, sig-in and log-in script that simulates signing-in and logging-in to an application; this code is very barebones, but uses basic logic
to show how simple a sign-in and log-in script can be. This program stores account information (with hashed passwords) locally to a secret file to simulate
a database.

## Features
- A simple password strength checker.
- Utilization of the "Have I Been Pwned" API to check if the password has been in a data breach.
- A debugger method that can be modified to add simple debugging tests to the program.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/aiden0023/Block-2-Project.git
   ```
2. Make sure Python is installed onto your OS.
3. Download the requests library for Python:
   ```sh
   pip install requests
   ```
4. Navigate to the project folder and run the program:
   ```sh
   python main.py
   ```

## Warnings
This program and tool is for educational use only and should never be used in a real-life authentication program; this program is to simply teach the
basics of how authentication scripts work. While using this script, for security reasons please do not put in any real log-in information that you 
currently use. Do not use this program to secure any sensitive information.

## Ethical Considerations
Again, do not use any part of this code in any real authentication system softwares. Because account information is stored locally, it is easy for
malicious actors to access this information.
