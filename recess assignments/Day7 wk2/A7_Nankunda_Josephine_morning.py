# # Assignment A7:
# # 1a) Show a context manager for file handling that automatically opens and closes a file.
# # b) Shows a context manager for managing a database connection.
# # c) Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time.

#  1a) Show a context manager for file handling that automatically opens and closes a file.
class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

    def write_line(self, line):
        self.file.write(line + '\n')

# Example usage
filename = 'example.txt'

with FileHandler(filename, 'w') as file_handler:
    file_handler.write_line('Hello, world!')
# The file will be automatically closed when the `with` block ends
print("=========(a)open and close file")
print("File writing complete!")

# #Shows a context manager for managing a database connection.
# print("=============(b)Shows a context manager for managing a database connection=========================================")
import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.commit()
        self.connection.close()

# Example usage
db_name = 'example.db'

with DatabaseConnection(db_name) as cursor:
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

# The database connection will be automatically closed when the `with` block ends


# The database connection will be automatically closed when the `with` block ends

print("======(c)Multithreading and multiprocessing================================")
print("=========example of multithreading=======")

import threading
import time

def task(name, duration):
    print(f"Task '{name}' started.")
    time.sleep(duration)
    print(f"Task '{name}' completed.")

# Create multiple threads
threads = []
for i in range(1, 4):
    name = f"Task-{i}"
    duration = i
    thread = threading.Thread(target=task, args=(name, duration))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All tasks completed.")

print("======example of multiprocessing====")
import concurrent.futures
import time

def task(name, duration):
    print(f"Task '{name}' started.")
    time.sleep(duration)
    print(f"Task '{name}' completed.")

if __name__ == '__main__':
    # Create multiple processes
    processes = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for i in range(1, 4):
            name = f"Task-{i}"
            duration = i
            process = executor.submit(task, name, duration)
            processes.append(process)

        # Wait for all processes to complete
        for process in concurrent.futures.as_completed(processes):
            process.result()

    print("All tasks completed.")


print("=======Both multiprocessing and multithreading tasks")

import time
import concurrent.futures

def time_consuming_task(name, duration):
    print(f"Starting {name} for {duration} seconds...")
    time.sleep(duration)
    print(f"{name} finished!")

def run_with_threads():
    tasks = [
        ("Task 1", 2),
        ("Task 2", 3),
        ("Task 3", 4)
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []

        for task in tasks:
            name, duration = task
            future = executor.submit(time_consuming_task, name, duration)
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            result = future.result()

def run_with_processes():
    tasks = [
        ("Task 1", 2),
        ("Task 2", 3),
        ("Task 3", 4)
    ]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []

        for task in tasks:
            name, duration = task
            future = executor.submit(time_consuming_task, name, duration)
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Running with threads:")
    run_with_threads()

    print("\nRunning with processes:")
    run_with_processes()


