"""A wrapper for discord.Embed to aid in creating nice-looking messages using
link-less embeds.
"""
from nextcord import Embed, Colour

JukeBot_Bluegreen = Colour.from_rgb(6, 227, 164)

uiEmoji = {
    #Reason      Which emoji to use      The colour of the accent on the left
    "Warn"    : [":warning:",            Colour.yellow()],
    "Error"   : [":no_entry_sign:",      Colour.red()],
    "Playing" : [":arrow_forward:",      JukeBot_Bluegreen],
    "Queued"  : [":speech_balloon:",     JukeBot_Bluegreen],
    "Version" : [":green_heart:",        JukeBot_Bluegreen],
    "Help"    : [":woman_technologist:", JukeBot_Bluegreen],
    "Skip"    : [":track_next:",         JukeBot_Bluegreen],
    "Debug"   : [":gear:",               Colour.lighter_grey()]
}

def DialogBox(messageEmoji, messageTitle, messageContent=False):
    """Creates a nice-looking dialog box using Discord's native embeds.
    TODO: Change to a class?"""
    title = f"{uiEmoji[messageEmoji][0]}  {messageTitle}"
    colour = uiEmoji[messageEmoji][1]

    if not messageContent: # If the dialog box was called without any message content, just a title and an emoji...
        embed = Embed(title = title,
                      colour = colour)
    else: # If we got an emoji, a title, _and_ message text.
        embed = Embed(title = title,
                      description = messageContent,
                      colour = colour)
    return embed
