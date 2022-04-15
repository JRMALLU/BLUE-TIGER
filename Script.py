class script(object):
    START_TXT = """👋 𝙷𝙴𝙻𝙾 {}

⎆ 𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 {}

🕵️ 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂,

➕ 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍

👮‍♂ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 : <a href=https://t.me/RJMALLU>RJ</a>"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✪ 𝙼𝚈 𝙽𝙰𝙼𝙴 : {}

✪ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 : <a href=https://t.me/RJMALLU>𝚁𝙹</a>

✪ 𝙿𝚁𝙾𝙼𝙾𝚃𝙸𝙾𝙽 : <a href=https://t.me/KAAVAL_KAARAN_tg>MSFA കാവൽ കാരൻ</a>

✪ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈 : 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼

✪ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹

✪ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴 : 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱

✪ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁 : 𝙷𝙴𝚁𝙾𝙺𝚄

✪ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂 : v2.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
👋എന്താടാ മോനെ നോക്കുന്നേ നിനക്ക് ആവശ്യമായിട്ടുള്ളത് ഇവിടെ ഇല്ല 😌
<b>👮‍♂ ᴅᴇᴠʟᴏᴘᴇʀ : </b> <a href=https://t.me/cine_makotta>𝚁𝙹</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    SONG_TXT = """<b>🎼𝚂𝙾𝙽𝙶 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳🎼</b>
𝚂𝙾𝙽𝙶 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝙾𝙳𝚄𝙻𝙴, 𝙵𝙾𝚁 𝚃𝙷𝙾𝚂𝙴 𝚆𝙷𝙾 𝙻𝙾𝚅𝙴 𝙼𝚄𝚂𝙸𝙲
<b>🎈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 🎈</b>
- /song 𝚈𝙾𝚄𝚁 𝚂𝙾𝙽𝙶 𝙽𝙰𝙼𝙴 - 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 😁
<b>🎶 𝙴𝚇𝙰𝙼𝙿𝙻𝙴 🎶</b>
- /song Naadan Vibe
<b>🌀𝚄𝚂𝙰𝙶𝙴🌀</b>
- 𝙲𝙰𝙽 𝙱𝙴 𝚄𝚂𝙴𝙳 𝙱𝚈
- 𝚆𝙾𝚁𝙺𝚂 𝙸𝙽 𝙱𝙾𝚃 𝙿𝙼 & 𝙱𝙾𝚃 𝙰𝙳𝙴𝙳𝙳 𝙶𝚁𝙾𝚄𝙿"""
    CORONA_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖢𝗈𝗏𝗂𝖽
𝚃𝚑𝚒𝚜 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚔𝚗𝚘𝚠 𝚍𝚊𝚒𝚕𝚢 𝚒𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗 𝚊𝚋𝚘𝚞𝚝 𝚌𝚘𝚟𝚒𝚍 
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪ /covid - 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾 𝗍𝗈 𝗀𝖾𝗍 𝖼𝗈𝗏𝗂𝖽𝖾 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇
➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
/covid 𝖨𝗇𝖽𝗂𝖺"""
    TTS_TXT = """Help: <b> TTS 🎤 module:</b>
Translate text to speech
<b>Commands and Usage:</b>
• /tts <text> : convert text to speech
<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• IMDb can translate texts to 200+ languages."""
    PURGE_TXT = """<b>Purge</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 
◉ /purge:- Delete All Messages From The Replied To Message, To The Current Message"""
    PIN_TXT ="""<b>PIN MODULE</b>
<b>𝙿𝙸𝙽 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴../</b>
<b>𝙰𝙻𝙻 𝚃𝙷𝙴 𝙿𝙸𝙽 𝚁𝙴𝙻𝙰𝚃𝙴𝙳 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙲𝙰𝙽 𝙱𝙴 𝙵𝙾𝚄𝙽𝙳 𝙷𝙴𝚁𝙴::</b>
<b>📌𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴📌</b>
◉ /pin :- 𝚃𝙾 𝙿𝙸𝙽 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙾𝙽 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝚃𝚂
◉ /unpin :- 𝚃𝙾 𝚄𝙽𝙿𝙸𝙽 𝚃𝙷𝙴 𝙲𝚄𝚁𝚁𝙴𝙴𝙽𝚃 𝙿𝙸𝙽𝙽𝙴𝙳 𝙼𝙴𝚂𝙰𝙰𝙶𝙴"""
    PASTE_TXT = """Help: <b>Paste</b>
Paste some texts or documents on a website!
<b>Commands and Usage:</b>
• /paste [text] - paste the given text on Pasty
<b>NOTE:</b>
• These commands works on both pm and group.
• These commands can be used by any group member."""
    FUN_TXT ="""<b>Gᴀᴍᴇs</b> 
    
<b>⚡ 𝙹𝚄𝚂𝚃 𝚂𝙾𝙼𝙴 𝙺𝙸𝙽𝙳 𝙾𝙵 𝙵𝚄𝙽 𝚃𝙷𝙸𝙽𝙶'𝚂 ⚡</b>
 
𝟣. /dice - 𝚁𝙾𝙻𝙴 𝚃𝙷𝙴 𝙳𝙸𝙲𝙴 
𝟤. /Throw 𝗈𝗋 /Dart - 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙳𝙰𝚁𝚃 
3. /Runs - 𝚂𝙾𝙼𝙴 𝚁𝙰𝙽𝙳𝙾𝙼 𝙳𝙸𝙰𝙻𝙾𝙶𝚄𝙴𝚂 
4. /Goal or /Shoot - 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙰 𝙶𝙾𝙰𝙻 𝙾𝚁 𝚂𝙷𝙾𝙾𝚃
5. /luck or /cownd - 𝚂𝙿𝙸𝙽 𝙰𝙽𝙳 𝚃𝚁𝚈 𝚈𝙾𝚄𝚁 𝙻𝚄𝙲𝙺"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details
•/whois :-give a user full details"""
    TELE_TXT = """<b>▫️HELP: Telegraph▪️</b>
Do as you wish with telegra.ph module!
</b>USAGE:</b>
🤧 /telegraph - Send me Picture or Vide Under (5MB)
<b>NOTE:</b>
• This Command Is Available in goups and pms
• This Command Can be used by everyone"""
    MAMMOKA_TXT = """𝐂𝐀𝐔𝐓𝐈𝐎𝐍 : <b>Iᴋᴋᴀ Fᴀɴs Aʀᴇ Pʀᴏʜɪʙɪᴛᴇᴅ Nᴇᴀʀ Tʜɪs ᴀʀᴇᴀ</b> 
    
<b> 𝙍𝙀𝘼𝙎𝙊𝙉: </b>
Tʜɪs ғɪʟᴛᴇʀ ᴄᴏɴᴛᴀɪɴs ᴛᴏxɪᴄ ғᴜɴɴʏ sᴛɪᴄᴋᴇʀs 😂😂😂
    
<b> 𝘾𝙊𝙈𝙈𝘼𝙉𝘿: </b>
/ikka ☺☺"""
    STICKER_TXT = """𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚃𝙾 𝙵𝙸𝙽𝙳 𝙰𝙽𝚈 𝚂𝚃𝙸𝙲𝙺𝙴𝚁𝚂 𝙸𝙳.
• 𝐔𝐒𝐀𝐆𝐄
To Get Sticker ID
 
  ⭕ 𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
 
◉ Reply To Any Sticker [/stickerid]"""
    FILTER_TXT = """🔰𝙸𝙼𝙿𝙾𝚁𝚃𝙰𝙽𝚃 𝙽𝙾𝚃𝙸𝙲𝙴 𝙵𝙾𝚁 𝙼𝙾𝚅𝙸𝙴 𝙶𝚁𝙾𝚄𝙿 𝙾𝚆𝙽𝙴𝚁𝚂🔰

ɪꜰ yᴏᴜʀᴇ ᴀᴅᴅᴇᴅ ᴛʜɪꜱ ʙᴏᴛ ꜰᴏʀ ᴍᴏᴠɪᴇ ɢʀᴏᴜᴩ yᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴩ ᴀɴᴅ ᴅᴏɴ'ᴛ ꜰᴏʀɢᴇᴛ ᴛᴏ ᴏɴ ᴀᴜᴛᴏꜰɪʟᴛᴇʀ ʜᴏᴡ ꜱᴡɪᴛᴄʜ ᴏɴ ᴀᴜᴛᴏꜰɪʟᴛᴇʀ?
ᴄʟɪᴄᴋ ᴛʜᴇ ᴛᴇxᴛ ᴀɴᴅ ᴄᴏᴩy ɪᴛ ᴏɴ yᴏᴜʀᴇ ɢʀᴏᴜᴩ :/autofilter on
➖️➖️➖️➖️➖️➖️➖️➖️➖️➖️
ഈ ബോട്ടിനെ നിങ്ങൾ മൂവി ലഭിക്കാൻ വേണ്ടിയാ ഉപയോഗിക്കുന്നെ എങ്കിൽ ബോട്ടിനെ ഗ്രൂപ്പിൽ അഡ്മിൻ ആകുകയും
ഈ കാണുന്ന ടെക്സ്റ്റ് ക്ലിക്ക് ചെയ്ത് ഗ്രൂപ്പിൽ പേസ്റ്റ് ചെയ്യുകയും ചേയ്യുക :
/autofilter on

A lot of People don't know how to Turn on the AutoFilter feature of this Bot.

📚 COMMANDS & USAGE:
- /autofilter on: Send this command in your group to turn on Auto-Filter."""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#Home
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#Person
ID - <code>{}</code>
Name - {}
"""
