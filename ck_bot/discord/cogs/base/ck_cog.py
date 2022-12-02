from discord import app_commands
from discord.ext.commands import Cog

from ...constants import CK_GUILD


@app_commands.guild_only()
@app_commands.guilds(CK_GUILD)
class CKCog(Cog):
    pass
