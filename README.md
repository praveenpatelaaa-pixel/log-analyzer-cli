# Log Analyzer CLI

## Project Title & Goal
This project is a command-line Python tool that analyzes server log files and extracts error-related information.

## Setup Instructions
1. Make sure Python is installed.
2. Open terminal in the project folder.
3. Run the command:
   python log_analyzer.py server.log

## Logic (How I Thought)
I used file handling to read the log file line by line and regular expressions to detect error messages.
Regex helps in identifying patterns like ERROR or specific error codes.
The hardest issue was handling missing files, which I fixed by adding file existence checks.

## Output Screenshots
(Attach screenshots showing the program output here)

## Future Improvements
- Add support for different log formats
- Generate summary reports
- Add date-wise error filtering

## Future Improvements
If I had 2 more days, I would improve error handling and add basic unit tests to make the application more reliable. I would also refactor the code to improve readability and maintainability.
✔ Simple
✔ Realistic
✔ Professional
✔ Exactly what interviewers expect from a fresher
