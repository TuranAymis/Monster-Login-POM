# Monster Login Automation

A UI test automation project developed with Python, Selenium WebDriver, and the Page Object Model design pattern.

The project automates the login flow on the Monster Notebook website and demonstrates how page interactions, test scenarios, and WebDriver management can be organized into reusable components.

## Project Purpose

The main goals of this project are:

- Automate a web login scenario with Selenium
- Apply the Page Object Model design pattern
- Separate page locators and actions from test logic
- Manage browser initialization through a reusable utility class
- Create a simple and maintainable UI automation structure

## Demo

<img src="docs/demo.gif" alt="Monster Login Automation Demo" width="100%">

## Tech Stack

- Python
- Selenium WebDriver
- unittest
- WebDriver Manager
- Page Object Model
- Google Chrome

## Project Structure

```text
Monster-Login-POM/
├── docs/
│   └── demo.gif
├── pages/
│   └── login_page.py
├── tests/
│   └── test_login.py
├── utils/
│   └── driver_manager.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Project Components

### Login Page

`pages/login_page.py` contains:

- Login page locators
- Email and password input actions
- Login button interaction
- Successful login verification

### Login Test

`tests/test_login.py` contains:

- Test setup and teardown methods
- The successful login scenario
- Login result assertion

### Driver Manager

`utils/driver_manager.py` contains:

- ChromeDriver installation
- Chrome browser initialization
- Browser window configuration
- WebDriver shutdown logic

## Prerequisites

Make sure the following tools are installed:

- Python 3.10 or later
- Google Chrome
- Git

Check your Python installation:

```bash
python --version
```

## Installation

Clone the repository:

```bash
git clone https://github.com/TuranAymis/Monster-Login-POM.git
```

Open the project directory:

```bash
cd Monster-Login-POM
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows Git Bash:

```bash
source .venv/Scripts/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Test Credentials

The current test contains placeholder credentials:

```python
email = "test@kullanici.com"
password = "sifre"
```

Replace these values locally with valid test account credentials before running the test.

Do not commit real email addresses, passwords, or other sensitive information to the repository.

A recommended future improvement is loading credentials from environment variables.

## Running the Test

Run the login test with:

```bash
python -m unittest tests/test_login.py -v
```

The test performs the following steps:

1. Starts Google Chrome
2. Opens the Monster Notebook login page
3. Enters the email address and password
4. Clicks the login button
5. Verifies that the logged-in user element is visible
6. Closes the browser

## Dependencies

The project uses:

```text
selenium
webdriver-manager
```

WebDriver Manager downloads and configures a compatible ChromeDriver automatically.

Some corporate networks, proxies, or custom certificate environments may prevent WebDriver Manager from downloading the driver because of SSL certificate verification errors.

## Current Test Coverage

The current project includes:

- Successful login scenario
- Browser setup before the test
- Browser cleanup after the test
- Explicit waits for page elements
- Successful login UI verification

## Possible Improvements

- Move credentials to environment variables
- Add invalid login scenarios
- Add empty field validation tests
- Add reusable test data
- Replace broad exception handling with specific Selenium exceptions
- Add screenshots for failed tests
- Add test reports
- Add logging
- Add cross-browser testing
- Add GitHub Actions for continuous integration

## Author

**Turan Aymış**

Senior Software QA Engineer

[GitHub Profile](https://github.com/TuranAymis)
