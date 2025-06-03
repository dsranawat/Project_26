import time

def stopwatch():
    input("Press Enter to start the stopwatch...")
    start_time = time.time()
    input("Stopwatch started! Press Enter to stop.")
    end = time.time()
    elapsed = end - start_time
    print(f"Elapsed time: {elapsed:.2f} seconds")

if __name__ == "__main__":
    print("...Stopwatch...")
    stopwatch()
    