import toml

output_file = ".streamlit/secrets.toml"

with open("Part_C\Resources\sy_comp_student_data.json") as json_file:
    json_text_1 = json_file.read()

with open("Part_C\Firebase_key.json") as json_file:
    json_text_2=json_file.read()

config = {"textkey2": json_text_1,"textkey3":json_text_2}
toml_config = toml.dumps(config)

with open(output_file, "a") as target:
    target.write(toml_config)