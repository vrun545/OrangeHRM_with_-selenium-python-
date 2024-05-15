
# Selenium Python Automation Project

This project demonstrates automated testing of the [OrangeHRM](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login) website using Selenium with Python and pytest framework. The tests are organized using the Page Object Model (POM) design pattern for improved maintainability and readability.

## Introduction

Automated testing is crucial for ensuring the quality and stability of web applications. This project demonstrates how to automate testing of the OrangeHRM website using Selenium WebDriver, Python, and pytest framework. By implementing the Page Object Model (POM), we organize our tests into reusable components, making the test suite more maintainable and scalable.

## Features

- Automated testing of login functionality.
- Demonstrates usage of POM design pattern.
- Generates HTML reports for test execution results.

## Prerequisites

Before running the tests, ensure you have the following installed:

- Python (version 3.7 or higher)
- pip (Python package installer)
- Chrome or Firefox browser
- ChromeDriver or GeckoDriver (for running tests in Chrome or Firefox)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-repo
   ```


3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```


## Usage

To run the tests, use the following command:

```bash
pytest -v
```

This command will execute all the test cases and generate HTML reports in the `htmlReports` directory.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize the README.md file according to your project's specific details and requirements. You can add more sections or information as needed.
