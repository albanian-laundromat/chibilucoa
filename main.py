import discord, commands, random, triggers, yapping
from urllib.request import urlretrieve

validchannels = [1229540258069221540,
                 1249072063784816640,
                 1224369809152806922,
                 1261541638212423761,
                 1264944177729376341]

forbiddenchannels = [1184930234051608666,
                     1260400559559675924,
                     1260400129249382501,
                     1260400004623765554,
                     1260399950500466769,
                     1260399655871578222,
                     1212974285170151466,
                     1264483221907701801,
                     1240736830232723536,
                     1240736830232723539
    ]

skibidichannels = [1259986626482802718,
                   1259353976650862653,
                   1259977074693767219,
                   1259980408318328894,
                   1260063031090479126,
                   1260065292210667550,
                   1260065450927329353,
                   1249072063784816640,
                   1259353976650862653,
                   1263421746770612286
                       ]

forbiddenservers = [1210342412581339156,
                    1238413160688386048,
                    1175162388568354867,
                    1240736830232723536,
                    1240736830232723536
    ]

disabletriggers = [1240736830232723536
                   ]

blacklist = [486185827005628420
             ]

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author} ({message.author.id}) in {message.channel.id}: {message.content}')
        if str(message.author) not in ["chibilucoa#8623", "___hyacinth", "j_lk23"] and message.guild == None:
            user = await self.fetch_user(812493620716371990)
            await user.send(content=f'{str(message.author)} ({message.author.id}) said: {message.content}')
            user = await self.fetch_user(958755251110936627)
            await user.send(content=f'{str(message.author)} ({message.author.id}) said: {message.content}')
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
        if str(message.author) != "chibilucoa#8623" and message.guild and message.guild.id not in disabletriggers:
            yapping.process(message.content.lower().replace("@here","").replace("@everyone", ""))
            if message.channel.id not in forbiddenchannels:
                repliestosend = [(trigger, message.content.lower().index(trigger)) for trigger in triggers.triggers if commands.findindex(message.content.lower(), trigger) != -1]
                for i in sorted(repliestosend, key = commands.rankings.skibidi):
                    await message.channel.send(triggers.triggers[i[0]])
                if (random.randint(1, 20) == 2 or "<@1252795706188496906>" in message.content or message.channel.id in skibidichannels) and message.author.id not in blacklist: 
                    if (message.guild == None or message.guild.id not in forbiddenservers) or message.channel.id in skibidichannels:
                        await message.channel.send(yapping.generate())
                        
        if message.content.split(" ")[0] == "cl$send" and str(message.author) in ["___hyacinth", "j_lk23", "spottedleafofficial"]:

            user = await self.fetch_channel(message.content.split(" ")[1])
            await user.send(content=message.content.split(" ",2)[2])

        if message.content.split(" ")[0] == "cl$dm" and str(message.author) in ["___hyacinth", "j_lk23", "spottedleafofficial"]:

            user = await self.fetch_user(message.content.split(" ")[1])
            await user.send(content=message.content.split(" ",2)[2])

        if message.author.id == 1102939243954847745:
            await message.add_reaction("🤓")

intents = discord.Intents.default()
intents.message_content = True

f = open("token.txt", "r")
token = f.read()
f.close()

client = MyClient(intents=intents)
client.run(token)
