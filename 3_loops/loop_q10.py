import time
wait_time = 1
max_retries = 15
attempts = 0

while attempts < max_retries:
    print(f"Attempt: {attempts+1} -> Wait Time {wait_time}")
    attempts += 1
    time.sleep(wait_time)
    wait_time = wait_time*2
