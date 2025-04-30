import subprocess

# Full path to your Python executable
python_path = r"C:/Users/Saint/AppData/Local/Programs/Python/Python313/python.exe"

def run_script(script_name):
    try:
        subprocess.Popen([python_path, script_name], shell=True)
    except Exception as e:
        print(f"Failed to run {script_name}: {e}")

print("Running salary projections...")
run_script("salary.py")

print("\nGenerating visualizations...")
run_script("visualizations.py")

print("\nAll tasks initiated. Visualization windows are running.")
