#!/bin/sh
# poll.sh <log> [sleep]: print only lines added since last poll of that log (cheap supervision of background jobs)
# usage: scripts/poll.sh /tmp/loop.log 50
L=${1:-/tmp/explore.log}; N=/tmp/poll.$(basename $L).n
sleep ${2:-50}
n=$(cat $N 2>/dev/null || echo 0); t=$(wc -l < $L)
[ "$t" -gt "$n" ] && sed -n "$((n+1)),${t}p" $L
echo $t > $N
pgrep -f "explore.py|sm.py loop|sm.py mine|stackmine.py" >/dev/null && echo "[running]" || echo "[stopped]"
