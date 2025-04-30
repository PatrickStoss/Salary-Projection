import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Path to the Excel file and main script
file_to_watch = "paychecks.xlsx"
python_path = "C:/Users/Saint/AppData/Local/Programs/Python/Python313/python.exe"
main_script = "main.py"

class ExcelFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(file_to_watch):
            print(f"{file_to_watch} was modified. Running projections...")
            os.system(f'"{python_path}" {main_script}')

if __name__ == "__main__":
    path = "."  # Watch the current directory
    event_handler = ExcelFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=False)
    
    print(f"Watching for changes in '{file_to_watch}'... Press Ctrl+C to exit.")
    try:
        observer.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Monitoring stopped.")
        observer.stop()

    observer.join()

