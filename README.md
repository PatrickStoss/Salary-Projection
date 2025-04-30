# 🔥 FileWatcher with Excel-Based Filing Status

This Python-based file watcher monitors an Excel file for changes in the **Filing Status** cell (`C2`). When you update the cell to `"Single"` or `"Married"`, the program automatically adapts the behavior accordingly. The file watcher can run persistently in the background or be triggered manually.

---

## ✨ Features

- 📈 Monitors Excel cell `C2` for filing status updates.
- ♻️ Automatically adapts calculations or actions based on `"Single"` or `"Married"` values.
- 🕰️ Runs persistently in the background or manually through `main.py`.
- 🮠 Cross-platform support (Windows, macOS, Linux).

---

## 📦 Installation

1. **Clone the Repository:**

```bash
git clone https://github.com/yourusername/filewatcher.git
cd filewatcher
```

2. **Create a Virtual Environment (Optional but Recommended):**

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
.\venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

3. **Install Required Packages:**

Install the necessary packages using `pip`:

```bash
pip install watchdog openpyxl
```

- `watchdog` → Monitors file system changes.
- `openpyxl` → Reads and writes Excel files (`.xlsx`).

---

## ⚙️ Configuration

### 1. **Excel File Setup**

Ensure your Excel file has the following format:

| **A**         | **B**           | **C**         |
|---------------|-----------------|---------------|
| Filing Status | (Leave Blank)   | Single/Married|

- **Cell `C2`**: Set this cell to `"Single"` or `"Married"` to define your filing status.

Example:  
```text
C2 = Single
```

### 2. **Python Script Setup**

In `filewatcher.py`, set the path to the Excel file you want to monitor:

```python
excel_path = "/path/to/your/excelfile.xlsx"
```

---

## ▶️ Usage

### 1. **Run Manually (via `main.py`)

To manually start the watcher:

```bash
python main.py
```

- Updates will be reflected immediately when `C2` changes.
- The watcher will run until you stop it with `Ctrl + C`.

---

### 2. **Run as Background Process (Persistent Mode)**

#### 💻 **Linux/macOS (via `nohup` or `systemd`):**

- **With `nohup` (runs even after terminal closes):**

```bash
nohup python filewatcher.py &
```

- **With `systemd` (automatic startup):**

1. Create a service file:

```bash
sudo nano /etc/systemd/system/filewatcher.service
```

Add the following content:

```ini
[Unit]
Description=Persistent FileWatcher Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/filewatcher.py
Restart=always
User=yourusername

[Install]
WantedBy=multi-user.target
```

2. **Enable and Start Service:**

```bash
sudo systemctl enable filewatcher
sudo systemctl start filewatcher
```

3. **Check Status:**

```bash
sudo systemctl status filewatcher
```

---

#### 🦟 **Windows (via Task Scheduler):**

1. Open **Task Scheduler**.
2. Create a new task:
   - **Trigger:** "At startup" or "Daily."
   - **Action:** Run `python filewatcher.py`.
3. **Save and enable** the task.

