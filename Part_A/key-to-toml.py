import toml

output_file = ".streamlit/secrets.toml"

with open("Part_A\\firestore-key.json") as json_file:
    json_text = json_file.read()

config = {"textkey1": json_text}
toml_config = toml.dumps(config)

with open(output_file, "w") as target:
    target.write(toml_config)