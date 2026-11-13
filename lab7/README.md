
# Lab 7 - Fuzz Testing

## Project: Traffic Fine Calculator

### 1. Aim

To perform fuzz testing on a Traffic Fine Calculator using Python, Pytest, and Hypothesis to identify unexpected errors and improve input validation.

### 2. Tools Used

- Python 3.11.9
- Pytest
- Hypothesis
- Visual Studio Code

### 3. Project Description

The application contains three functions:

1. `parse_ticket_id()` - Parses a ticket ID into prefix, year, and serial number.
2. `total_fines()` - Calculates the total of multiple traffic fines, with a maximum limit of 10,000.
3. `speed_excess()` - Calculates the percentage by which vehicle speed exceeds the speed limit.

### 4. Fuzz Testing

Hypothesis generates different input values, including arbitrary strings and None, to identify unexpected failures.

### 5. Bugs Identified

Fuzz testing identified errors involving:

- Invalid and empty ticket IDs.
- Empty or None fine inputs.
- Invalid speed readings and None values.

The original implementation produced 3 failed tests.

### 6. Bug Fixes

Input validation and exception handling were added to all three functions. Invalid inputs now return safe default values instead of causing unhandled exceptions.

### 7. Test Execution

Run the following command:

```bash
python -m pytest -v test_traffic_fine.py
```

### 8. Final Result

All three fuzz tests passed after correcting the application.

- `test_parse_ticket_id_no_crash` - PASSED
- `test_total_fines_no_crash` - PASSED
- `test_speed_excess_no_crash` - PASSED

### 9. Screenshots

The following screenshots demonstrate the original execution, discovered failures, corrected execution, and successful fuzz testing:

- `lab7_original_output.png`
- `lab7_fuzz_failures.png`
- `lab7_fixed_output.png`
- `lab7_fuzz_passed.png`

### 10. Conclusion

Fuzz testing using Hypothesis helped identify unexpected input-handling errors. After implementing input validation, all three automated tests passed successfully.
