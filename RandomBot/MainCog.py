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
  
  # Start Values.py
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

def setup(bot : commands.Bot):
  '''bot.add_cog(Values(main=bot))
  bot.add_cog(Choosers(main=bot))
  bot.add_cog(Shards(main=bot))
  bot.add_cog(Shufflers(main=bot))
  bot.add_cog(Hidden(main=bot))
  bot.add_cog(Generators(main=bot))
  bot.add_cog(Events(main=bot))'''
  bot.add_cog(RandomBotCog(main=bot))
