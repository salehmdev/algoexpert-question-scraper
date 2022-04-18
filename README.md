# AlgoExpert Question Scraper

Script to grab the question names from Algoexpert.io.

## Setup

1. Setup python environment. Python version 3.8+ should work. I personally use `venv`:

```bash
py -3.10 -m venv env 
```

2. Install dependencies

```bash
pip install -r ./requirements.txt
```

3. Download and unzip a chrome webdriver: 
   https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/

4. Update the path (within `app.py`) to the chrome driver executable:

```python
DRIVER_PATH = r'PATH_TO_CHROME_DRIVER'
```

## Running

```bash
python3 .\app.py
```