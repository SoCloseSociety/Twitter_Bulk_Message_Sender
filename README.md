# Twitter Direct Message Automation

This script automates sending direct messages to a list of Twitter profiles. It uses Selenium WebDriver for browser automation, BeautifulSoup for parsing HTML, and pandas for handling CSV data.

## Prerequisites

Ensure that you have the following installed:

- Python 3.6 or newer
- Selenium WebDriver
- BeautifulSoup4
- pandas

You will also need to have the Google Chrome browser installed, as well as the corresponding ChromeDriver, which must be added to your system's path.

## Usage

1. Give a .csv file  as input which  contains  twitter  profile links. You can get that link from our profile scrapper bot. 

2. Prepare a text file named `message.txt` containing the message you want to send. This message should be all on one line.

3. Run the script in your terminal:

    ```shell
    python main.py
    ```

4. You will be prompted to enter the filename of your CSV file. Enter the filename and press enter.

5. A browser window will open showing the Twitter login page. Manually log into Twitter.

6. After logging in, go back to your terminal and type `S` then press enter.

7. The script will now send your message to each of the Twitter profiles listed in your CSV file.

## Warning

This script may violate Twitter's Terms of Service. Do not use it to send spam or unsolicited messages. Always respect the privacy and time of others. This script is for educational purposes only and the author is not responsible for any misuse.
