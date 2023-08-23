# xGrep: Filename and Content Change Stager

`xGrep` is a utility tool that recursively searches through directories, identifying filenames and content that match a specific pattern. It was designed specifically for the use case of updating references from "twitter" to "x", but it's versatile enough for other pattern replacements.

## Summary

xGrep allows you to navigate through your project and pinpoint specific instances where changes are required, both in filenames and their content. It's perfect for large-scale refactoring or updates where manual checks can become cumbersome.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/DJStompZone/xGrep.git
   cd xGrep
   ```

2. Install Dependencies:
Ensure you have pip installed. Then:
   ```bash
   pip install -r requirements.txt
   ```

# Usage
Navigate to the directory of interest and run the xGrep script:
   ```bash
   python3 xgrep.py
   ```
After execution, a detected_changes.json file will be generated, detailing the suggested changes.

License
Released under the MIT License. See LICENSE for more information.

# Author
DJ @ DeepAI
