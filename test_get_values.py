from module import get_values
import sys
from os import system
system("clear")


def run_all_tests():
    tests = [
        (({"a": 1, "b": 2},), [1, 2]),
        (({"name": "Alice", "age": 16},), ["Alice", 16]),
        (({},), []),
        (({"x": 10},), [10]),
    ]

    run_tests(tests, get_values)


def run_tests(tests, function):
    failure = False

    for i, (inputs, expected) in enumerate(tests):
        try:
            actual = function(*inputs)

            print(f"Inputs: {inputs}")
            print(f"Expected: {expected}, Got: {actual}")

            # Compare as sets to avoid order issues
            assert set(actual) == set(expected)

            print(f"Test {i}: Pass!\n")

        except AssertionError:
            print(f"Test {i}: Fail\n")
            failure = True

        except Exception as e:
            print(f"Test {i}: Error → {type(e).__name__}: {e}\n")
            failure = True

    print("❌ Some tests failed." if failure else "✅ All tests passed!")


if __name__ == "__main__":
    run_all_tests()
    sys.exit(0)