import discord
from discord.ext import commands
import numpy as np

client=commands.Bot(command_prefix=".")

@client.event
async def on_ready():
	print("The bot is online")


@client.event
async def on_member_join(member):
	ch=await member.create_dm()
	await ch.send(f"Hii"+ member.mention+", to give you access over the channel, I need to see your enrollment ID. Please write '.e' then give a space and then write your enrollment number. Please note that the enrollment number is case sensitive. \n An example will be -> \n .e ABCD123abcd456op")

@client.command()
async def e(ctx,*,enr):
	#print("the command is called by")
	a=ctx.message.author
	#print(a)
	id1= ctx.message.author.id
	#print(id1)
	en=str(enr)
	#print("the entered enrollment is")
	#print(en)
	l=np.load("D:\\ISB2020\\enum.npy")
	if en not in l:
		await ctx.send(f"Sorry mate. Your entered enrollment number"+ en+" is either Invalid or has already been used by someone.")
	else:
		member=ctx.guild.get_member(id1)
		role = discord.utils.get(member.guild.roles, name='accessed')
		await member.add_roles(role)
		print("Role changed to 'accessed'")
		await ctx.send(f" Welcome mate. You got access to all the channels.")
		print(l)
		for a,b in enumerate(l):
			print(b)
			if en==b:
				l[a]="None"
				np.save("D:\\ISB2020\\enum",l)
				print("Saved & loop broken")
				print(l)
				break

client.run("NzU3OTU2MDQwMTU0Mjg0MDcz.X2n7kg.5Nz0c0kuXFeXBxMncjeMa6UxNuY")
