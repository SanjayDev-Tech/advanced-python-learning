def square(num):
    result = []
    for i in num:
        result.append(i*i)
    return result

my_num = square([1,2,3,4])   
print(my_num)     

📋 Expected Output: [1, 4, 9, 16]


#using Generator
def square(num):
    for i in num:
        yield (i*i)

my_num = square([1,2,3,4]) 


print(my_num)    #<generator object square at 0x7fc344b44fb0>
print(next((my_num)))  #1
print(next((my_num)))  #4
print(next((my_num)))  #9
print(next((my_num)))  #16


def square(num):
    for i in num:
        yield (i*i)

 my_num = square([1,2,3,4])

for j in my_num:
     print(j)

📋 Expected Output:  1
4
9
16

my_num = [x*x for x in [1,2,3,4]]  # using list comprehension
print(my_num)

📋 Expected Output: [1, 4, 9, 16]



import random
import time

"""
Advanced Python: Generators & Iterators Lab
Concepts Covered: Lazy Evaluation, Constant Space Complexity, Pipeline Architecture
"""

# LEVEL 1: Infinite Fibonacci Streamer
def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# LEVEL 2: Chunked Batch Loader
def batch_loader(dataset, batch_size):
    for i in range(0, len(dataset), batch_size):
        yield dataset[i : i + batch_size]

        

# LEVEL 3: Real-time Log Sensor & Filter


# 1. GENERATOR 1: Live Log Sensor Streamer
def log_sensor_stream():
    log_levels = ["INFO", "WARN", "ERROR", "INFO", "SUCCESS"]
    messages = ["User logged in", "Memory threshold 80%", "Database Connection Failed", "API request 200", "Payment complete"]
    
    while True:
     
        level = random.choice(log_levels)
        msg = random.choice(messages)
        yield f"[{level}] - {msg}"
        time.sleep(0.5)  #  For Real-time simulation 

# 2. GENERATOR 2: The Real-time Filter
def log_filter(raw_stream, target_level):
    for log_line in raw_stream:
   
        if target_level in log_line:
            yield log_line


   
    raw_logs = log_sensor_stream()
    error_alerts = log_filter(raw_logs, "ERROR")
    
  
    for alert in error_alerts:
        print(f"🔥 ALERT TRIGGERED: {alert}")