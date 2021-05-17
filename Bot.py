from discord import player
import TicTac
import PlayerTurns
from discord.ext import commands

client = commands.Bot(command_prefix=">")
players = []
gameStarted = False

def playerSymbol():
    if (PlayerTurns.front() == players[0]):
        return "X"
    else:
        return "O"

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def join(ctx):
    global gameStarted

    if (gameStarted):
        await ctx.send("There is currently a game in session")
        return

    if (len(players) <= 0 or players[0] != ctx.author):
        players.append(ctx.author)
        await ctx.send("Lobby capacity: " +str(len(players)) +"/2")
        await ctx.send(ctx.author)
    else:
       await ctx.send("This user has already joined the lobby")

    if (len(players) >= 2):
        gameStarted = True
        PlayerTurns.newList(players)
        
        await ctx.send("The game has started")
        await ctx.send(TicTac.DisplayBoard())


@client.command()
async def place(ctx, args):
    global players
    global gameStarted

    if (ctx.author != PlayerTurns.front()):
        await ctx.send("Either it is not your turn or you are not apart of this game")
        return

    position = int(args)

    if (position >= 0 and position < 9):
        if (TicTac.Place(position, playerSymbol())):

            await ctx.send(TicTac.DisplayBoard())

            if(TicTac.tieGame()):
                await ctx.send("Tie Game")
                TicTac.reset()
                players = []
                gameStarted = False

            if(TicTac.WinCon()):
                await ctx.send(str(ctx.author) +" has won!!!")
                TicTac.reset()
                players = []
                gameStarted = False
            else:
                PlayerTurns.nextTurn()
        else:
            await ctx.send("Position is already filled")
    else:
        await ctx.send("HELP: enter a valid position (0 - 9)")


@client.command()
async def info(ctx):
    await ctx.send(""">place *position*: places a piece at the specific position
>join: joins a new game of tic-tac toe
>boards: displays a leaderboard
Reference Board for positions
https://i.imgur.com/xyiYO8O.png""")

client.run("")
