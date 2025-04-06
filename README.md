# Exploring Conditionals in Python: A Collection of solved Problem Sets
This repository contains a series of Python programs that utilize conditionals to solve a variety of problems. Each program demonstrates the effective use of **if**, **elif**, **else**, and other conditional logics such as **match-case** to tackle specific challenges.

## Problem Sets
### **1. Extensions.py** 
**Objective:** Determines the media type (MIME type) of a file based on its extension.

**Key Concepts:**

    Use of .rsplit() to handle file extensions.

    Conditional checks for supported extensions and fallback to default types.

**Example Output:**

***Input: cat.gif → Output: image/gif***

### **2. Bank.py** 
**Objective:** Simulates a scenario where a bank rewards customers based on specific greetings.

**Key Concepts:**

    startswith() method to check greeting prefixes.

    Handling inputs case-insensitively and ignoring leading/trailing spaces.

**Example Output:**

***Input: hey → Output: $20***

### **3. Meal.py**
**Objective:** Determines meal times based on the time of day.

**Key Concepts:**

    Converting input time strings into numerical values.

    Applying conditional logic to categorize times into breakfast, lunch, or dinner periods.

**Example Output:**

***Input: 12:30 → Output: Lunch Time***

### **4. Interpreter.py**
**Objective:** Implements a basic arithmetic interpreter that evaluates simple expressions.

**Key Concepts:**

    Splitting input strings to extract operands and operators.

    Applying conditional checks to execute the appropriate arithmetic operation.

**Example Output:**

***Input: 4 + 5 → Output: 9***

### **5. Deep.py**
**Objective:** Responds to philosophical questions about life, the universe, and everything.

**Key Concepts:**

    Handling case insensitivity and leading/trailing spaces.

    Matching specific valid responses using match-case or multiple conditional checks.

**Example Output:**

***Input: forty-two → Output: Yes***

Feel free to fork or clone this repository and contribute to these problem sets by adding more scenarios or enhancing the existing ones.