import logging
from discord.app_commands import CommandTree, Command
from discord import Interaction
from ck_bot.utils.constants import CK_BOT_CHANNEL_ID

_log = logging.getLogger(__name__)

# TODO Do not leave any trace of commands in Bot Channel (i.e. The application did not respond)
class BotChannelCommandtree(CommandTree):
    #########################################
    # Public API
    #########################################
    async def interaction_check(self, interaction: Interaction, /) -> bool:
        self.__log_interaction(interaction)
        pass_check: bool = interaction.channel.id == CK_BOT_CHANNEL_ID  # type:ignore
        if not pass_check:
            await interaction.response.send_message(
                "Please enter command in bot channel", ephemeral=True
            )
        return pass_check

    #########################################
    # Private Helper Functions
    #########################################
    def __log_interaction(self, interaction: Interaction):
        command: Command = interaction.command  # type: ignore
        user_input = ""
        namespace_iterator = iter(interaction.namespace)
        for key_pair in namespace_iterator:
            user_input += key_pair[0] + "=" + key_pair[1] + ","
        _log.debug("Command {%s} called with {%s}", command.name, user_input)
