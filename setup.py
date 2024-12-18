from setuptools import setup

def run_malicious_code():
    # Simulate malicious activity
    print("This is malicious code executing...")
    with open("malicious_log.txt", "w") as f:
        f.write("Malicious code executed successfully!\n")

run_malicious_code()

setup(
    name="malicious-library",
    version="1.0.0",
    description="A malicious Python package",
    py_modules=["malicious_library"],
)