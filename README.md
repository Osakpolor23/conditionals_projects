# Exploring Conditionals in Python: A Collection of solved Problem Sets
This repository contains a series of Python programs that utilize conditionals to solve a variety of problems. Each program demonstrates the effective use of **if**, **elif**, **else**, and other conditional logics such as **match-case** to tackle specific challenges.

## Project Overview
### **1. Extensions.py** 
**Description:** This program determines the media type (MIME type) of a file based on its extension. It takes a file name as input, extracts the extension using string manipulation, and matches it against a predefined list of supported media types. If the extension is unsupported, the program defaults to returning application/octet-stream.

**Key Concepts:**

    Use of .rsplit() to handle file extensions.

    Conditional checks for supported extensions and fallback to default types.

**Sample Input:**

    cat.gif

**Expected Output:**

    image/gif

### **2. Bank.py** 
**Description:** A fun simulation program where the bank rewards customers based on specific greetings. The program evaluates the user's greeting (case-insensitively) and assigns a monetary reward depending on its content. Polite and kind greetings are rewarded the most, while other inputs yield smaller rewards.

**Key Concepts:**

    startswith() method to check greeting prefixes.

    Handling inputs case-insensitively and ignoring leading/trailing spaces.

**Sample Input:**

     hey 

**Expected Output:**

    $20

### **3. Meal.py**
**Description:** This program determines which meal (breakfast, lunch, or dinner) corresponds to a given time. Users input a time in a 24 hour format, which is parsed and checked against predefined meal periods.

**Key Concepts:**

    Converting input time strings into numerical values.

    Applying conditional logic to categorize times into breakfast, lunch, or dinner periods.

**Sample Input:**

    12:30

**Expected Output:**

    Lunch Time

### **4. Interpreter.py**
**Description:** A simple arithmetic interpreter that evaluates basic mathematical expressions involving addition, subtraction, multiplication or division. The program splits the input string into operands and operators and performs the corresponding computation with the result returned as a float.

**Key Concepts:**

    Splitting input strings to extract operands and operators.

    Applying conditional checks to execute the appropriate arithmetic operation.

**Sample Input:**

    4 + 5 

**Expected Output:

    9.0

### **5. Deep.py**
**Description:** This program is a playful take on answering a philosophical question about life, the universe, and everything. It checks if the user input matches specific phrases (case-insensitively) and returns an appropriate response.

**Key Concepts:**

    Handling case insensitivity and leading/trailing spaces.

    Matching specific valid responses using match-case or multiple conditional checks.

**Sample Input:**

    forty-two 

**Expected Output:**

    Yes

Feel free to fork or clone this repository and contribute to these problem sets by adding more scenarios or enhancing the existing ones.
