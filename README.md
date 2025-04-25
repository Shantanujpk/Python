Python Modules and Package Management
This project demonstrates the basic concepts of Python modules, their types, and how to manage external packages using pip.

📚 About Modules
Modules allow us to use existing code written by others, saving time and effort when developing new programs.

There are two types of modules:
Internal Modules (Built-In):   These are provided by Python itself.
Example: hashlib
No installation is needed.

External Modules:  Code written by external developers, made available for use.
Must be installed separately using pip.
Example: pandas, sklearn, tensorflow

🔧 Using pip (Package Installer for Python)
pip is the default package manager for Python.

It fetches and installs external libraries from the internet.

Always use pip install <package-name> in the terminal (not inside the Python interpreter).
Example:
bash
pip install pandas
pip install tensorflow
Note:
If you are using VS Code, open the integrated terminal (Ctrl + ~) to run pip install commands.
Do not run them inside the Python shell (>>>) or it will throw an error.

🗂 Where Are Installed Packages Stored?
On Windows (default installation location):

C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python<version>\Lib\site-packages
On Mac/Linux:
/usr/local/lib/python<version>/site-packages
You can check your installed packages inside these directories.

🧪 Sample Python Code
python

import pandas       # External module (needs pip install)
import sklearn      # External module (needs pip install)
import hashlib      # Internal (built-in) module
import tensorflow   # External module (needs pip install)

print("Checking the installations")


✅ Quick Summary
Internal Module/Package    No pip
Extenal Module/ Package    Use pip
