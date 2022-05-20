# **tureng_terminal**
helper for finding the meaning of the word from terminal rather than browser. code takes argument from commandline 

***Requirements:***
BeautifulSoup and requests module of Python.


***Note:*** User can make ailas command for easy usage.

Example:

location of the repo: ~/testboard/generaleverything/turengterm/

in /.bashrc file : alias turengword='_(){ python3 ~/testboard/generaleverything/turengterm/tureng.py ${*:1}; }; _'


To make it permanent: source /.bashrc

