# slurm-notify-telegram

Send notification of jobs on slurm to telegram bot.

## Installation

For the python scripts, install [telebot](https://github.com/eternnoir/pyTelegramBotAPI).

## Deployment

* `bot_server.py` replies to `/hello` and `/getcid` messages by polling TG. Run it anywhere for convenience.
* `notification_server.py` receives notifications by http, and forward them to specific chat.
* `snotified.sh` is run by each user on the head node of slurm controller. It reads notifications of jobs via intra-node email sent by slurm, and send them to the notification server.

## Usage

See the help message in `bot_server.py`
