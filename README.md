# Bing Search Automation

This project automates Bing searches using Selenium, providing a script for both desktop and mobile search simulations.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Description

The project utilizes the Selenium library to automate Bing searches for a list of randomly selected words. The script includes two search scenarios: desktop and mobile mode. It can be used for testing and experimenting with web automation techniques.

## Features

- Automated Bing searches with Selenium.
- Support for both desktop and mobile modes.
- Random selection of words for search.

## Getting Started

### Prerequisites

- Python installed on your machine.
- Required Python packages: `selenium` for web automation, `requests` for HTTP requests.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Ethan4thewin/BingSearchAutomation.git
   ```
2. Download Edge WebDriver and Firefox WebDriver:

   Download Edge web driver from https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver. Most of the time, the stable channel is the right choice.
   
   We may also want Firefox web driver Geckodriver for mobile browsing emulating. Link for downloading Mozilla Firefox geckodriver is https://github.com/mozilla/geckodriver/releases; choose the appropriate one for your computer architecture.
   
   In any case, put the file into the repository location.

4. Install dependencies:

   ```bash
   pip install selenium
   pip install requests
   ```

### Usage

Execute the desktop search script:

```bash
python search_pc.py
```
Execute the mobile search script:

```bash
python search_mobile.py
```
### Contributing & Troubleshooting
Contributions are welcome! Feel free to open issues or pull requests.

### License
This project is licensed under the MIT License.
