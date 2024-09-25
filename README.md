Here’s a properly formatted README file for your Fetch-Backend Challenge:

---

# Fetch-Backend Challenge

This guide will walk you through setting up and running this Python project, even if you've never used Python before.

## 1. Install Python

1. Go to the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the latest version of Python for your operating system (Windows, macOS, or Linux).
3. Run the installer:
    - **On Windows**: Make sure to check the box that says **"Add Python to PATH"** during installation.
    - **On macOS/Linux**: Follow the installation prompts.

## 2. Verify Python Installation

1. Open a command prompt (on Windows) or terminal (on macOS/Linux).
2. Type the following command and press Enter:
    ```bash
    python --version
    ```
3. You should see the Python version number. If you get an error, try this instead:
    ```bash
    python3 --version
    ```

## 3. Clone Repository & Install Required Libraries

1. Clon this Github Repository
    ```bash
    git clone https://github.com/Jesungha/fetch-backend.git
    ```

2. In the command prompt or terminal, navigate to the project folder:
    ```bash
    cd path/to/your/project/folder
    ```
3. Install the required libraries using `pip` (Python's package installer):
    ```bash
    pip install -r requirements.txt
    ```
    If that doesn't work, try this:
    ```bash
    pip3 install -r requirements.txt
    ```

## 4. Run the Backend Server

1. In the command prompt or terminal, ensure you're in the project folder.
2. Run the backend server:
    ```bash
    python backend.py
    ```
    If that doesn't work, try this:
    ```bash
    python3 backend.py
    ```
3. You should see a message saying the server is running, usually on `http://127.0.0.1:5000/`.
4. Keep this window open while running tests.

## 5. Run the Tests

1. Open a new command prompt or terminal window.
2. Navigate to the project folder again:
    ```bash
    cd path/to/your/project/folder
    ```
3. Run the test script:
    ```bash
    python testing.py
    ```
    If that doesn't work, try this:
    ```bash
    python3 testing.py
    ```
4. You should see the test results in the console.

## Troubleshooting

- **"Command not found" error when running Python**: Ensure Python is correctly added to your system's PATH during installation.
- **Missing modules error**: Make sure you've installed all required libraries (refer to step 3).
- **Server doesn't start**: Check if another program is using port 5000. You can change the port in `backend.py` if needed.

## Project Structure

```
fetch-backend-challenge/
├── backend.py            # The main server file
├── Customer.py           # Contains the Customer class implementation
├── testing.py            # Contains tests for the API endpoints
├── requirements.txt      # Contains the Python dependencies
└── README.md             # Project documentation
```

## 6. Available API

1. /add__
    Method = POST__
    Description: When a user has points added, we will use an /add route that accepts a transaction which contains
    how many points will be added, what payer the points will be added through, and the timestamp for when the
    transaction takes place. The request body for this endpoint will look like the following
    {
        "payer" : "DANNON",
        "points" : 5000,
        "timestamp" : "2020-11-02T14:00:00Z
    }

    How to call:__
    put in Command line or terminal. You can change -d parameter
    ```Bash
    curl -X POST http://localhost:5000/add \
    -H "Content-Type: application/json" \
    -d '{"payer": "DANNON", "points": 300, "timestamp": "2022-10-31T10:00:00Z"}'

    ```

2. /spend__
    Method: POST__
    Description: When a user goes to spend their points, they are not aware of what payer their points were added
    through. Because of this, your request body should look like

    {"points" : 5000}

    How to call:__
    put in Command line or terminal. You can change -d parameter
    ```Bash
    curl -X POST http://localhost:5000/spend \
    -H "Content-Type: application/json" \
    -d '{"points": 5000}'
    ```

3. /balance__
    Method: GET__
    Description: This route should return a map of points the user has in their account based on the payer they were
    added through. This endpoint can be used to see how many points the user has from each payer at any given
    time. Because this is a GET request, there is no need for a request body. This endpoint should always
    return a 200 and give a response body similar to the following:
    
    {
        "DANNON": 1000,
        ”UNILEVER” : 0,
        "MILLER COORS": 5300
    }
    

    How to Call:__
    put in command line or terminal
    ```Bash
    curl http://localhost:5000/balance
    ```
    
---
