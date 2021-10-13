### Disclaimer
**This code is provided for educational purposes only and is not to be used for any purpose that would infringe on the policies or terms of service of any party.**

------------------------

# JukeBot

**http://squigjess.github.io/JukeBot/**

A self-hosted audio streaming bot for Discord. Currently supports YouTube, with plans to support other services and local file streaming eventually.

While it currently works, JukeBot is still under development. A lot of the bugs are still being found and worked on. As a result, the current version you see here in the `live` branch is technically a testing version that happens to be deployed to a few private Discord servers for testing purposes.

If you would like to run JukeBot and report on your bugs and issues, I would be forever grateful.

# Installation

## 1. Install Python dependencies
    python3 -m venv venv
    source venv/bin/activate   # For macOS/Linux
    venv/Scripts/activate.bat  # For Windows
    pip install -r requirements.txt

## 2. Set up `config.py`
Rename `config.EXAMPLES.py` to `config.py` and update the FFmpeg path and your Discord bot's token.

## 3. Install FFmpeg
* Download the FFmpeg binaries for your system from [the official ffmpeg.org website](https://ffmpeg.org/download.html)
* Place them somewhere accessible on your machine.
* Update `FFMPEG_PATH` in `config.py`.

## 4. Set up a Discord application and bot
I'm not gonna go into too much detail on this, but create a bot, add it to your server, then put the bot's token in `DISCORD_BOT_TOKEN` in `config.py`.

# To do
* Features
  * Add `!play` and `!pause` commands
* Track/queue data refactor
  * Include who queued up a track in song data
  * Class-ify song/queue objects to store now-playing data in them
* Behind the scenes stuff
  * Have JukeBot auto-disconnect (maybe after a delay?) when the queue is exhausted.
  * [Move to discord.py's inherent checks system](https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html?highlight=on_command_error#checks)
  * [Implement proper error handling](https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html?highlight=on_command_error#error-handling)
  * https://pyinstaller.readthedocs.io/en/stable/operating-mode.html#hiding-the-source-code
  * https://pyinstaller.readthedocs.io/en/stable/usage.html#cmdoption-i
* Documentation
  * Update README and Quickstart once build process is sorted out
* Maybes
  * Implement Spotify link recognition and translation (not sure if this is possible with a self-hosted set-up)
<!-- * ~~Find out why compiled version doesn't launch a terminal window on Linux.~~
~~* Implement the ability to remove a single track from the queue in !clear~~
* ~~Make "queued" msg titles link to the OG video~~
* ~~Logfile~~
* ~~Update docstrings~~
* ~~work on build script~~
* ~~Move config to .json in anticipation of exe distribution~~
* ~~Add a way to clear the queue.~~
* ~~Function-ify redundant embed/dialog code in `!play`.~~
* ~~Work on a nicer-looking `!help` command.~~
* ~~Add a pretty `!queue` command.~~
* ~~Set up GitHub Pages website for JukeBot.~~
* ~~Re-implement `!skip`.~~
* ~~PySimpleGUI~~ -->
