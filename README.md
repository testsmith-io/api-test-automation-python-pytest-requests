# API Test Automation with Python, Pytest, and Requests

[![API Test Automation with Python, Pytest, and Requests](https://github.com/testsmith-io/api-test-automation-python-pytest-requests/actions/workflows/python.yml/badge.svg)](https://github.com/testsmith-io/api-test-automation-python-pytest-requests/actions/workflows/python.yml)

This repository contains example scripts for API test automation using:
- **Python**
- **Requests** for API interaction
- **Pytest** for test execution

## Features
- Examples of GET, POST, and Protected API requests.
- Clear demonstration of test automation practices with assertions and chaining requests.
- Fully automated CI pipeline using GitHub Actions.

## Test API
All examples in this repository are designed to work with the **Practice Software Testing API**, a publicly available API for learning and practicing software testing. You can explore the API documentation and endpoints here:  
👉 **[Practice Software Testing API](https://api.practicesoftwaretesting.com/api/documentation)** 👈

## Examples Included
1. **GET Request**: Fetch a list of brands with `GET /brands`.
2. **Login API**: Authenticate using `POST /login` with an email/password payload.
3. **Protected API Request**: Authenticate, then use a token to fetch data with `GET /invoices`.

## Prerequisites
- **Python 3.9+**
- **pip** (Python package installer)
- A code editor like **VS Code**

## Setup and Run
### 1. Clone the Repository
```bash
git clone https://github.com/testsmith-io/api-test-automation-python-pytest-requests.git
```

### 2. Navigate to the Project Directory
```bash
cd api-test-automation-python-pytest-requests
```

### 3. Set Up a Virtual Environment (Optional, Recommended)
Using a virtual environment ensures that dependencies for this project are isolated from your global Python environment.

#### Create a Virtual Environment

In VS Code open the Command Palette (MacOs: `CMD` + `SHIFT` + `P`, Windows: `CTRL` + `SHIFT` + `P`)

- In the Command Palette, type and select/type: `Python: Select Interpreter`.
- Choose the Python interpreter you want to use from the list OR create a new
one.

This ensures VS Code uses the virtual environment for running and debugging.

#### Install Dependencies
Once the virtual environment is active:
```bash
pip install -r requirements.txt
```

### 4. Run the Tests
```bash
pytest
```

## Automated Workflow
The repository includes a GitHub Actions workflow to automatically build and test the project.
