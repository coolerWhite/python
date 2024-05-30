text = """export STAGE=TEST
export TOKEN_ID=one"""
with open(".envrc","w") as opened_file:
    opened_file.write(text)