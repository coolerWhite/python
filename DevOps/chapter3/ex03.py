import subprocess

cp = subprocess.run(["ls", "-l"], capture_output=True, universal_newlines=True)
print(cp.stdout)