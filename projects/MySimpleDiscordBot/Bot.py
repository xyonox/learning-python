import discord
from discord.ext import commands

class MyBot(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # Überprüfe, ob die Nachricht nicht vom Bot selbst stammt
        if message.author == self.user:
            return
        print(f'Message from {message.author}: {message.content}')
        await self.process_commands(message)  # Stelle sicher, dass Befehle verarbeitet werden

intents = discord.Intents.default()
intents.message_content = True

file_path = "C:\\Users\\carlf\\OneDrive\\Dokumente\\ep-s\\tst.txt"
with open(file_path, "r") as f:
    token = f.read().strip()

bot = MyBot(command_prefix=".", intents=intents)

@bot.command()
async def hey(ctx, arg):
    await ctx.send(arg)

bot.run(token)
