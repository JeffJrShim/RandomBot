from RandomBot.Values import *
from RandomBot.Choosers import *
from RandomBot.Shards import *
from RandomBot.Shufflers import *
from RandomBot.Hidden import *
from RandomBot.Generators import *
from RandomBot.Events import *

from discord.ext import commands

def setup(bot : commands.Bot):
  bot.add_cog(Values(main=bot))
  bot.add_cog(Choosers(main=bot))
  bot.add_cog(Shards(main=bot))
  bot.add_cog(Shufflers(main=bot))
  bot.add_cog(Hidden(main=bot))
  bot.add_cog(Generators(main=bot))
  bot.add_cog(Events(main=bot))
