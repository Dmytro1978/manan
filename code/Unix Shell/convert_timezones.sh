#!/bin/bash
#set -vx
dt_utc=$(TZ="UTC" date +'%Y-%m-%d %H:%M:%S %Z')
echo $dt_utc
dt_pst=$(TZ="US/Pacific" date -d "${dt_utc}" +'%Y-%m-%d %H:%M:%S %Z')
echo $dt_pst
dt_pst_new=$(TZ="US/Pacific" date +'%Y-%m-%d %H:%M:%S %Z' -d "$dt_pst+1 hour")
echo $dt_pst_new
dt_utc_new=$(TZ="UTC" date -d "${dt_pst_new}" +'%Y-%m-%d %H:%M:%S %Z')
echo $dt_utc_new