# NetworkCheckerBot

NetworkCheckerBot is a Python bot that collects ping data from your Minecraft server and stores it in a MySQL database. This bot is used to monitor the performance of your Minecraft server and analyze network latency.

## Features

- **Ping Data Collection**: Collects ping data from your Minecraft server.
- **MySQL Database Integration**: Stores ping data in a MySQL database.
- **Configuration File**: Easily configure IP address, port, and database information.
- **Logging**: Logs bot activities and errors to `bot.log`.
- **Asynchronous Operation**: Provides high efficiency using asynchronous programming.

## Requirements

- Python 3.8+
- `mysql-connector-python` library
- `asyncio` and other necessary libraries

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/username/NetworkCheckerBot.git
    cd NetworkCheckerBot
    ```

2. **Install Requirements**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Edit the Config File**:
    ```python
    class Config:
        SERVER_HOST = 'host_name'
        SERVER_PORT = 25567
        DB_HOST = 'your_ip'
        DB_USER = 'your_username'
        DB_PASS = 'your_password'
        DB_NAME = 'database_name'
    ```

4. **Log File and Other Settings**:
    ```bash
    Check the log file name and log rotation settings in `utils/logger.py`.
    ```

## Usage

1. **Start the Bot**:
    ```bash
    python main.py
    ```

2. **Verify the Bot is Running**:
    ```bash
    1. Check the `bot.log` file to confirm that the bot has started and is collecting ping data.
    ```

