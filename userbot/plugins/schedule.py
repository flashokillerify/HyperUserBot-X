from asyncio import sleep


@bot.on(admin_cmd(pattern="schd (\d*) (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="schd (\d*) (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    cat = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = cat[1]
    ttl = int(cat[0])
    try:
        await event.delete()
    except:
        pass
    await sleep(ttl)
    await event.respond(message)


CMD_HELP.update(
    {
        "schedule": "__**PLUGIN NAME :** Schedule__\
    \n\nš** CMD ā„** `.schd` <time_in_seconds>  <message to send>\
    \n**USAGE   ā„  **Send you the given message after that particular time\
    "
    }
)
