import RandomBot.Values.*
import RandomBot.Choosers.*
import RandomBot.Shards.*
import RandomBot.Shufflers.*
import RandomBot.Hidden.*
import RandomBot.Generators.*
import RandomBot.Events.*

from discord.ext import commands

def setup(bot : commands.Bot):
  bot.add_cog(Values(main=bot))
  bot.add_cog(Choosers(main=bot))
  bot.add_cog(Shards(main=bot))
  bot.add_cog(Shufflers(main=bot))
  bot.add_cog(Hidden(main=bot))
  bot.add_cog(Generators(main=bot))
  bot.add_cog(Events(main=bot))
