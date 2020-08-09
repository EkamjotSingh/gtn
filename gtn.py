import discord
from discord.ext import commands , tasks
from discord.ext.commands import Bot , has_permissions
import time
import json

client = commands.Bot(command_prefix="n!")

@client.remove_command("help")

@client.event
async def on_ready():
    print("I am ready")

@client.command()
@has_permissions(administrator=True)
async def set(ctx , number: int):
    with open("gtn_json.json" , "w") as f:


        numb = {}
        numb['number'] = int(number)
        numb['ID'] = int(ctx.guild.id)

        num = json.dump(numb , f , indent=4)

    await ctx.send(f"Done! **Number set to {number}!**")

@client.command()
@has_permissions(administrator=True)
async def start(ctx , lower , upper , prize):
    embed = discord.Embed(
        title="**Guess the Number**" ,
        description=f'''Guess the number between ``{lower}`` and ``{upper}``! :white_check_mark:
Prize:- **{prize}** :moneybag:
Sponsored by :- <@718112706917564466> ''' ,
        color= discord.Color.blue()

    )
    embed.set_footer(text="Guess the Number | Ekamjot#9133")
    await ctx.message.delete()
    await ctx.send(embed=embed)

@client.command()
@has_permissions(administrator=True)
async def unlock(ctx , seconds: int):
    await ctx.message.delete()
    for r in range(seconds):
        await ctx.send(f"Starting in {seconds-r}")
        time.sleep(1)

    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)



@client.command()
@has_permissions(administrator=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role , send_messages=False)
    embed = discord.Embed(
        title="**Channel Locked :lock:**" ,
        color=discord.Color.blue()
    )
    await ctx.message.delete()
    await ctx.send(embed=embed)
    await embed.set_footer(text="Guess the Number | Ekamjot#9133")



@client.event
async def on_message(message):
    await client.process_commands(message)
    with open("gtn_json.json" , "r") as f:
        nu = json.load(f)

        if message.channel.id == 734091229427662932:
            return

        if int(message.content) == nu['number']:
            embed = discord.Embed(
                title="**Game Over!**" ,
                description=f'''Congratulations! {message.author.mention}
You guessed the right number!
You won **25rs** :moneybag:
The number was **{nu['number']}** :white_check_mark:
**DM  <@718112706917564466> to claim your reward!**
''' ,
                color= discord.Color.blue()
            )
            embed.set_footer(text="Guess the Number | Ekamjot#9133")

            chan = client.get_channel(message.channel.id)
            gui = client.get_guild(740542421515108352)

            await message.channel.send(embed=embed)

            await chan.set_permissions(gui.default_role, send_messages=False)
            await message.channel.send("Channel Locked :lock:")


        elif int(message.content) > 3000:
            await message.channel.send(f"{message.author.mention} The number is between ``1-3000``")












client.run("NzM5NDM3MDAxMDczMjI5ODg0.XyacXw.qn1UeHNEviWyMNl9b8ewGt57uSw")
