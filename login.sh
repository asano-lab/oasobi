#!/bin/bash
read -rp 'ID: ' uid
read -rsp 'Password: ' pwd
curl -X POST -d uid=${uid} -d pwd=${pwd} https://login.shinshu-u.ac.jp/cgi-bin/Login.cgi
