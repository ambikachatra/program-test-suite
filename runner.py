import os
import json
programs = os.listdir("programs")

print(programs)

for program in programs:
    file = open(f"programs/{program}/manifest.json", "r")
    content = file.read()
    file.close()
    print(content)
    program_object = json.loads(content)  
    entrypoint = program_object["entrypoint"]
    print(entrypoint)


full_path = f"programs/{program}/{entrypoint}"
print(full_path)

tests = content["tests"]
for test in tests:
    description = test['description']
    input_data = test['input']
    expected_output = test['output']
    print(f"Description: {description}")
    print(f"Input: {input_data}")
    print(f"Expected Output: {expected_output}")

    

