#!/bin/bash

# Task 1: Log Running Processes

LOG_DATE=$(date +"%Y-%m-%d")
PROCESS_LOG="process_log_${LOG_DATE}.log"

ps -eo pid,ppid,user,%mem,%cpu,comm --sort=-%mem > "$PROCESS_LOG"
echo "Running processes logged in $PROCESS_LOG"


# Task 2: Check for High Memory Usage (>30%)

HIGH_MEM_LOG="high_mem_processes.log"

# Get processes with >30% memory usage
high_mem_processes=$(ps -eo pid,ppid,user,%mem,%cpu,comm --sort=-%mem | awk '$4 > 30')

if [ ! -z "$high_mem_processes" ]; then
    echo "WARNING: Processes using more than 30% memory detected!"
    echo "$high_mem_processes" >> "$HIGH_MEM_LOG"
fi


# Task 3: Check Disk Space on Root Partition

disk_usage=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')

if [ "$disk_usage" -gt 80 ]; then
    echo "WARNING: Disk usage on / is above 80% (Current: ${disk_usage}%)"
fi


# Task 4: Display Summary

total_processes=$(ps -e --no-headers | wc -l)
high_mem_count=$(echo "$high_mem_processes" | wc -l)

echo "-------------------------"
echo "System Health Summary:"
echo "Total running processes: $total_processes"
echo "Processes using >30% memory: $high_mem_count"
echo "Disk usage on /: ${disk_usage}%"
echo "-------------------------"
