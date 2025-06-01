import os
import discord
from discord.ext import commands
from discord.ui import View, Button
from discord import app_commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Your pre-approved keys
valid_keys = {
    "YS7PMJtj3#Lw0t@d0R!pNWVnO%xHvw5@",
    "D#qIlW78iO6yGax4^!L24nL#tcB7kj$S",
    "x5@tOqSO7qHwcjHhBSf$8^A5hboa&RQV"
}

# Used keys
used_keys = set()

class ActionButtons(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.redeem_msg = None

    @discord.ui.button(label="Redeem Key", style=discord.ButtonStyle.green, custom_id="redeem")
    async def redeem_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(KeyModal())

    @discord.ui.button(label="Get Script", style=discord.ButtonStyle.blurple, custom_id="get_script")
    async def get_script(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "**Not whitelisted!**\nYou need to be whitelisted to get this script.\nIf you have a script key, click on the Redeem button below to redeem it.",
            ephemeral=True
        )

    @discord.ui.button(label="Buyer Server", style=discord.ButtonStyle.gray, custom_id="buyer_server")
    async def buyer_server(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "**Not whitelisted!**\nYou need to be whitelisted to get this script.\nIf you have a script key, click on the Redeem button below to redeem it.",
            ephemeral=True
        )

    @discord.ui.button(label="Reset HWID", style=discord.ButtonStyle.red, custom_id="reset_hwid")
    async def reset_hwid(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "**Not whitelisted!**\nYou need to be whitelisted to get this script.\nIf you have a script key, click on the Redeem button below to redeem it.",
            ephemeral=True
        )


class KeyModal(discord.ui.Modal, title="Redeem Script Key"):
    key_input = discord.ui.TextInput(label="Enter your 32-character script key", style=discord.TextStyle.short, max_length=32)

    async def on_submit(self, interaction: discord.Interaction):
        key = self.key_input.value.strip()

        if len(key) != 32:
            await interaction.response.send_message("❌ Invalid key format. Make sure it's exactly 32 characters long.", ephemeral=True)
        elif key in used_keys:
            await interaction.response.send_message("An error occurred | Key has already been used.", ephemeral=True)
        elif key in valid_keys:
            used_keys.add(key)
            await interaction.response.send_message("An error occurred | Key has already been used.", ephemeral=True)
        else:
            await interaction.response.send_message("An error occurred | Key doesn't exist.", ephemeral=True)


@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

    # Send the panel message in a specific channel (replace CHANNEL_ID)
    channel = bot.get_channel(1378720138089468095)  # <--- Replace this with your channel ID
    if channel:
        embed = discord.Embed(
            title="Glacier X - Control Panel",
            description=(
                "**This control panel is for the project: Glacier X**\n"
                "If you're a buyer, click on the buttons below to redeem your key, get the script or join the buyer server\n\n"
                "• ɢʟᴀᴄɪᴇʀ x"
            ),
            color=discord.Color.blue()
        )
        await channel.send(embed=embed, view=ActionButtons())

bot.run(os.getenv("BOT_TOKEN"))
