import discord
from discord.ext import commands
from core.classes import Cog_Extension
import yt_dlp as youtube_dl
from discord.utils import get
import asyncio
import json
import os

# 這邊可以使用Cog功能繼承基本屬性
class music(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['p', 'play'])
    @commands.is_owner()
    async def _play(self, ctx, url: str):
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        global url1
        global title
        url1 = url
        channel = ctx.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if channel:
            if not voice:
                voice = await channel.connect()
        else:
            return await ctx.channel.send(f"你沒連進去語音頻道")
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        url = (f"{url1}")
        download(url1)
        for file in os.listdir("./"):
            if file.endswith(".json"):
                if not voice.is_playing():
                    with open('playlist.json', 'r+') as jf:
                        showinfo()
                        print("我是一號測試點")
                        data = json.load(jf)
                        temp = data["Music"]
                        nowurl = {"Title": f"{title}" + f" [{id}]"}
                        temp.append(nowurl)
                        write_json(data)
                        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)


        if voice.is_playing():
            with open('playlist.json', 'r+') as jf:
                showinfo()
                data = json.load(jf)
                temp = data["Music"]
                queueurl = {"Title": f"{title}" + f" [{id}]"}
                temp.append(queueurl)
                write_json(data)
        else:

            with open('playlist.json', 'r+') as jf:
                showinfo()
                voice.play(discord.FFmpegPCMAudio(f"{data['Music'][0]['Title']}.mp3"), after = lambda e : play_next(ctx, self))
                voice.is_playing()
        
        if voice.disconnect():
            with open('playlist.json', 'r+') as jf:
                showinfo()
                data = json.load(jf)
                del data['Music']



    @commands.command(pass_context=True, brief="重播暫停音樂", aliases=['resume'])
    async def _resume(self, ctx):
        channel = ctx.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if not voice.is_playing():
            voice.resume()
            await ctx.channel.send("開始音樂!")

    @commands.command(pass_context=True, brief="暫停音樂", aliases=['pause'])
    async def _pause(self, ctx):
        channel = ctx.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice.is_playing():
            voice.pause()
            await ctx.channel.send("已暫停音樂!")

    @commands.command(pass_context=True, brief="跳過音樂", aliases=['skip'])
    async def _skip(self, ctx):
        channel = ctx.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        voice.pause()
        play_next(self, ctx)

def play_next(self, ctx):
    global source
    with open('playlist.json', 'r+') as jf:
        queues = json.load(jf)
        if len(queues['Music']) >= 2:
            del queues['Music'][0]
            print(queues['Music'][0]['Title'], "new_song")
            showinfo()
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
            voice.play(discord.FFmpegPCMAudio(f"{queues['Music'][0]['Title']}.mp3"), after = lambda e : play_next(ctx, self))
            voice.is_playing()


def showinfo():
    print("我是二號測試點")
    ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url1, download=False)
        global title
        title = info['title']
        global id
        id = info['id']


def download(url):
    ydl_opts = {
        'format' : 'bestaudio/best',
        "postprocessors": 
        [{"key" : "FFmpegExtractAudio", "preferredcodec" : "mp3", "preferredquality" : "192"}],   
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

def write_json(data, filename="playlist.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def setup(bot):
    bot.add_cog(music(bot))
