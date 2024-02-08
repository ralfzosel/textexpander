Converts appointments from Calendar (macOS) to simple text format (German).

Installation:
-------------
Its ment to be used with Textexpander. You can simply import the `import.csv` on https://app.textexpander.com/settings/import . You still have to switch content type "Shell Script".

*Alternatively*, you can create a new text snippet in TextExpander with content type "Shell Script" and paste the content of `calendar_to_text.py`. Replace the value of the variable `input_schedule` (within the tripple quotation marks) with the `Clipboard` in Textexpander and add as first line of code (beferee the "from datetime …"-line) the following line:

#!python3

Usage:
------
On Calender, mark the desired appointments and copy them to clipboard. Go to where you want to insert the appointments and trigger the Textexpander snippet.

A text formatted like this example will be inserted:

    Mittwoch, 14.02.24, 10:45 Uhr
    Donnerstag, 15.02.24, 15:00 Uhr
    Donnerstag, 15.02.24, 17:00 Uhr

It's tested with macOS 13.6.4.