from module import add_score
import sys
from os import system
system("clear")


def run_all_tests():
    tests = [
        (({"Alice": 90}, "Bob", 85), {"Alice": 90, "Bob": 85}),
        (({}, "Alice", 100), {"Alice": 100}),
        (({"x": 1}, "y", 2), {"x": 1, "y": 2}),
    ]

    run_tests(tests, add_score)


def run_tests(tests, function):
    failure = False

    for i, (inputs, expected) in enumerate(tests):
        try:
            actual = function(*inputs)

            print(f"Inputs: {inputs}")
            print(f"Expected: {expected}, Got: {actual}")

            assert actual == expected
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