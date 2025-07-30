# strome-f0-control

Control a Ströme AC unit with Flipper Zero

Connect your Flipper via serial-usb and adjust the serial port as needed via
the "--port" switch. It defaults to /dev/ttyACM0.

Tested functional on Flipper Zero firmware 1.3.4. Earlier firmware (at least
1.0.1) had issues with sample sizes >150 like these, and CLI support for
those still seem to have issues. Sending pre-saved IR payloads does not
seem to be possible via CLI yet, even though it is via the GUI.



