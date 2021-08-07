from RandomBot.Values import *
from RandomBot.Choosers import *
from RandomBot.Shards import *
from RandomBot.Shufflers import *
from RandomBot.Hidden import *
from RandomBot.Generators import *
from RandomBot.Events import *

from discord.ext import commands

Cogs = (Choosers, Shards, Shufflers, Hidden, Generators, Events)

class RandomBotCog(commands.Cog, *Cogs):
  def __init__(self, main):
    self.bot = main
  
  #Start Values.py
  @commands.command(name='randomnumber', help='Generates a random number.')
  async def randomnumberexec(self, ctx, nmbr: int=1000000):
    if (nmbr > 1000000000000):
      await ctx.send("I can only generate numbers lower than 1000000000000.")
      return
    response = random.randint(0,nmbr)
    await ctx.send(response)

  @commands.command(name='randomrange', help='Generates a number in a range.')
  async def randomrange(self, ctx, min : int, max : int):
    if (max > 1000000000000):
      await ctx.send("I can only generate numbers lower than 1000000000000.")
      return
    response = random.randint(min,max)
    await ctx.send(response)
  
  @commands.command(name='luckynumber', help='Generate a lucky number.')
  async def gennumber(self, ctx):
      newnumber = random.randint(0,100)
      await ctx.send(newnumber)

  @commands.command(name='cooltest', help='How cool are you?')
  async def test(self, ctx):
    await ctx.send(f'{ctx.author.mention}, You are {random.randint(0,100)} percent cool.')
  
  @commands.command(name='risktest', help='How risky is something?')
  async def tester(self, ctx, *, idea):
    risk = random.randint(0,100)
    await ctx.send(f'***{idea}*** is {risk}% risky')
  
  @commands.command(name='smarttest', help='How smart are you?')
  async def stester(self, ctx):
    smart = random.randint(0,100)
    await ctx.send(f'{ctx.author.mention}, You are {smart}% smart')

  @commands.command(name='rate', help='Rate a thing.')
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
  
  @commands.command(name='dice', help='Roll dice.')
  async def roll(self, ctx, numberofdice: int, numberofsides: int):
      vdice = [
          str(random.choice(range(1, numberofsides + 1)))
          for _ in range(numberofdice)
      ]
      await ctx.send(', '.join(vdice))
  #End Values.py
  
  #Start Shufflers.py
  @commands.command(name='shuffle', help='Shuffle word(s)')
  async def shuffler(self, ctx, *, word: str):
      wordl = list(word)
      random.shuffle(wordl)
      await ctx.send(''.join(wordl))
  
  @commands.command(name='shufflebyword', help='Shuffle every word in a sentence.')
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

  @commands.command(name='shufflesentence', help='Shuffle words to make a weird sentence.')
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
  @commands.command(hidden=True)
  async def support(self, ctx):
    embed = discord.Embed()
    embed.add_field(name="Need help?", value="Click [here](https://randombot.tk/support) to join the support server.")
    await ctx.send(embed=embed)
  
  @commands.command(hidden=True)
  async def invite(self, ctx):
    embed = discord.Embed()
    embed.add_field(name="Want to invite me?", value="Click [here](https://randombot.tk/invite) to invite me to a server.")
    await ctx.send(embed=embed)
  
  @commands.command(hidden=True)
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
  
  

def setup(bot : commands.Bot):
  '''bot.add_cog(Values(main=bot))
  bot.add_cog(Choosers(main=bot))
  bot.add_cog(Shards(main=bot))
  bot.add_cog(Shufflers(main=bot))
  bot.add_cog(Hidden(main=bot))
  bot.add_cog(Generators(main=bot))
  bot.add_cog(Events(main=bot))'''
  bot.add_cog(RandomBotCog(main=bot))
