import discord, asyncio, random
from discord.ext import commands

client = commands.Bot(command_prefix = ".")

   
@client.command(aliases = ["bj"])
async def blackjack(self, ctx):
    if not ctx.guild:
        return await ctx.send("You cannot use this commands in dms")


    #First Embed
    blackjack_embed = discord.Embed(
        title = f"{ctx.author.name} | Charlitan Blackjack",
        description = "type `hit` to get another card. type `stand` to stand or some shit i dont know blackjack terms lol. type `end` to end the game",
        color = 0xFF272A
    )
    blackjack_embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/857774570290020383/858016747373854760/Las_Vegas_0_535829219.png")

    #Types and lists
    icons = [
        ":diamonds:",
        ":heart:",
        ":spades:",
        ":clubs:"
    ]

    hands = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    #Random Choice icons
    random_icon_author = random.choice(icons)
    random_icon_dealer = random.choice(icons)

    #Hands
    dealer_cards_score = 0
    author_cards_score = 0

    dealer_cards_display_first = ""
    author_cards_display_first = ""


    #First Random Cards
    first_hand_author = random.choice(hands)
    first_hand_dealer = random.choice(hands)

    #First Hand Author
    if first_hand_author == "J" or first_hand_author == "Q" or first_hand_author == "K":
        author_cards_score += 10
    else:
        author_cards_score += first_hand_author

    author_cards_display_first += f"{random_icon_author}**{first_hand_author}**"


    #First Hand Dealer
    if first_hand_dealer == "J" or first_hand_dealer == "Q" or first_hand_dealer == "K":
        dealer_cards_score += 10
    else:
        dealer_cards_score += first_hand_dealer

    dealer_cards_display_first += f"{random_icon_dealer}**{first_hand_dealer}**" #Don't Display until end


    blackjack_embed.add_field(name = f"{ctx.author.name}'s Hand", value = f"{author_cards_display_first}\nTotal: {author_cards_score}", inline = True)
    blackjack_embed.add_field(name = f"Dealers Hand", value = "[?]\nTotal: ?", inline = True) #Dealers first mystery hand - edit later


    edit1 = await ctx.send(embed = blackjack_embed)

    #Dealer Loopable Mystery
    dealer_display_hand = "[?]" #SOME CARDS ARENT SHOWING UP FIX LATER
    dealer_mystery_number = 0


    #Code
    while True:


        #Looped embed
        looped_embed = discord.Embed(
            title = f"{ctx.author.name} | Charlitan Blackjack",
            description = "type `hit` to get another card. type `stand` to stand or some shit i dont know blackjack terms lol. type `end` to end the game",
            color = 0xFF272A
        )
        looped_embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/857774570290020383/858016747373854760/Las_Vegas_0_535829219.png")

        #Looped icon
        looped_icon_author = random.choice(icons)
        looped_icon_dealer = random.choice(icons)


        #Looped hands
        random_hand_author = random.choice(hands)
        random_hand_dealer = random.choice(hands)




        #Wait For
        try:
            message1 = await self.client.wait_for("message", check = lambda m: m.author.id == ctx.author.id and m.channel.id == ctx.channel.id, timeout = 40)
        except asyncio.TimeoutError:
            no_time = discord.Embed(
                title = "You ran out of time.",
                color = discord.Color.red()
            )
            return await edit1.edit(embed = no_time)

        if message1.content.lower() == "hit":

            #Checks
            if random_hand_author == "J" or random_hand_author == "Q" or random_hand_author == "K":
                author_cards_score += 10
            else:
                author_cards_score += random_hand_author

            author_cards_display_first += f"{looped_icon_author}**{random_hand_author}**"

            if dealer_cards_score > author_cards_score and dealer_cards_score <= 21:
                pass
            else:


                if random_hand_dealer == "J" or random_hand_dealer == "Q" or random_hand_dealer == "K":
                    dealer_mystery_number += 10
                    harder_npc = 10
                else:
                    dealer_mystery_number += random_hand_dealer
                    harder_npc = random_hand_dealer



                dealer_cards_score += dealer_mystery_number
                if dealer_cards_score > 21:
                    dealer_cards_score -= harder_npc



                dealer_cards_display_first += f"{looped_icon_dealer}**{random_hand_dealer}**"
                dealer_display_hand += f"{looped_icon_dealer}**{random_hand_dealer}**"




        elif message1.content.lower() == "stand":
            if author_cards_score < dealer_cards_score and dealer_cards_score <= 21:
                looped_embed.add_field(name = f"**--YOU LOST--**", value = f"{author_cards_display_first}\nTotal: {author_cards_score}", inline = True)
                looped_embed.add_field(name = f"Dealers Hand", value = f"{dealer_cards_display_first}\nTotal: {dealer_cards_score}", inline = True)
                looped_embed.set_image(url = "https://cdn.discordapp.com/attachments/857774570290020383/858103079232340049/image0.png")
                return await edit1.edit(embed = looped_embed)

            elif author_cards_score > dealer_cards_score and author_cards_score <= 21:
                second_wind_dealer = random.choice(hands)
                if second_wind_dealer == "J" or second_wind_dealer =="Q" or second_wind_dealer =="K":
                    dealer_cards_score += 10
                    dealer_mystery_number += 10
                else: 
                    dealer_cards_score += second_wind_dealer
                    dealer_mystery_number += second_wind_dealer

                dealer_cards_display_first += f"{looped_icon_dealer}**{second_wind_dealer}**"
                dealer_display_hand += f"{looped_icon_dealer}**{second_wind_dealer}**"


                if author_cards_score > dealer_cards_score and author_cards_score <= 21:
                    looped_embed.add_field(name = f"**--YOU WIN--**", value = f"{author_cards_display_first}\nTotal: {author_cards_score}", inline = True)
                    looped_embed.add_field(name = f"Dealers Hand", value = f"{dealer_cards_display_first}\nTotal: {dealer_cards_score}", inline = True)
                    return await edit1.edit(embed = looped_embed)

                elif author_cards_score < dealer_cards_score and dealer_cards_score <= 21:
                    looped_embed.add_field(name = f"**--YOU LOSE--**", value = f"{author_cards_display_first}\nTotal: {author_cards_score}", inline = True)
                    looped_embed.add_field(name = f"Dealers Hand", value = f"{dealer_cards_display_first}\nTotal: {dealer_cards_score}", inline = True)
                    looped_embed.set_image(url = "https://cdn.discordapp.com/attachments/857774570290020383/858103079232340049/image0.png")
                    return await edit1.edit(embed = looped_embed)




        elif message1.content.lower() == "end":
            ended = discord.Embed(
                title = "The game has ended",
                color = 0xFF272A
            )
            ended.set_image(url = "https://cdn.discordapp.com/attachments/857774570290020383/858016747373854760/Las_Vegas_0_535829219.png")
            return await ctx.send(embed = ended)

        else:
            await ctx.send("That isn't valid")
            continue

        await message1.delete()

        #Draw - Both Bust (DRAW)
        if author_cards_score > 21 and dealer_cards_score > 21:
            looped_embed.add_field(name = f"**--A DRAW--**", value = f"{author_cards_display_first}\nTotal: {author_cards_score}", inline = True)
            looped_embed.add_field(name = f"Dealers Hand", value = f"{dealer_cards_display_first}\nTotal: {dealer_cards_score}", inline = True)
            return await edit1.edit(embed = looped_embed)


        #Draw - Both Draw 21 (DRAW)
        if author_cards_score == 21 and dealer_cards_score == 21:
            looped_embed.add_field(name = f"**--A DRAW--**", value = f"{author_cards_display_first}\nTotal: {author_cards_score}", inline = True)
            looped_embed.add_field(name = f"Dealers Hand", value = f"{dealer_cards_display_first}\nTotal: {dealer_cards_score}", inline = True)
            return await edit1.edit(embed = looped_embed)


        #Bust - Author (LOST)
        if author_cards_score > 21:
            looped_embed.add_field(name = f"**--YOU LOST--**", value = f"{author_cards_display_first}\nTotal: {author_cards_score}", inline = True)
            looped_embed.add_field(name = f"Dealers Hand", value = f"{dealer_cards_display_first}\nTotal: {dealer_cards_score}", inline = True)
            looped_embed.set_image(url = "https://cdn.discordapp.com/attachments/857774570290020383/858103079232340049/image0.png")
            return await edit1.edit(embed = looped_embed)

        #Bust - Dealer (WIN)
        if dealer_cards_score > 21:
            looped_embed.add_field(name = f"**--YOU WIN--**", value = f"{author_cards_display_first}\nTotal: {author_cards_score}", inline = True)
            looped_embed.add_field(name = f"Dealers Hand", value = f"{dealer_cards_display_first}\nTotal: {dealer_cards_score}", inline = True)
            return await edit1.edit(embed = looped_embed)




        looped_embed.add_field(name = f"{ctx.author.name}'s Hand", value = f"{author_cards_display_first}\nTotal: {author_cards_score}", inline = True)
        looped_embed.add_field(name = f"Dealer's Hand", value = f"{dealer_mystery_number}\nTotal: ? + {dealer_mystery_number}", inline = True)
        await edit1.edit(embed = looped_embed)
            
            

            



            
