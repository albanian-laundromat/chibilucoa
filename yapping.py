import random

ngramnumber = 5

def process(text):
    if len(text) < ngramnumber - 1:
        return
    text = "B" + text.lower() + "E"
    
    f = open(f"yapping{ngramnumber}.txt", "r", encoding = "utf-8")
    content = f.read()
    f.close()

    if len(content) > 100000:
        return

    for i in range(ngramnumber - 1, len(text)):
        if len(content) != 0:
            content += "S"
        content += text[i - ngramnumber + 1:i + 1]

    f = open(f"yapping{ngramnumber}.txt", "w", encoding = "utf-8")
    f.write(content)
    f.close()
    

def generate():
    
    f = open(f"yapping{ngramnumber}.txt", "r", encoding = "utf-8")
    content = f.read()
    f.close()

    triplets = content.split("S")

    
    reply = random.choice([i for i in triplets if i[0] == "B"])

    triplets.remove(reply)
    
    while True:
        if reply[-1] == "E":
            reply = reply[:-1]
            break
        current = reply[1 - ngramnumber:]
        candidates = [i[-1] for i in triplets if i[:-1] == current]
        if candidates == []:
            break
        chosen = random.choice(candidates)
        triplets.remove(current + chosen)
        if chosen == "E":
            break
        reply += chosen

    f = open(f"yapping{ngramnumber}.txt", "w", encoding = "utf-8")
    f.write("S".join(triplets))
    f.close()
    return reply[1:] + " :3"
