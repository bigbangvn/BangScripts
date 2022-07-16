
tell application "Safari"
    quit
end tell
delay 3

activate application "Safari"

delay 3
tell application "System Events"
    keystroke "t" using {command down} -- Create a New tab
    delay 2
    keystroke "langnet.co"
    key code 36 -- Press Enter
    delay 2
    repeat 2 times
        keystroke "r" using {command down} -- Refresh
        delay 2
    end repeat

end tell
