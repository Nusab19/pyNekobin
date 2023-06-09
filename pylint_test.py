import subprocess

def test_linter():
    # I like to do things in one line :333
    result = float(subprocess.run(["pylint", "nekobin/*.py"], capture_output=True).stdout.decode('utf-8').strip().split('\n')[-1].split()[6].split('/')[0])

    assert result >= 7, f"Your code is rated {result}/10.0"

test_linter()