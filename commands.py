import rankings
from urllib.request import urlretrieve

validcommands = [
    "ping",
    "countrycodes",
    "commands",
    "languagecodes",
    "info",
    "lyrics",
    "ranking",
    "global",
    "rankingmethods",
    "suggest",
    "countrylog",
    "winners",
    "process"
    ]

f = open("contests.txt", "r")
contests = f.read().split("\n")
f.close()

def findindex(itera, item):
    try:
        return itera.index(item)
    except:
        return -1

def ping(message, author):
    return ("pong", "hiiiiiii :3")


def ccodes(message, author):
    f = open("ccodes.txt", "r", encoding="utf-8")
    thing = f.read()
    f.close()
    thing = thing.split("\n")
    thing.sort()
    thing = [i.split("|") for i in thing]
    thing = ["`"+i[0]+"` "+i[1] for i in thing]
    return ("all valid country codes", "\n".join(thing))

def lcodes(message, author):
    f = open("lcodes.txt", "r", encoding="utf-8")
    thing = f.read()
    f.close()
    thing = thing.split("\n")
    thing.sort()
    thing = [i.split("|") for i in thing]
    thing = ["`"+i[0]+"` "+i[1] for i in thing]
    return ("all valid language codes", "\n".join(thing))


def commandslist(message, author):
    return ("All currently supported commands: ","\n".join(sorted(validcommands)))

def entryinfo(message, author):
    plus = False
    if len(message) < 3:
        return ("an error occurred", ":pregnant_man: idk what to do here")
    contest = message[1]
    if contest not in contests:
        return ("an error occurred", "that's not a supported contest")
    if contest[-1] == "+":
        contest = contest[:-1]
        plus = True
    try:
        f = open(f"contest_{contest}/entry_{message[2]}/index.txt", encoding="utf-8")
    except:
        if plus:
            try:
                f = open(f"contest_{contest}/plus/entry_{message[2]}/index.txt", encoding="utf-8")
            except:
                return ("an error occurred", "that's not a supported entry")
        else:
            return ("an error occurred", "that's not a supported entry")
    info = f.read()
    f.close()
    info = info.split("\n")
    return ("information about the entry:", f"name: {info[0]}\nartist(s): {info[1]}\nlanguage(s): {info[2]}")

def getlyrics(message, author):
    plus = False
    contest = message[1]
    if len(message) < 3:
        return ("an error occurred", ":pregnant_man: idk what to do here")
    if message[1] not in contests:
        return ("an error occurred", "either that contest ain't exist or hyacinth got lazy")
    if contest[-1] == "+":
        contest = contest[:-1]
        plus = True
    try:
        f = open(f"contest_{message[1]}/entry_{message[2]}/index.txt", encoding="utf-8")
    except:
        if plus:
            try:
                f = open(f"contest_{message[1]}/plus/entry_{message[2]}/index.txt", encoding="utf-8")
            except:
                return ("an error occurred", "seems that entry doesn't exist within the specified contest")
        return ("an error occurred", "seems that entry doesn't exist within the specified contest")
    info = f.read()
    f.close()
    if info.split("\n")[2] == "Instrumental":
        return ("there are no lyrics to this entry", "embed description")
    if len(message) == 3:
        try:
            f = open(f"contest_{message[1]}/entry_{message[2]}/lyrics.txt", encoding="utf-8")
        except:
            try:
                f = open(f"contest_{message[1]}/plus/entry_{message[2]}/lyrics.txt", encoding="utf-8")
            except:
                return ("an error occurred", "we don't have the lyrics available at this point in time")
            return ("an error occurred", "we don't have the lyrics available at this point in time")
        lyrics = f.read()
        f.close()
    else:
        try:
            f = open(f"contest_{message[1]}/entry_{message[2]}/trans_{message[3]}.txt", encoding="utf-8")
        except:
            try:
                f = open(f"contest_{message[1]}/plus/entry_{message[2]}/trans_{message[3]}.txt", encoding="utf-8")
            except:
                return ("an error occurred", "we don't have the lyrics available at this point in time")
            return ("an error occurred", "we don't have the lyrics available at this point in time")
        lyrics = f.read()
        f.close()
    k = lyrics.index("\n")
    return (lyrics[:k], lyrics[k:])

def suggest(message, author):
    f = open("suggestions.txt", "a")
    f.write(f"user {author} writes:\n{" ".join(message[1:])}\n")
    f.close()
    return ("thank you for the suggestion", "hyacinth will look at it at some point in the future")

def process(message, author):
    if author != 958755251110936627:
        return ("oopsies", "access to this command is for premium users only")
    return ("success", "or maybe not idk")


commandnames = [
    ping,
    ccodes,
    commandslist,
    lcodes,
    entryinfo,
    getlyrics,
    rankings.ranking,
    rankings.combined,
    rankings.descmethods,
    suggest,
    rankings.countrylog,
    rankings.winners,
    process
    ]
