# TG monitor

Monitors a telegram channel for a specific word and notifies you using pushover. 

## Requirements

- Python3
- https://pushover.net account


## Setup instructions

### 1) Install python packages

pip3 install -r requirements.txt


### 2) Create folder and files

- mkdir /etc/tg-monitor
- copy config.ini --> /etc/tg-monitor/config.ini
- copy tg-monitor.py --> /usr/local/bin/tg-monitor
- chmod +x /usr/local/bin/tg-monitor

### 3) Create telegram API key

Follow this guide: 
https://core.telegram.org/api/obtaining_api_id

- You will get basic addresses as well as the **api_id** and **api_hash** parameters required for user authorization.


### 4) Update config.ini

The config file requires the following parameters:

- **api_id** = API id obtained from Telegram during step 2
- **api_hash** = API hash obtained from Telegram during step 2
- **tg_username** = A telegram username that has access to the channel you intend on monitoring.
- **user_input_channel** = The telegram channel you want to monitor. (Note: The tg_username must have access to this channel)
- **pushover_user_key** = Pushover user key for sending messages.
- **pushover_app_key** = Pushover app key for sending messages.



### 5) Running for the first time to save session details

Note that during the first run Telegram will request you to provide register mobile number and your telegram password to authenticate. After the initial run the session data is saved.

- Copy telegram session file telegramusername.session to /usr/local/bin/
- For example:

```
cp ankh2054.session /usr/local/bin/ 
```


### 6) Create and register as service. 

- mkdir -p /usr/lib/systemd/system 
- Add the contents below to file --> /usr/lib/systemd/system/tg-monitor.service

```
[Unit]
Description=tg-monitor
StartLimitIntervalSec=400
StartLimitBurst=3


[Service]
User=charles
ExecStart=/bin/bash -c "/usr/local/bin/tg-monitor > /dev/null  2>&1"
Restart=always
RestartSec=90

[Install]
WantedBy=multi-user.target
```

- Create and start service
```
sudo systemctl enable tg-monitor.service
sudo systemctl start tg-monitor 

```

### 6) Running for the first time

Note that during the first run you should 



### 7) Configuring high-priority alerts 

- The pushover app allows you to overide the **Do Not Disturb mode** on your phone. 
- Within the python script you can set which alerts are considered high-priority. 
- By default any missed blocks are set to high-priority
- This ensures that even when you slumper and have **Do Not Disturb mode** enabled you wil be alerted when your proucer misss blocks.

![IMG_62E0230DB425-1](https://user-images.githubusercontent.com/6784287/131241185-5a82e583-6ae0-4b47-a41a-d6feaf799062.jpeg)