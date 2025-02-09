# AI (ChatGPT) generated code to provide test framework for automated execution of test cases.
# Solutions are coded by live, warm-blooded human. Only used AI to generate test framework only!

import unittest
import io
import sys

test_failed = False  # Global variable to track if any test fails

def run_tests(solution_class, method_name, test_cases):
    """
    Runs test cases using unittest for a given method in a Solution class.
    
    Prints each test case's input, output, expected result, and whether it passed or failed.
    
    :param solution_class: The class containing the method to test.
    :param method_name: The method inside the class to test.
    :param test_cases: A list of dictionaries with 'input' and 'expected' keys.
    """

    class DynamicTestCase(unittest.TestCase):
        
        def test_cases(self):
            global test_failed
            solution_instance = solution_class()  # Instantiate Solution class
            method_to_test = getattr(solution_instance, method_name)  # Get method
            
            for case in test_cases:
                input_values = case["input"]
                expected_output = case["expected"]
                
                try:
                    actual_output = method_to_test(*input_values)
                    passed = actual_output == expected_output
                    
                    # Print detailed results
                    print("\n-------------------------")
                    print(f"Input: {input_values}")
                    print(f"Output: {actual_output}")
                    print(f"Expected: {expected_output}")
                    
                    if passed:
                        print("Good job, test case passed!")
                    else:
                        # Mark test as failed
                        test_failed = True
                        print("X Failed")
                        print(f"X Difference: Expected {expected_output}, but got {actual_output}")

                except Exception as e:
                    test_failed = True
                    print("\n-------------------------")
                    print(f"Input: {input_values}")
                    print(f"X Exception: {e}")

    # Capture and suppress unittest's summary output
    output_capture = io.StringIO()
    sys.stdout = output_capture

    suite = unittest.TestLoader().loadTestsFromTestCase(DynamicTestCase)
    unittest.TextTestRunner(verbosity=1).run(suite)

    sys.stdout = sys.__stdout__  # Restore normal stdout

    # Remove last few lines that contain unittest summary
    output_lines = output_capture.getvalue().split("\n") # Get each output print statement from tests
    filtered_output = "\n".join(output_lines)  # Format test results

    print(filtered_output)  # Print output statements from test execution

    # Print success message only if all tests passed
    if not test_failed:
        print("\nGreat Job! All tests passed!")
    else:
        print("\nFailed tests detected. Don't be discouraged, try again!")