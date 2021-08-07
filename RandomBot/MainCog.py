from redbot.core import commands
import random, discord

class RandomBotCog(commands.Cog):
  def __init__(self, main):
    self.bot = main
  
  #Start Values.py
  @commands.command(name='rbrandomnumber', help='Generates a random number.')
  async def randomnumberexec(self, ctx, nmbr: int=1000000):
    if (nmbr > 1000000000000):
      await ctx.send("I can only generate numbers lower than 1000000000000.")
      return
    response = random.randint(0,nmbr)
    await ctx.send(response)

  @commands.command(name='rbrandomrange', help='Generates a number in a range.')
  async def randomrange(self, ctx, min : int, max : int):
    if (max > 1000000000000):
      await ctx.send("I can only generate numbers lower than 1000000000000.")
      return
    response = random.randint(min,max)
    await ctx.send(response)
  
  @commands.command(name='rbluckynumber', help='Generate a lucky number.')
  async def gennumber(self, ctx):
      newnumber = random.randint(0,100)
      await ctx.send(newnumber)

  @commands.command(name='rbcooltest', help='How cool are you?')
  async def test(self, ctx):
    await ctx.send(f'{ctx.author.mention}, You are {random.randint(0,100)} percent cool.')
  
  @commands.command(name='rbrisktest', help='How risky is something?')
  async def tester(self, ctx, *, idea):
    risk = random.randint(0,100)
    await ctx.send(f'***{idea}*** is {risk}% risky')
  
  @commands.command(name='rbsmarttest', help='How smart are you?')
  async def stester(self, ctx):
    smart = random.randint(0,100)
    await ctx.send(f'{ctx.author.mention}, You are {smart}% smart')

  @commands.command(name='rbrate', help='Rate a thing.')
  async def rs(self, ctx, *, thing):
    v1 = random.randint(0,5)
    v2 = random.randint(0,9)
    if v1 == 5 and v2 > 0:
      await ctx.send(f'I rate ***{thing}*** 5 out of 5 stars.')
    elif v1 == 5 and v2 == 0:
      await ctx.send(f'I rate ***{thing}*** 5 out of 5 stars.')
    elif v1 == 0 and v2 == 0:
      await ctx.send(f'I rate ***{thing}*** 0 out of 5 stars.')
    else:
      await ctx.send(f'I rate ***{thing}*** {v1}.{v2} out of 5 stars.')
  
  @commands.command(name='rbdice', help='Roll dice.')
  async def roll(self, ctx, numberofdice: int, numberofsides: int):
      vdice = [
          str(random.choice(range(1, numberofsides + 1)))
          for _ in range(numberofdice)
      ]
      await ctx.send(', '.join(vdice))
  #End Values.py
  
  #Start Shufflers.py
  @commands.command(name='rbshuffle', help='Shuffle word(s)')
  async def shuffler(self, ctx, *, word: str):
      wordl = list(word)
      random.shuffle(wordl)
      await ctx.send(''.join(wordl))
  
  @commands.command(name='rbshufflebyword', help='Shuffle every word in a sentence.')
  async def shuffleword(self, ctx, *, wordl: str):
      wordl = wordl.split(" ")
      newsentence = []
      for byword in range(len(wordl)):
        wordl1 = list(wordl[byword])
        wordl2 = random.sample(wordl1, len(wordl1))
        newsentence1 = ""
        for wjoin in wordl2:
          newsentence1 += wjoin
        newsentence.append(newsentence1 + ' ')
      wordl = newsentence
      await ctx.send(''.join(wordl))

  @commands.command(name='rbshufflesentence', help='Shuffle words to make a weird sentence.')
  async def makesentence(self, ctx, *, sentence: str):
      wordlist = sentence.split(' ')
      wordlist1 = list(wordlist)
      random.shuffle(wordlist1)
      await ctx.send(' '.join(wordlist1))
  #End Shufflers.py
  
  #Start Shards.py
  @commands.Cog.listener()
  async def on_shard_connect(self,shard_id):
    if shard_id == 0:
      activity = discord.Game(name=f"Starting shard {shard_id+1}.")
      await self.bot.change_presence(status=discord.Status.online, activity=activity)
      print(f"{self.bot.user} has connected.")
    else:
      activity = discord.Game(name=f"Starting shard {shard_id+1}.")
      await self.bot.change_presence(status=discord.Status.online, activity=activity)
      print(f"Shard {shard_id} has connected.")
      print(f"Shard {shard_id+1} is connecting.")

  @commands.Cog.listener()
  async def on_shard_disconnect(self,shard_id):
    print(f"Shard {shard_id} has disconnected.")

  @commands.Cog.listener()
  async def on_shard_resume(self,shard_id):
    print(f"Shard {shard_id} has reconnected.")

  @commands.Cog.listener()
  async def on_shard_ready(self,shard_id):
    print(f"Shard {shard_id} is ready to go!")
  #End Shards.py
  
  #Start Hidden.py
  @commands.command(name="rbsupport", hidden=True)
  async def support(self, ctx):
    embed = discord.Embed()
    embed.add_field(name="Need help?", value="Click [here](https://randombot.tk/support) to join the support server.")
    await ctx.send(embed=embed)
  
  @commands.command(name="rbinvite", hidden=True)
  async def invite(self, ctx):
    embed = discord.Embed()
    embed.add_field(name="Want to invite me?", value="Click [here](https://randombot.tk/invite) to invite me to a server.")
    await ctx.send(embed=embed)
  
  @commands.command(name="rbbotinfo", hidden=True)
  async def botinfo(self, ctx):
            hexlist = '01234567890abcdef'
            colorhex = ''
            for makecolor in range(0,6):
              genhex = random.choice(hexlist)
              colorhex = colorhex + genhex
            color = discord.Color(int(colorhex, 16))
            embed = discord.Embed(color=color)
            embed.add_field(name="Users", value=str(len(self.bot.users)), inline=False)
            embed.add_field(name="Servers", value=str(len(self.bot.guilds)), inline=False)
            if ctx.author.name == ctx.author.display_name:
              embed.set_footer(text=f'Requested by {ctx.author.display_name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
            else:
              embed.set_footer(text=f'Requested by {ctx.author.display_name} ({ctx.author.name}#{ctx.author.discriminator})', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
  #End Hidden.py
  
  #Start Generators.py
  @commands.command(name='rbcolorgen', aliases=['colourgen', 'color', 'colour'], help='Generate a random hex color')
  async def gencolor(self, ctx):
      if length > 1975:
        return await ctx.send("I can only generate passwords shorter than 1975 characters.")
      chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*();,./':<>?\[]}{-=+"
      password=""
      if length > 5:
          for passlength in range(0,length):
              genchar=random.choice(chars)
              password=password+genchar
          if ctx.guild == None:
            await ctx.send(password)
          else:
            await ctx.author.send(f'Generated password: `${password}`')
            await ctx.send('Check your DM\'s.')
      else:
          await ctx.send("There must be at least 6 characters.")
  
  @commands.command(name='rbbinarygen', help='Generate a random binary sequence.')
  async def bgen(self, ctx, length : int):
    if length > 220:
      return await ctx.send("I can only generate binary sequences shorter than 220 chunks.")
    bin = '01'
    gbin = ''
    for bgener1 in range(0, length):
      for bgener2 in range(0,8):
        cbin = random.choice(bin)
        gbin = gbin + cbin
      gbin = gbin + ' '
    await ctx.send(gbin)
  
  @commands.command(name='rbeject', help='Eject a user.')
  async def ejectuser(self, ctx, *, user : discord.Member="you"):
    if user == "you":
      user = ctx.author
    crew = ["black", "blue", "brown", "cyan", "darkgreen", "lime", "orange", "pink", "purple", "red", "white", "yellow"]
    crewcolor = random.choice(crew)
    imp = ["true", "false", "false", "false", "false"]
    isimpostor = random.choice(imp)
    username = str(user.name)
    urlname = urllib.parse.quote(username)
    ejected = f'https://vacefron.nl/api/ejected?name={urlname}&impostor={isimpostor}&crewmate={crewcolor}'
    embed = discord.Embed()
    embed.set_image(url=ejected)
    await ctx.send(embed=embed)

  @commands.command(name='rblettergen', help='Generate a random letter.')
  async def lgen(self, ctx):
      chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
      await ctx.send(random.choice(chars))
  #End Generators.py
  
  #Start Events.py
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    await ctx.send(f'An error occured: {str(error)}')
  
  @commands.Cog.listener()
  async def on_ready(self):
    activity = discord.Game(name="rb.help | Invite the bot: https://randombot.tk/invite")
    await self.bot.change_presence(status=discord.Status.online, activity=activity)
    print(f'{self.bot.user} is ready to go!')

  '''@commands.Cog.listener() 
  async def on_message(self, message):
    if message.content.startswith(""):
      logs = await self.bot.fetch_channel(832337043064488047)
      await logs.send(f"command message sent by ***{message.author.name}#{message.author.discriminator}*** in server ***{message.guild.name}*** (***{message.guild.id}***) in channel ***{message.channel.name}*** (***{message.channel.id}***). content: {message.content}")
    for x in message.mentions:
        if(x==self.bot.user):
          if message.content.split() == ['<@!716309071854174268>'] or message.content.split() == ['<@716309071854174268>']:
            if message.author.bot:
              return
            hexlist = '01234567890abcdef'
            colorhex = ''
            for makecolor in range(0,6):
              genhex = random.choice(hexlist)
              colorhex = colorhex + genhex
            color = discord.Color(int(colorhex, 16))
            embed = discord.Embed(color=color, title="Hello, my name is RandomBot!")
            embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/716309071854174268/da597c1ceb8aac700263b371bc3c1fc2.webp?size=1024')
            embed.add_field(name="The developer", value="GD Tom#0001", inline=False)
            embed.add_field(name="Did something go wrong?", value="[Click this to join the support server.](https://randombot.tk/support)", inline=False)
            embed.add_field(name="Want to invite me to your server?", value="[Click this to invite me!](https://randombot.tk/invite)", inline=False)
            embed.add_field(name="About Me:", value="I started as a useless app, but then the developer\ndecided to make a bot. I was already in the developer\nportal so the developer took me and made me\na working bot. He already knew Python\nso he coded me. I am what he made.", inline=False)
            embed.add_field(name="My prefix:", value="rb.", inline=False)
            if message.author.name == message.author.display_name:
              embed.set_footer(text=f'Requested by {message.author.display_name}#{message.author.discriminator}', icon_url=message.author.avatar_url)
            else:
              embed.set_footer(text=f'Requested by {message.author.display_name} ({message.author.name}#{message.author.discriminator})', icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)'''
 #End Events.py

 #Start Choosers.py
  @commands.Cog.listener()
  async def on_reaction_remove(self, reaction, user):
    if str(reaction.emoji) == "🎉":
      uinfo = f'{user}'
      greactors.remove(uinfo)

  @commands.command(name="rbchoose", help="Seperate choices with \" + \"")
  async def c(self,ctx, *, options):
    osplit = options.split(" + ")
    ping = False
    for option in osplit:
      if option.startswith("<@") or option.startswith("@here") or option.startswith("@everyone"):
        ping = True
    if ping:
      return await ctx.send("I can't ping.")
    choice = random.choice(osplit)
    await ctx.send(f"I choose ***{choice}***.")

  @commands.command(name='rbdecide', help="Decide on something for you")
  async def chooser(self, ctx, *, thing):
    options = ['Yes.', 'For sure!', 'Maybe.', 'I don\'t know.', 'No.', 'Definently not.', 'Definently!']
    choic3 = random.choice(options)
    await ctx.send(choic3)
  
  @commands.command(name="rbrandomuser", description="Chooses a member from the member type")
  async def randomuser(self, ctx, usertype):
    if usertype == "bot":
      users = ctx.guild.members
      while True:
        chosen = random.choice(users)
        if not chosen.bot:
          continue
        elif chosen.id != self.bot.user.id:
          await ctx.send(f"{chosen.name}#{chosen.discriminator}")
          return
    elif usertype == "user":
      users = ctx.guild.members
      while True:
        chosen = random.choice(users)
        if not chosen.bot:
          await ctx.send(f"{chosen.name}#{chosen.discriminator}")
          return
        else:
          continue
    else:
      await ctx.send("Type invalid, wanted user or bot.")
#End Choosers.py

def setup(bot : commands.Bot):
  '''bot.add_cog(Values(main=bot))
  bot.add_cog(Choosers(main=bot))
  bot.add_cog(Shards(main=bot))
  bot.add_cog(Shufflers(main=bot))
  bot.add_cog(Hidden(main=bot))
  bot.add_cog(Generators(main=bot))
  bot.add_cog(Events(main=bot))'''
  bot.add_cog(RandomBotCog(main=bot))
