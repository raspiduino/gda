# GDA - Google Drive download using aria2c
Download large file in Google Drive with aria2 at max speed 

## Why do this?
With small file, you can easily download it by ```aria2c -x16 -s16 -j5 "https://drive.google.com/uc?id=YOURFILEID&export=download"```. But you can't do that with large file because Google will show a warning about virus scan. So I want to make this for downloading the large file from Google Drive automaticly without confirm that warning.

## How this work?
This work the same as <a href="https://gist.github.com/iamtekeste/3cdfd0366ebfd2c0d805#gistcomment-2316906">this</a> wget method: Get the auth cookies from Google Drive, pass it to aria2c (see <a href="https://github.com/aria2/aria2/issues/545">this</a>).

## Usage
```gda.py fileid```
<br>fileid: Insert your fileid
<br>For example: if your link is https://drive.google.com/file/d/1nVOL_4NMw8hfszfYYo2bwUSgFtQtulAT/view
<br>```gda.py 1nVOL_4NMw8hfszfYYo2bwUSgFtQtulAT```

## Requirement
- Python3
- <i>requests</i> library: ```pip/pip3 install requests``` 
- <a href="https://github.com/aria2/aria2">aria2</a>

## Todo
- Add folder download support

## Credits
Special thanks to aria2, requests and other libs.
