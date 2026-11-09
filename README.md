# Code-Based URL Shortener

A lightweight, console-based URL shortener simulation built in Python. This project mimics the core logic of production link shorteners by generating unique alphanumeric codes, storing them in memory, and redirecting users automatically.

---

## Features

* **Custom Code Generation:** Automatically generates a unique 5-character alphanumeric key for every long URL.
* **Simulated Short Domain:** Formats links cleanly with a custom mock domain (`http://curto.fy/CODE`).
* **Smart Input Handling:** Accepts either the short code or the full short link when opening a URL.
* **Auto-Redirection:** Uses Python's built-in `webbrowser` module to automatically launch the original link in your default browser.
* **Styled CLI Menu:** Features a clean, terminal-friendly user interface with input validation.

---

## Technologies Used

* **Python 3.x**
* `random` & `string` (for generating unique keys)
* `webbrowser` (for automated redirection)

---

## How to Run

1. Make sure you have **Python** installed on your machine.
2. Clone this repository or download the Python script:
   ```bash
   git clone https://github.com/Arthur137116/code-based-URL-shortener
