# LeetCode Study Plan Solutions [![Python Unit Tests](https://github.com/daily-coding-problem/neetcode-150/actions/workflows/python-unittests.yml/badge.svg)](https://github.com/daily-coding-problem/neetcode-150/actions/workflows/python-unittests.yml) [![Format Check](https://github.com/daily-coding-problem/leetcode-study-plans/actions/workflows/format-check.yml/badge.svg)](https://github.com/daily-coding-problem/leetcode-study-plans/actions/workflows/format-check.yml)

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/-Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
![LeetCode](https://img.shields.io/badge/-LeetCode-FF4B00?style=flat-square&logo=leetcode&logoColor=white)

This is a repository that contains solutions to 📚 [LeetCode's Study Plans](https://leetcode.com/studyplan).

## Folder Structure

The repository is organized based on the study plans from LeetCode.

- <img src="https://github.com/user-attachments/assets/0b70acb4-2bd5-4fee-8cae-44c3b04a7052" width="25px"> [Binary Search](https://leetcode.com/studyplan/binary-search) is found in [Binary Search/](Binary%20Search)

## Prerequisites

- Python 3.9 or above should be installed.
- Some problems may require [LeetCode Premium](https://leetcode.com/subscribe).
- [Black](https://black.readthedocs.io/en/stable/) formatter should be installed to ensure consistent code formatting.

## Test

Clone the repository:

```bash
git clone https://github.com/daily-coding-problem/leetcode-study-plans
```

Change directories into the repository:

```bash
cd leetcode-study-plans
```

Execute tests:

```bash
python -m unittest discover -s . -p "*.py"
```

- `-s`: Specifies the start directory for discovery (`.` means the current directory)
- `-p`: Specifies the pattern of Python files to search for tests (in this case `*.py` meaning all `.py` files)

## _Why Python for Coding Interviews?_

Python is often recommended for coding interviews due to several compelling reasons:

-  **Readability**: Python is a high-level language known for its clear and concise syntax, making it easy to read and write. This can be especially helpful during interviews where you need to quickly convey your thought process.

-  **Simplicity**: With its straightforward syntax, Python allows you to focus on solving problems rather than getting bogged down by complex language rules. This simplicity can help you implement solutions more efficiently during an interview.

-  **Extensive Libraries**: Python boasts a vast ecosystem of libraries and frameworks, such as NumPy and pandas, which can be leveraged to solve complex problems more easily. This can be a significant advantage when tackling algorithmic challenges.

-  **Strong Community Support**: Python has a large and active community of developers. This means there are plenty of resources, tutorials, and forums available to help you learn and troubleshoot any issues you might face.

These attributes make Python a preferred choice for many candidates preparing for coding interviews.
To learn more about Python and its applications in coding interviews,
check out the _Python for Coding Interviews_ course on [NeetCode](https://neetcode.io/courses) where you will learn effective Python for coding interviews.

## 🗺️ Cheat Sheets?

For each study plan, a dedicated `CHEAT_SHEET.md` has been included to provide quick references and shortcuts for solving problems efficiently.
These cheat sheets summarize key concepts, common problem-solving patterns, and examples relevant to the respective study plan.

### Available Cheat Sheets

- [Binary Search Cheat Sheet](Binary%20Search/CHEAT_SHEET.md): Covers essential tips and tricks for mastering Binary Search problems, including examples and edge cases.
