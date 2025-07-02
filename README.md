# Race Bias Simulator
## Background
This simulator intends to use artificial manipulation to illustrate how AI and algorithms can disproportionately harm minority popultations, especially within the banking and financial sectors.

## Directions for use

### **1. Install Git and Python (if not already installed)**

#### 🔧 Git:

* **Mac**:
  Open Terminal and type:

  ```bash
  git --version
  ```

  If Git isn’t installed, you’ll be prompted to install it.

#### 🐍 Python:

* **Mac**:
  Check version:

  ```bash
  python3 --version
  ```

  If not installed, install [Python from python.org](https://www.python.org/downloads/).

---

### **2. Clone the GitHub Repository**

Go to your GitHub repo and copy the **HTTPS URL** (e.g., `https://github.com/yourusername/race-bias-simulator.git`)

Then in Terminal:

```bash
cd ~/Documents  # or wherever you want the project
git clone https://github.com/yourusername/race-bias-simulator.git
cd race-bias-simulator
```

---

### **3. Create and Activate a Virtual Environment**

```bash
python3 -m venv venv         # Create the virtual environment
source venv/bin/activate     # Activate it (use venv\Scripts\activate on Windows)
```

You should see `(venv)` at the start of your terminal line now.

---

### **4. Install Required Packages**

Make sure there's a `requirements.txt` file in your repo. If not, you can create it manually:

```txt
pandas
numpy
matplotlib
seaborn
```

Then run:

```bash
pip install -r requirements.txt
```

---

### **5. Run the Python File**

Assuming your main file is called `main.py` (or similar):

```bash
python main.py
```

If you saved the code in a file like `risk_simulation.py`, use:

```bash
python risk_simulation.py
```

You should see a bar graph pop up displaying the AI risk score comparison.

---

### ✅ Optional: Create `main.py` (if not already created)

If your code is not yet in a Python file, create one:

```bash
touch main.py
nano main.py
```

Paste your code in, save (`Ctrl+X`, then `Y`, then `Enter`).

---

### ✅ Optional: Generate requirements.txt Automatically

If you installed packages manually, run:

```bash
pip freeze > requirements.txt
```

This captures all installed packages and versions.