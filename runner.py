import os
import json
programs = os.listdir("programs")

print(programs)

for program in programs:
    file = open(f"programs/{program}/manifest.json", "r")
    content = file.read()
    file.close()

    program_object = json.loads(content)  
    entrypoint = program_object["entrypoint"]

    full_path = f"programs/{program}/{entrypoint}"
    print(full_path)
    

