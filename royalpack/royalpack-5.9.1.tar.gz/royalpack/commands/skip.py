from typing import *
import discord
import royalnet.commands as rc


class SkipCommand(rc.Command):
    name: str = "skip"

    aliases = ["s"]

    description: str = "Salta il file attualmente in riproduzione."

    async def run(self, args: rc.CommandArgs, data: rc.CommandData) -> None:
        if self.interface.name == "discord":
            message: discord.Message = data.message
            guild: discord.Guild = message.guild
            guild_id: Optional[int] = guild.id
        else:
            guild_id = None
        response: Dict[str, Any] = await self.interface.call_herald_event("discord", "discord_skip", guild_id=guild_id)
        await data.reply("⏩ File attuale saltato!")
