display notification "(Auto restart VPN every 8 hours)" with title "Restarting VPN" subtitle "Please wait for 1 minute for it to complete." sound name "Frog"

tell application "AnyConnect"
    quit
end tell
delay 3

activate application "AnyConnect"

delay 3
tell application "System Events"
    repeat 2 times
        key code 36 -- Press Enter
        delay 2
    end repeat

end tell
