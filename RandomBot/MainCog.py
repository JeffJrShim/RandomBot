import RandomBot.Values
import RandomBot.Choosers
import RandomBot.Shards
import RandomBot.Shufflers

from discord.ext import commands

def setup(bot : commands.Bot):
  bot.add_cog(Values(main=bot))
  bot.add_cog(Choosers(main=bot))
  bot.add_cog(Shards(main=bot))
  bot.add_cog(Shufflers(main=bot))
