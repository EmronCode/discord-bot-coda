import discord
from discord.ext import commands

class TicTacToeButton(discord.ui.Button):
    def __init__(self, row, col):
        super().__init__(style=discord.ButtonStyle.secondary, label="⬜", row=row)
        self.row_index = row
        self.col_index = col

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"You clicked cell ({self.row_index}, {self.col_index})",
            ephemeral=True
        )

class TicTacToeView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        for row in range(3):
            for col in range(3):
                self.add_item(TicTacToeButton(row, col))

class TicTacToeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tictactoe(self, ctx):
        """Clickable TicTacToe grid"""
        view = TicTacToeView()
        await ctx.send("TicTacToe Game (click a cell):", view=view)

async def setup(bot):
    await bot.add_cog(TicTacToeCog(bot))