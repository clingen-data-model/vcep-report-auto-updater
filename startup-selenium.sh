#!/bin/bash

# Start the Selenium server
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/Users/$(whoami)/selenium_profile"
