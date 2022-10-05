import animu

TOKEN = "ANIMU API TOKEN HERE"
client = animu.Client(TOKEN)
roleplay = client.roleplay(animu.Roleplay.angry)
print(roleplay)