import os, rankingmethods

f = open("contests.txt", "r", encoding="utf-8")
contests = f.read().split("\n")
f.close()

f = open("ccodes.txt", "r", encoding="utf-8")
codes = f.read().split("\n")
f.close()
ccodes = {}
for i in codes:
    ccodes[i[:3]] = i[4:]

supportedcommands = [
    "submit",
    "view",
    "delete",
    "copy"
    ]

def isinternational(contest):
    return contest[0].isnumeric() or (contest[0] == "w" and contest[1].isnumeric())

def getentries(contest):
    plus = False
    if contest[-1] == "+":
        plus = True
        contest = contest[:-1]
    dirlist = os.listdir(f"contest_{contest}/")
    countrylist = [i[6:] for i in dirlist if i.startswith("entry_")]
    if plus:
        dirlist = os.listdir(f"contest_{contest}/plus/")
        countrylist += [i[6:] for i in dirlist if i.startswith("entry_")]
    return countrylist

def gettitle(contest, code):
    plus = False
    if contest[-1] == "+":
        plus = True
        contest = contest[:-1]
    try:
        f = open(f"contest_{contest}/entry_{code}/index.txt", encoding="utf-8")
    except:
        f = open(f"contest_{contest}/plus/entry_{code}/index.txt", encoding="utf-8")
    title = f.read().split("\n")[0]
    f.close()
    return title

def skibidi(toilet):
    return toilet[1]

def splitbylist(characters, stringtosplit):
    output = [""]
    for i in stringtosplit:
        if i in characters:
            output.append("")
        else:
            output[-1] += i
    return [i for i in output if i]

def compileranking(ranking, flip = False):
    if flip:
        newranking = [[country, 1 + len([i for i in ranking.keys() if ranking[i] < ranking[country]])] for country in ranking.keys()]
    else:
        newranking = [[country, 1 + len([i for i in ranking.keys() if ranking[i] > ranking[country]])] for country in ranking.keys()]
    sortedlist = sorted(newranking, key = skibidi)
    output = ""
    for i in sortedlist:
        output += f"`{str(i[1]+1000)[1:]}` {round(ranking[i[0]], 2)} \t {i[0]}\n"
    return output

def submit(message, author):
    contest = message[0]
    international = isinternational(contest)    
    entrylist = getentries(message[0])
    ranking = splitbylist(" ,\n", " ".join(message[1:]))
    plus = False
    if contest[-1] == "+":
        plus = True
        contest = contest[:-1]
    if sorted(ranking) == sorted(entrylist):
        hasranking = True
        try:
            if plus:
                f = open(f"contest_{contest}/plus/rankings/{author}.txt", "r", encoding="utf-8")
            else:
                f = open(f"contest_{contest}/rankings/{author}.txt", "r", encoding="utf-8")
            oldranking = f.read().split("\n")
            f.close()
        except:
            hasranking = False
            oldranking = None
        if plus:
            f = open(f"contest_{contest}/plus/rankings/{author}.txt", "w", encoding="utf-8")
        else:
            f = open(f"contest_{contest}/rankings/{author}.txt", "w", encoding="utf-8")
        f.write("\n".join(ranking))
        title = "your ranking:"
        output = ""
        for i in range(len(ranking)):
            changed = False
            status = ""
            country = ranking[i]
            if hasranking:
                try:
                    oldrank = oldranking.index(country)
                    difference = oldrank - i
                    if difference:
                        changed = True
                    if difference <= 0:
                        status = f"({difference})"
                    else:
                        status = f"(+{difference})"
                except:
                    status = "(NEW)"
                    changed = True
            if international:
                thingtoadd = f"`{str(i + 1001)[1:]}` {ccodes[country]}"
            else:
                thingtoadd = f"`{str(i + 1001)[1:]}` {gettitle(message[0], country)}"
            if hasranking and changed:
                thingtoadd += f" **{status}**"
            output += thingtoadd + "\n"
        return (title, output)
    else:
        junk = [i for i in ranking if i not in entrylist]
        missing = [i for i in entrylist if i not in ranking]
        extra = [i for i in entrylist if ranking.count(i) > 1]
        title = "something went wrong:"
        output = ""
        if junk:
            output += f"i don't understand: `{', '.join(junk)}`\n"
        if missing:
            output += f"you are missing: `{', '.join(missing)}`\n"
        if extra:
            output += f"you have too many of: `{', '.join(extra)}`\n"   
        return (title, output)
    
def delete(message, author):
    plus = False
    contest = message[0]
    if contest[-1] == "+":
        plus = True
        contest = contest[:-1]
    try:
        if plus:
            os.remove(f"contest_{contest}/plus/rankings/{author}.txt")
        else:
            os.remove(f"contest_{contest}/rankings/{author}.txt")
        return ("ranking deleted successfully!", "what the title said")
    except:
        return ("you don't have a ranking to delete!", "silly you")

