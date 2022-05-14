import datetime, time, asyncio, keyboard

# only for testing purposes (sees how the emoji and text would respond to all the unix times.)
def test():
    for unixtimestamp in range(0, 86400):
        if unixtimestamp % 60 == 0:
            dt = datetime.datetime.fromtimestamp(unixtimestamp)
            print(f"{get_emoji(dt)} It's {get_timestamp(dt)}")

#scheduling start of minute async event
async def at_minute_start():
    while True:
        now = datetime.datetime.now()
        after_minute = now.second + now.microsecond / 1_000_000
        if after_minute:
            await asyncio.sleep(60-after_minute)
        send_time_message()


def send_time_message():
    print("Sending message to change nickname...")
    now = datetime.datetime.now()
    nick(f"{get_emoji(now)} It's {get_timestamp(now)}")
    
    
#change the nickname by typing the command in
def nick(nick):
    keyboard.write(f"/nick {nick}")
    keyboard.press_and_release("Enter")

#Get human readable timestamp of DT object
def get_timestamp(dt):
    if dt.minute == 0:
        if dt.hour == 0:
            return "Midnight"
        if dt.hour == 12:
            return "Noon"
        return f"{dt.hour%12}'o Clock"
    
    minute = dt.minute
    if len(str(minute)) == 1:
        minute = "0" + str(dt.minute)
    return f"{12 if dt.hour == 12 else dt.hour%12}:{minute} {'PM' if dt.hour>=12 else 'AM'}"

#Get emoji of DT object
def get_emoji(dt):
    emojis = "🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦"

    if dt.minute <= 15:
        return emojis[2 * (dt.hour%12) ]
    if dt.minute > 15 and dt.minute <= 45:
        return emojis[2 * (dt.hour%12) + 1]
    try:
        return emojis[2 * (dt.hour%12) + 2]
    except IndexError:
        return emojis[0]


print("The application will automatically start in 5 seconds, press CTRL+C on the terminal to stop.")

#initial delay, then create async task, and run the loop forever
#TODO add keyboard shortcut to stop this.

time.sleep(5)

loop = asyncio.get_event_loop()
loop.create_task(at_minute_start())
loop.run_forever()

#test()


#made by PreciousWarrior
