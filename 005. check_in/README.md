# check in with Python

一个签到小脚本。通过 requests 发送带 cookies 请求，来模拟用户登陆网站。

## 功能

- 在 steamcn，readfree 每天定时登陆

## 定时设置

定时采用 ubuntu 自带 crontab来实现每天定时启动

```bash
00 06 * * * /bin/bash ~/scripts/checkin/checkin.sh >> ~/scripts/checkin/checkin_log.txt 2>&1 &
```

每天6点登陆网站，并将报错情况输出到checkin_log.txt文件

## 依赖

- requests