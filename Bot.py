import aiohttp
from io import BytesIO
from pyrogram import client, filters
from pyrogram. types Message
from Python_ARQ import ARQ


app = Client(
"quote",
bot_token="2019666523:AAGpiM_x86nkNPYdWzzOxuQybgRadksgz1A",
api_id=2019666523,
api_hash="AAGpiM_x86nkNPYdWzzOxuQybgRadksgz1A",
)
ARQ_URL = "http://thearq.tech/"
session = aiohttp.ClientSession()
ARQ_X_API = "VCMTBE-FQVIXC-ZSRMGQ-KAMFYC-ARQ"
arq = ARQ(ARQ_URL, ARQ_X_API, session)

async def quotify(messages: list):
response await arq.quotly(messages)
if not response.ok:
return [False, response.result]
sticker
response.result
sticker BytesIO(sticker)
sticker.name = "dwaboss.webp"
return [True, sticker]
else msg
def get_arg(message):
msg message. text
msg =
msg.replace(" 1) if msg[1] =
split msg[1:).replace("\n", \n").split("")
if " ".join( split[1:]).strip().
return
return
".join( split[1:])
III
def intarg(message: Message) -> bool:
count = get_arg(message)
try:
count = int(count)
return [True, count]
except ValueError:
return [False, 0]

@app.on_message(filters.command("dwa"))
async def quotebot(_, message):
  
  if not message.reply_to_message:
return await message.reply_text(
"Mesajı yanıtlayın sticker edim."

)

if not message.reply_to_message.text:
return await message.reply_text(
"Yanıtladığınız mesaj deyil şəkildir. və mən bunu sticker edə bilmərəm."


m = await message.reply_text("Stickerə çevirilir.")
if len(message.command) < 2:
messages = [message.reply_to_message]
elif len(message.command) == 2:
arg = intarg(message)
if arg[0]:
if arg[1] < 2 or arg[1] > 10:
return await m.edit("2-10 arası edə bilərəm yalnız.")
count = arg[1]
messages = await client.get_messages
message.chat.id,
[
for i in rangeſ
message.reply_to_message.message_id,
message.reply_to_message.message_id + count,
)
],
replies=0,
)
else:
if get_arg(message) != "r":
return await m.edit
"Yazdığınızı anlamadım, 'r' or 'INT', EX: /q 2"
)
reply_message = await client.get_messages,
message.chat.id,
message.reply_to_message.message_id,
replies=1,
)
messages [reply_message]

else:
  await m.edit(
    "Yazdığınız anlaşılmadı zəhmət olmasa düzgün əmrlərdən istifadə edin"
    )
    return
  try:
    sticker = await quotify(messages)
    if not sticker[0]:
      await message.reply_text(stciker[1])
      return await m.delete()
      sticker = sticker[1]
      await message.reply_sticker(stciker)
      await m.delete()
      sticker.close()
      except:
        await m.edit(
          "Stickerə çevirən zaman xəta baş verdi,"
          + " xəta a "
          + "Mesajı çevirən zaman xəta baş verdi."
          )
          
          app.run()