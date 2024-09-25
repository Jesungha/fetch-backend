# Fetch-Backend Challenge
This guide will walk you through setting up and running this Python project, even if you've never used Python before.
1. Install Python

Go to the official Python website: https://www.python.org/downloads/
Download the latest version of Python for your operating system (Windows, macOS, or Linux).
Run the installer:

On Windows: Make sure to check the box that says "Add Python to PATH" during installation.
On macOS/Linux: Follow the installation prompts.



2. Verify Python Installation

Open a command prompt (on Windows) or terminal (on macOS/Linux).
Type python --version and press Enter.
You should see the Python version number. If you get an error, try python3 --version.

3. Install Required Libraries

In the command prompt or terminal, navigate to the project folder:
Copy cd path/to/your/project/folder

Install the required libraries using pip (Python's package installer):
Copy pip install -r requirements.txt
If that doesn't work, try pip3 pip install -r requirements.txt

4. Run the Backend Server

In the command prompt or terminal, make sure you're in the project folder.
Run the backend server:
Run in terminal  python backend.py
If that doesn't work, try python3 backend.py.
You should see a message saying the server is running, usually on http://127.0.0.1:5000/.
Keep this window open while running tests.

5. Run the Tests

Open a new command prompt or terminal window.
Navigate to the project folder again.
Run the test script:
Copypython testing.py
If that doesn't work, try python3 testing.py.
You should see the test results in the console.

Troubleshooting

If you get a "command not found" error when trying to run Python, make sure Python is correctly added to your system's PATH.
If you get an error about missing modules, make sure you've installed all required libraries (step 3).
If the server doesn't start, check if another program is using port 5000. You can change the port in backend.py if needed.

Project Structure

backend.py: The main server file.
Customer.py: Contains the Customer class implementation.
testing.py: Contains tests for the API endpoints.
