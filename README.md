# SEQA Exam — Selenium Test + Jenkins CI

## Description
This project contains an automated test to check the page: 
`https://the-internet.herokuapp.com/challenging_dom`

The test is implemented using:
- **Python + pytest**
- **Selenium WebDriver (Firefox + geckodriver)**
- **Jenkins CI**

## What the test checks:
- The presence of 3 buttons (by color)
- The presence of a table with 10 rows and correct headers
- The presence of the `<canvas>` element and its screenshot creation
- Screenshots are saved at each stage (page, buttons, final)

## How to run
```bash
pytest test_challenging_dom_firefox.py
