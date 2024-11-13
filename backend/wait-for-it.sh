#!/usr/bin/env bash
# wait-for-it.sh v2.5.0

# Use this script to wait until a specified TCP host and port are available.
# Example usage:
#   ./wait-for-it.sh db:5432 -- echo "Database is up"

TIMEOUT=15
QUIET=0
HOST=""
PORT=""
CMD=""

usage()
{
  echo "Usage: $0 host:port [-t timeout] [-q] -- command"
  echo ""
  echo "  -t  Timeout in seconds (default is 15)"
  echo "  -q  Quiet mode (no output)"
  echo "  host:port  The host:port to wait for"
  echo "  command    The command to run after the wait is complete"
}

# Parse command line arguments
while getopts "t:q" opt; do
  case "$opt" in
    t)
      TIMEOUT="$OPTARG"
      ;;
    q)
      QUIET=1
      ;;
    *)
      usage
      exit 1
      ;;
  esac
done
shift $((OPTIND-1))

if [ "$#" -lt 1 ]; then
  usage
  exit 1
fi

HOSTPORT=$1
CMD="${@:2}"

HOST=$(echo "$HOSTPORT" | cut -d: -f1)
PORT=$(echo "$HOSTPORT" | cut -d: -f2)

# Wait for the host:port to be available
for i in $(seq 1 $TIMEOUT); do
  nc -z "$HOST" "$PORT" > /dev/null 2>&1
  if [ $? -eq 0 ]; then
    if [ $QUIET -eq 0 ]; then
      echo "$HOSTPORT is available"
    fi
    exec $CMD
    exit 0
  fi
  sleep 1
done

echo "Timeout reached while waiting for $HOSTPORT"
exit 1
