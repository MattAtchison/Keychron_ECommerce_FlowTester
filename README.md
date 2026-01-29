# Ecommerce Testing Bot

A Python-based Selenium automation project that simulates a core ecommerce user journey on a live retail website, including product browsing, cart interactions, and checkout initiation. The project is structured using object-oriented design and modular helper functions to support scalable automation workflows.

---

## Features

- Object-oriented Selenium automation framework (`EcommerceTesting` class)
- Automated navigation to product categories
- Carousel interaction and product selection
- Add-to-cart and checkout flow automation
- Login flow initiation with optional manual form entry module
- Modular helper function for manual checkout data input

---

## Tools & Technologies

- **Python 3**
- **Selenium WebDriver**
- **Google Chrome + ChromeDriver / Selenium Manager**
- Object-Oriented Programming (OOP)
- Explicit waits (`WebDriverWait`, `ExpectedConditions`)
- Modular Python project structure

---

## Next Steps

- Add popup and cookie banner handling for more robust automation  
- Implement assertions to validate cart contents and pricing  
- Add structured logging and automatic screenshots on failure  
- Introduce configurable login strategies (manual vs credential-based)  
- Refactor selectors into reusable utility methods  
- Convert workflows into automated test cases using `pytest`  
- Add CI integration for automated test execution  

---