def view(message, author):
    plus = False
    contest = message[0]
    if contest[-1] == "+":
        plus = True
        contest = contest[:-1]
    international = isinternational(contest) 
    selfrequest = (len(message) > 3)
    if selfrequest:
        referent = message[1]
        if not referent.isnumeric():
            return ("an error occured", "that doesn't appear to be a valid user id")
    else:
        referent = author
    try:
        if plus:
            f = open(f"contest_{contest}/plus/rankings/{referent}.txt", "r")
        else:
            f = open(f"contest_{contest}/rankings/{referent}.txt", "r")
        ranking = f.read()
        f.close()
        ranking = [i for i in ranking.split("\n") if i]
        if selfrequest:
            title = "your ranking"
        else:
            title = f"ranking of user {referent}:"
        output = ""
        for i in range(len(ranking)):
            if international:
                output += f"`{str(i + 1001)[1:]}` {ccodes[ranking[i]]}\n"
            else:
                output += f"`{str(i + 1001)[1:]}` {gettitle(message[0], ranking[i])}\n"
        return (title, output)
    except:
        if selfrequest:
            return ("you don't appear to have a ranking", "go make one now!")
        else:
            return ("something went wrong", "either that user doesn't exist or they don't have a ranking of that contest")

def copy(message, author):
    plus = False
    contest = message[0]
    if contest[-1] == "+":
        plus = True
        contest = contest[:-1]
    try:
        if plus:
            f = open(f"contest_{contest}/plus/rankings/{author}.txt", "r")
        else:
            f = open(f"contest_{contest}/rankings/{author}.txt", "r")
        ranking = f.read()
        f.close()
        ranking = [i for i in ranking.split("\n") if i]
        output = " ".join(ranking)
        return ("your ranking of the contest", f"`$ranking submit {message[0]} {output}`")
    except:
        return ("you don't appear to have a ranking", "go make one now!")

functionnames = [
    submit,
    view,
    delete,
    copy
    ]

def ranking(message, author):
    if len(message) == 1:
        return ("an error occured", "what do you want to do?")
    if message[1] not in supportedcommands:
        return ("an error occured", "that's not a supported command")
    if len(message) == 2:
        return ("an error occured", "you need to specify a contest")
    if message[2] not in contests:
        return ("an error occured", "that's not a valid contest")
    functiontorun = functionnames[supportedcommands.index(message[1])]
    return functiontorun(message[2:], author)

def combined(message, author):
    if len(message) == 1:
        return ("an error occured", "please provide a contest")
    if message[1] not in contests:
        return ("an error occured", "that's not a valid contest")
    contest = message[1]
    entries = getentries(contest)
    plus = False
    if contest[-1] == "+":
        plus = True
        contest = contest[:-1]
    international = isinternational(contest)
    method = [i[2:] for i in message if i.startswith("r-")]
    method = [i for i in method if i in rankingmethods.methodids]
    if method:
        method = method[0]
    else:
        method = "1"
    size = len(entries)
    scores = {}
    for entry in entries:
        scores[entry] = []
    if plus:
        folder = f"contest_{contest}/plus/rankings/"
    else:
        folder = f"contest_{contest}/rankings/"
    for ranked in os.listdir(folder):
        f = open(f"{folder}{ranked}")
        rank = f.read().split("\n")
        f.close()
        if set(rank) != set(entries):
            continue
        for entry in entries:
            scores[entry].append(1 + rank.index(entry))
    numbers = {}
    for entry in entries:
        if international:
            numbers[ccodes[entry]] = rankingmethods.usemethod(scores[entry], size, method)
        else:
            numbers[gettitle(contest, entry)] = rankingmethods.usemethod(scores[entry], size, method)
    return ("the global ranking of the requested contest with the requested ranking system:", compileranking(numbers, method in rankingmethods.reversethese))

def descmethods(message, author):
    return ("all supported ranking methods:", rankingmethods.description)

def countrylog(message, author):
    if len(message) == 1:
        return ("an error occured", "please specify a country")
    if message[1] not in ccodes.keys():
        return ("an error occured", "that is not a valid country code")
    country = message[1]
    if len(message) > 2:
        referent = message[2]
        if not referent.isnumeric():
            return ("an error occured", "that's not a valid user id")
        title = f"user {referent}'s rankings of {ccodes[country]}:"
    else:
        referent = author
        title = f"your rankings of {ccodes[country]}:"
    output = ""
    badvisioneditions = sorted([i for i in contests if i[0].isnumeric()])
    for edition in badvisioneditions:
        try:
            f = open(f"contest_{edition}/entry_{country}/index.txt")
            name = f.read().split("\n")[0]
            f.close()
        except:
            continue
        line = "**" + edition + "** " + name
        try:
            f = open(f"contest_{edition}/rankings/{referent}.txt")
            placing = 1 + f.read().split("\n").index(country)
            f.close()
            line += f" **{placing}/{len(getentries(edition))}**"
            if placing == len(getentries(edition)):
                line += " <:BOOOHOOHOHOOHO:1246931137771733195>"
            elif placing == 1:
                line += " <:kabir:1223783550726311986>"
        except:
            pass
        output += f"{line}\n"
    return (title, output)
        
def winners(message, author):
    if len(message) == 1:
        referent = author
        title = f"your badvision winners"
    else:
        referent = message[1]
        title = f"user {referent}'s badvision winners"
        if not referent.isnumeric():
            return ("an error occurred", "that's not a valid user id")
    badvisioneditions = sorted([i for i in contests if i[0].isnumeric()])
    output = ""
    hasrankings = False
    for edition in badvisioneditions:
        try:
            f = open(f"contest_{edition}/rankings/{referent}.txt")
            winner = ccodes[f.read().split("\n")[0]]
            f.close()
            output += f"`{edition}` {winner}\n"
            hasrankings = True
        except:
            pass
    if not hasrankings:
        return ("an error occurred", "you or the requested user has no badvision rakings")
    return (title, output)

def entries(message, author):
    if len(message) == 1:
        return
    contest = message[1]
