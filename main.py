import discord, commands, random, triggers, yapping
from urllib.request import urlretrieve

validchannels = [1229540258069221540,
                 1249072063784816640,
                 1224369809152806922,
                 1261541638212423761,
                 1264944177729376341]

forbiddenchannels = [#1184930234051608666,
                     1260400559559675924,
                     1260400129249382501,
                     1260400004623765554,
                     1260399950500466769,
                     1260399655871578222,
                     1212974285170151466,
                     1264483221907701801,
                     1240736830232723536,
                     1240736830232723539,
                     1184930234051608666
    ]

skibidichannels = [1259986626482802718,
                   1259353976650862653,
                   1259977074693767219,
                   1259980408318328894,
                   1260063031090479126,
                   1260065292210667550,
                   1260065450927329353,
                   #1249072063784816640,
                   1259353976650862653,
                   1263421746770612286
                       ]

forbiddenservers = [1210342412581339156,
                    1238413160688386048,
                    #1175162388568354867,
                    1240736830232723536,
                    1240736830232723536,
                    1200106243071692890
    ]

disabletriggers = [1240736830232723536,
                   1210342412581339156,
                   1175162388568354867
                   ]

blacklist = [486185827005628420,
             749043503379775509,
             1102939243954847745
             ]

admins = [958755251110936627,
          812493620716371990
    ]

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        try:
            k = f'Message from {message.author} ({message.author.id}) in {message.channel.name} ({message.channel.id}), {message.guild.name} ({message.guild.id}): {message.content}'
        except:
            k = f'Message from {message.author} ({message.author.id}): {message.content}'
            print(k)
            if message.channel.id != 1266944000963776515:
                logs = await self.fetch_channel(1266944000963776515)
                await logs.send(k)
                if message.attachments != []:
                    for i in message.attachments:
                        await logs.send(i.url)
        print(k)
        if message.content.startswith("$")\
        and len(message.content.strip()) > 1\
        and str(message.author) != "chibilucoa#8623"\
        and message.channel.id in validchannels:
            components = [i for i in message.content[1:].split(" ") if i]
            if components[0] in commands.validcommands:
                functiontorun = commands.commandnames[commands.validcommands.index(components[0])]
                results = functiontorun(components, message.author.id)
                if len(results) == 2:
                    title, reply = results
                    embed=discord.Embed(title = title, description = reply, color = 0xf5bc20)
                await message.reply(mention_author=False, embed=embed)
            else:
                embed=discord.Embed()
                embed.add_field(name="hey so uhh", value=components[0] + " is not a recognized command. Please try again.", inline=False)
                await message.reply(mention_author=False, embed=embed)
        if str(message.author) != "chibilucoa#8623" and message.guild and message.author.id not in blacklist and not message.content.startswith("cl$"):
            yapping.process(message.content.lower().replace("@here","").replace("@everyone", ""))
            if message.channel.id not in forbiddenchannels:
                repliestosend = [(trigger, message.content.lower().index(trigger)) for trigger in triggers.triggers\
                                 if commands.findindex(message.content.lower(), trigger) != -1]
                if message.guild.id not in disabletriggers:
                    for i in sorted(repliestosend, key = commands.rankings.skibidi):
                        await message.channel.send(triggers.triggers[i[0]])
                if (random.randint(1, 40) == 2 or "<@1252795706188496906>" in message.content or message.channel.id in skibidichannels) and message.author.id not in blacklist: 
                    if (message.guild == None or message.guild.id not in forbiddenservers) or message.channel.id in skibidichannels:
                        await message.channel.send(yapping.generate())
                        
        if message.content.split(" ")[0] == "cl$send" and str(message.author) in ["___hyacinth", "j_lk23", "spottedleafofficial"]:

            user = await self.fetch_channel(message.content.split(" ")[1])
            await user.send(content=message.content.split(" ",2)[2])

        if message.content.split(" ")[0] == "cl$del" and str(message.author) in ["___hyacinth", "j_lk23", "spottedleafofficial"]:

            user = await self.fetch_channel(message.content.split(" ")[1])
            user2 = await user.fetch_message(message.content.split(" ")[2])
            await user2.delete()

        if message.content.split(" ")[0] == "cl$dm" and str(message.author) in ["___hyacinth", "j_lk23", "spottedleafofficial"]:

            user = await self.fetch_user(message.content.split(" ")[1])
            await user.send(content=message.content.split(" ",2)[2])

        if message.author.id in [1102939243954847745, 546463211675844653]:
            await message.add_reaction("🤓")

        if "pillalu" in message.content.lower():
            await message.add_reaction("<:ramanujan:1196873462317326516>")

        """if message.author.id in [1102939243954847745, 546463211675844653]:
            await message.add_reaction("🤓")
            if message.author.id == 546463211675844653:
                await message.add_reaction("<:ted:1197556869166804992>")

        if message.author.id == 749043503379775509:
            await message.add_reaction("🤫")

        if message.author.id == 749043503379775509:
            await message.add_reaction("🧏")

        if message.author.id == 1110016316309520394:
            await message.add_reaction("<:Horny:1233921381305942017>")

        if message.author.id == 812493620716371990:
            await message.add_reaction("🔥")

        if message.author.id == 768471140649402408:
            for i in "🇸 🇹 🇫 🇺":
                if i != " ":
                    await message.add_reaction(i)"""

        if message.content.startswith("cl$queue ") and message.channel.id == 1212984565958713374:
            if len(message.content) > 20:
                f = open("questions.txt", "a")
                f.write("\n" + message.content[9:].replace("\n", " "))
                f.close()
                await message.channel.send(f"Your question,\n{message.content[9:].replace('\n', ' ')}\nhas been added to the queue")
            else:
                await message.channel.send("Your question needs to be longer")

        if message.content == "cl$qotd" and message.channel.id == 1212984565958713374 and message.author.id in admins:
            f = open("questions.txt", "r")
            questions = f.read().split("\n")
            f.close()
            question = questions.pop(0)

            await message.channel.send(f"# QOTD\n\n{question}")

            f = open("questions.txt", "w")
            f.write("\n".join(questions))
            f.close()

        if message.content == "cl$bars":
            k = []
            for i in range(4):
                e = yapping.generate()[:-3]
                for j in "\n=/<>@%#$&*(){}[]`:0123456789":
                    e = e.replace(j, " ")
                k.append(e)
                if i % 4 == 3:
                    k.append("")
            await message.channel.send("\n".join(k))
                

        
intents = discord.Intents.default()
intents.message_content = True

f = open("token.txt", "r")
token = f.read()
f.close()

client = MyClient(intents=intents)
client.run(token)
