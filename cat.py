import subprocess

tokenized_string = "hello"
output = subprocess.check_output(
    ["sed", "s/foo/bar/"],
    input=tokenized_string.encode()
)
print(output.decode())




