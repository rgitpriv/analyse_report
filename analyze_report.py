#!/usr/bin/env python3
import pyautogui as ag
import random
import time
import signal

# Keeps your status active on slack/teams. Use an empty channel or
# message to yourself. Start script, then within 30 seconds focus your
# desired slack/teams chat window.

# Tested on arch linux & windows 11

MAX_IDLE = 120  # pause between 0 and this value, in seconds
START_DELAY = 30  # pause before starting output

def sigIntHandler(signun, frame):
    exit(0)

# capture control+c
signal.signal(signal.SIGINT, sigIntHandler)

print(f'Focus chat window target, you have {START_DELAY} seconds')
time.sleep(START_DELAY)
print('Scanning archives..')

if __name__ == "__main__":
    while True:
        ag.keyDown('shift')
        report = random.randint(0, MAX_IDLE)
        print(f'Found {report} records - processing...')
        ag.keyUp('shift')
        time.sleep(report)
