#! /usr/bin/env python3

htmlText = """Content-type: text/html; charset=UTF-8
<html>
<head>
  <title>現在時刻を表示する</title>
</head>
<body>
<h1>現在時刻</h1>
<p>%s</p>
</body>
</html>
"""

import time
now = time.strftime("%Y年%m月%d日 %H時%M分%S秒")
print(htmlText % now)