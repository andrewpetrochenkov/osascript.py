[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/osascript.svg?longCache=True)](https://pypi.org/pypi/osascript/)
[![](https://img.shields.io/pypi/v/osascript.svg?maxAge=3600)](https://pypi.org/pypi/osascript/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/osascript.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/osascript.py/)

#### Install
```bash
$ [sudo] pip install osascript
```

#### Functions
function|description
-|-
`osascript.osascript(applescript, background=False)`|run applescript file/code. deprecated
`osascript.run(applescript, background=False)`|run applescript file/code

#### Examples
```python
>>> import osascript

>>> code,out,err = osascript.run('display dialog "42"')
```

#### Links
+   [osascript(1) Mac OS X Manual Page](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/osascript.1.html)

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>