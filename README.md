# SEQA Exam — Selenium Test + Jenkins CI + ZAP PenTest

## Description
This repository contains the solution for the SEQA exam.

The project tests this target:  
[`https://the-internet.herokuapp.com/challenging_dom`](https://the-internet.herokuapp.com/challenging_dom)

It covers:
- Selenium testing
- Jenkins CI integration
- OWASP ZAP-based penetration testing of Gruyere

---

## What to Check (For Examiner)

Please use the following list to verify each part of the task:

 Task                                | Location in Repository                         |
|------------------------------------|--------------------------------------------------|
|  Selenium test code              | `Exam_SEQA/test_challenging_dom_firefox.py`      |
|  Screenshots from test           | `Exam_SEQA/01_page_loaded.png`, ..., `04_final.png` |
|  Jenkins success screenshot      | `Exam_SEQA/Jenkins console Titkov.jpg`           |
|  Jenkins build execution view    | `Exam_SEQA/Jenkins execute Titkov.jpg`           |
|  ZAP scan result (HTML report)   | `Exam_SEQA/ZAP by Checkmarx Scanning Report Titkov.htm` |
| ZAP GUI screenshot              | `Exam_SEQA/ZAP Gruyere Screenshot.jpg`           |

---

## Selenium Test — What it Verifies

- 3 UI Buttons are visible (blue, red, green)
- Table has 10 rows and correct headers
- `<canvas>` is present and screenshot taken
- Screenshots are saved on each step

---

## How to Run the Test

You can run the test using:

```bash
pytest test_challenging_dom_firefox.py
