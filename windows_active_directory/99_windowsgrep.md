## Windows Grep / Grepping with Windows

### CMD
```
FINDSTR /i /r /c:"hello.*goodbye" /c:"goodbye.*hello" Demo.txt
FINDSTR -i -r -c:"hello.*goodbye" /c:"goodbye.*hello" Demo.txt
FINDSTR /irc:"hello.*goodbye" /c:"goodbye.*hello" Demo.txt
FINDSTR /ic:"hello" Demo.txt | findstr /ic:"goodbye"
FINDSTR "granny Smith" Apples.txt Pears.txt
FINDSTR /C:"granny Smith" Contacts.txt
```
Search every file in the current folder and all subfolders for the word "Smith", regardless of upper/lower case, note that /S will only search below the current directory:
```
FINDSTR /s /i smith *.*
```