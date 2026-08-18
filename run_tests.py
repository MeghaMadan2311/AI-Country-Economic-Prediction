import subprocess
import sys


def run_tests():
    result = subprocess.run(
        [sys.executable, "-m", "pytest"],
        capture_output=False
    )

    return result.returncode


if __name__ == "__main__":
    exit_code = run_tests()

    if exit_code == 0:
        print("All tests passed!")
    else:
        print("Some tests failed.")

    sys.exit(exit_code)
