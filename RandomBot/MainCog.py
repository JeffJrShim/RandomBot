from redbot.core import commands
import random, discord
from asyncio import sleep

class RandomBot(commands.Cog):
  """ RandomBot's main cog """
  def __init__(self, main):
    self.bot = main
  
  #Start Values.py
  @commands.command(name='rbrandomnumber', help='Generates a random number.')
  async def randomnumberexec(self, ctx, nmbr: int=1000000):
    """ Generates a random number. """
    if (nmbr > 1000000000000):
      await ctx.send("I can only generate numbers lower than 1000000000000.")
      return
    response = random.randint(0,nmbr)
    await ctx.send(response)

  @commands.command(name='rbrandomrange', help='Generates a number in a range.')
  async def randomrange(self, ctx, min : int, max : int):
    """ Generates a number in a range. """
    if (max > 1000000000000):
      await ctx.send("I can only generate numbers lower than 1000000000000.")
      return
    response = random.randint(min,max)
    await ctx.send(response)
  
  @commands.command(name='rbluckynumber', help='Generate a lucky number.')
  async def gennumber(self, ctx):
      """ Generate a lucky number. """
      newnumber = random.randint(0,100)
      await ctx.send(newnumber)

  @commands.command(name='rbcooltest', help='How cool are you?')
  async def test(self, ctx):
    """ How cool are you? """
    await ctx.send(f'{ctx.author.mention}, You are {random.randint(0,100)} percent cool.')
  
  @commands.command(name='rbrisktest', help='How risky is something?')
  async def tester(self, ctx, *, idea):
    """ How risky is something? """
    risk = random.randint(0,100)
    await ctx.send(f'***{idea}*** is {risk}% risky')
  
  @commands.command(name='rbsmarttest', help='How smart are you?')
  async def stester(self, ctx):
    """ How smart are you? """
    smart = random.randint(0,100)
    await ctx.send(f'{ctx.author.mention}, You are {smart}% smart')

  @commands.command(name='rbrate', help='Rate a thing.')
  async def rs(self, ctx, *, thing):
    """ Rate a thing. """
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
      """ Roll dice. """
      vdice = [
          str(random.choice(range(1, numberofsides + 1)))
          for _ in range(numberofdice)
      ]
      await ctx.send(', '.join(vdice))
  #End Values.py
  
  #Start Shufflers.py
  @commands.command(name='rbshuffle', help='Shuffle word(s)')
  async def shuffler(self, ctx, *, word: str):
      """ Shuffle word(s) """
      wordl = list(word)
      random.shuffle(wordl)
      await ctx.send(''.join(wordl))
  
  @commands.command(name='rbshufflebyword', help='Shuffle every word in a sentence.')
  async def shuffleword(self, ctx, *, wordl: str):
      """ Shuffle every word in a sentence. """
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
      """ Shuffle words to make a weird sentence. """
      wordlist = sentence.split(' ')
      wordlist1 = list(wordlist)
      random.shuffle(wordlist1)
      await ctx.send(' '.join(wordlist1))
  #End Shufflers.py
  
  
  #Start Generators.py
  @commands.command(name='rbcolorgen', aliases=['rbcolourgen', 'rbcolor', 'rbcolour'], help='Generate a random hex color')
  async def gencolor(self, ctx):
    """ Generate a random hex color """
    hexlist = '01234567890abcdef'
    colorhex = ''
    for makecolor in range(0,6):
      genhex = random.choice(hexlist)
      colorhex = colorhex + genhex
    color = discord.Color(int(colorhex, 16))
    colrgb = discord.Color.to_rgb(color)
    embed=discord.Embed(title=f'{color} {colrgb}', color=color)
    await ctx.send(embed=embed)
  
  @commands.command(name='rbpasswordgen', help='Generate a random password')
  async def genpass(self, ctx):
      """ Generate a random password """
      if length > 1975:
        return await ctx.send("I can only generate passwords shorter than 1975 characters.")
      chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*();,./':<>?\\[]}{-=+"
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
    """ Generate a random binary sequence. """
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
    """ Eject a user. """
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
      """ Generate a random letter. """
      chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
      await ctx.send(random.choice(chars))
  #End Generators.py

 #Start Choosers.py
  @commands.command(name='rbyesorno', help='Randomly choose yes or no.')
  async def fiftyfifty(self, ctx, yespercent: int=50, nopercent: int=50):
      """ Randomly choose yes or no. """
      if nopercent + yespercent == 100:
          y="Yes. "
          n="No. "
          ychance=y*yespercent
          nchance=n*nopercent
          yn=ychance+nchance
          yn2 = yn.split(" ")
          result=random.choice(yn2)
          await ctx.send(result)
      else:
          await ctx.send("Invalid percentage or value.")

  @commands.command(name='rbflipcoin', help='Flip a coin.')
  async def flip(self, ctx):
      """ Flip a coin. """
      h="Heads! "
      t="Tails! "
      hchance=h*50
      tchance=t*50
      ht=hchance+tchance
      ht2 = ht.split(" ")
      result=random.choice(ht2)
      await ctx.send(result)
  
  global greactors
  greactors = []

  @commands.command(name="rbgiveaway", description="Start a giveaway.")
  async def gstart(self, ctx, channel:discord.TextChannel, gtime:int, *, reward):
    """ Start a giveaway. """
    if gtime > 86400:
      return await ctx.send("I can only do giveaways shorter than 1 day.")
    global greactors
    gtimes = 0
    embed = discord.Embed(title="New giveaway!")
    embed.add_field(name="Prize", value=reward)
    embed.add_field(name="Time", value=f'{gtime} seconds')
    embed.add_field(name="Host", value=f'{ctx.author.name}#{ctx.author.discriminator}')
    gembed = await channel.send(embed=embed)
    await gembed.add_reaction("🎉")
    nembed = None
    while gtime > 0:
      await sleep(10)
      gtime = gtime - 10
      nembed = discord.Embed(title="New giveaway!")
      nembed.add_field(name="Prize", value=reward)
      nembed.add_field(name="Time", value=f'{gtime} seconds')
      nembed.add_field(name="Host", value=f'{ctx.author.name}#{ctx.author.discriminator}')
      await gembed.edit(embed=nembed)
    chosenuser = random.choice(greactors)
    while True:
      if chosenuser == f"{self.bot.user.name}#{self.bot.user.discriminator}" or chosenuser == f"{ctx.author.name}#{ctx.author.discriminator}":
        if gtimes == 100:
          wembed = discord.Embed(title=f'Nobody won the {reward} giveaway.')
          await gembed.edit(embed=wembed)
          greactors = []
          return 
        else:
          gtimes = gtimes + 1
          chosenuser = random.choice(greactors)
      else:
        wembed = discord.Embed(title=f'{chosenuser} won the {reward} giveaway!')
        await gembed.edit(embed=wembed)
        greactors = []
        return

  @commands.Cog.listener()
  async def on_reaction_add(self, reaction, user):
    if str(reaction.emoji) == "🎉":
      uinfo = f'{user}'
      greactors.append(uinfo)
  
  @commands.Cog.listener()
  async def on_reaction_remove(self, reaction, user):
    if str(reaction.emoji) == "🎉":
      uinfo = f'{user}'
      greactors.remove(uinfo)

  @commands.command(name="rbchoose", help="Seperate choices with \" + \"")
  async def c(self,ctx, *, options):
    """ Chooses a random item out of a list seprated with " + " """
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
    """ Decide on something for you """
    options = ['Yes.', 'For sure!', 'Maybe.', 'I don\'t know.', 'No.', 'Definently not.', 'Definently!']
    choic3 = random.choice(options)
    await ctx.send(choic3)
  
  @commands.command(name="rbrandomuser", description="Chooses a member from the member type")
  async def randomuser(self, ctx, usertype):
    """ Chooses a member from the member type """
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
  bot.add_cog(RandomBot(main=bot))
