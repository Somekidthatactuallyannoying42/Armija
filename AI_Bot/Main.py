import discord, random, requests, os
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

async def hello(ctx):
    print(f'We logged as {bot.user}!')
    
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello my n-word{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name = file.filename
            file_url = file.url
            await file.save(f'{file_name}')
            await ctx.send(f'File lu udah di simpen di Banja luka{file_name}')
            hasil = get_class('keras_model.h5', 'labels.txt', file_name)

            if hasil[0] == 'Europe\n' and hasil[1] >= 0.6:
                await ctx.send('This is Europe..')
                await ctx.send('Other information..')
            elif hasil[0] == 'Afrika\n' and hasil[1] >= 0.6:
                await ctx.send('This is Africa..')
                await ctx.send('Other information..')
            elif hasil[0] == 'South American\n' and hasil[1] >= 0.6:
                await ctx.send('This is South American..')
                await ctx.send('Other information..')
            elif hasil[0] == 'Australia\n' and hasil[1] >= 0.6:
                await ctx.send('This is Australia..')
                await ctx.send('Other information..')
            elif hasil[0] == 'Asia\n' and hasil[1] >= 0.6:
                await ctx.send('This is Asia')
                await ctx.send('Other information..')

        else:
            await ctx.send('THIS (RE)TARD IMAGE AINT VALID MATE! >:(')
 

