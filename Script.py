class script(object):
    START_TXT = """๐ ๐ท๐ด๐ป๐พ {}

โ ๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด ๐ธ๐ {}

๐ต๏ธ ๐ธ ๐ฒ๐ฐ๐ฝ ๐ฟ๐๐พ๐๐ธ๐ณ๐ด ๐ผ๐พ๐๐ธ๐ด๐,

โ ๐น๐๐๐ ๐ฐ๐ณ๐ณ ๐ผ๐ด ๐๐พ ๐๐พ๐๐ ๐ถ๐๐พ๐๐ฟ ๐ฐ๐ฝ๐ณ ๐ด๐ฝ๐น๐พ๐ ๐

๐ฎโโ ๐ฒ๐๐ด๐ฐ๐๐พ๐ : <a href=https://t.me/RJMALLU>RJ</a>"""
    HELP_TXT = """๐ท๐ด๐ {}
๐ท๐ด๐๐ด ๐ธ๐ ๐๐ท๐ด ๐ท๐ด๐ป๐ฟ ๐ต๐พ๐ ๐ผ๐ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐."""
    ABOUT_TXT = """โช ๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด : {}

โช ๐ฒ๐๐ด๐ฐ๐๐พ๐ : <a href=https://t.me/RJMALLU>๐๐น</a>

โช ๐ฟ๐๐พ๐ผ๐พ๐๐ธ๐พ๐ฝ : <a href=https://t.me/KAAVAL_KAARAN_tg>MSFA เดเดพเดตเตฝ เดเดพเดฐเตป</a>

โช ๐ป๐ธ๐ฑ๐๐ฐ๐๐ : ๐ฟ๐๐๐พ๐ถ๐๐ฐ๐ผ

โช ๐ป๐ฐ๐ฝ๐ถ๐๐ฐ๐ถ๐ด : ๐ฟ๐๐๐ท๐พ๐ฝ ๐น

โช ๐ณ๐ฐ๐๐ฐ ๐ฑ๐ฐ๐๐ด : ๐ผ๐พ๐ฝ๐ถ๐พ ๐ณ๐ฑ

โช ๐ฑ๐พ๐ ๐๐ด๐๐๐ด๐ : ๐ท๐ด๐๐พ๐บ๐

โช ๐ฑ๐๐ธ๐ป๐ณ ๐๐๐ฐ๐๐๐ : v2.0.1 [ ๐ฑ๐ด๐๐ฐ ]"""
    SOURCE_TXT = """<b>NOTE:</b>
๐เดเดจเตเดคเดพเดเดพ เดฎเตเดจเต เดจเตเดเตเดเตเดจเตเดจเต เดจเดฟเดจเดเตเดเต เดเดตเดถเตเดฏเดฎเดพเดฏเดฟเดเตเดเตเดณเตเดณเดคเต เดเดตเดฟเดเต เดเดฒเตเดฒ ๐
<b>๐ฎโโ แดแดแด สแดแดแดส : </b> <a href=https://t.me/cine_makotta>๐๐น</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
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
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
โข /id - <code>get id of a specified user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    SONG_TXT = """<b>๐ผ๐๐พ๐ฝ๐ถ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ๐ผ</b>
๐๐พ๐ฝ๐ถ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ ๐ผ๐พ๐ณ๐๐ป๐ด, ๐ต๐พ๐ ๐๐ท๐พ๐๐ด ๐๐ท๐พ ๐ป๐พ๐๐ด ๐ผ๐๐๐ธ๐ฒ
<b>๐ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ ๐</b>
- /song ๐๐พ๐๐ ๐๐พ๐ฝ๐ถ ๐ฝ๐ฐ๐ผ๐ด - ๐๐พ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ ๐
<b>๐ถ ๐ด๐๐ฐ๐ผ๐ฟ๐ป๐ด ๐ถ</b>
- /song Naadan Vibe
<b>๐๐๐๐ฐ๐ถ๐ด๐</b>
- ๐ฒ๐ฐ๐ฝ ๐ฑ๐ด ๐๐๐ด๐ณ ๐ฑ๐
- ๐๐พ๐๐บ๐ ๐ธ๐ฝ ๐ฑ๐พ๐ ๐ฟ๐ผ & ๐ฑ๐พ๐ ๐ฐ๐ณ๐ด๐ณ๐ณ ๐ถ๐๐พ๐๐ฟ"""
    CORONA_TXT = """โค ๐๐๐ฅ๐ฉ: ๐ข๐๐๐๐ฝ
๐๐๐๐ ๐ฒ๐๐๐๐๐๐ ๐๐๐๐๐ ๐ข๐๐ ๐๐ ๐๐๐๐  ๐๐๐๐๐ข ๐๐๐๐๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐ 
โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:
โช /covid - ๐๐๐พ ๐๐๐๐ ๐ผ๐๐๐๐บ๐๐ฝ ๐๐๐๐ ๐๐๐๐ ๐ผ๐๐๐๐๐๐ ๐๐บ๐๐พ ๐๐ ๐๐พ๐ ๐ผ๐๐๐๐ฝ๐พ ๐๐๐ฟ๐๐๐๐บ๐๐๐๐
โ๐ค๐๐บ๐๐๐๐พ:
/covid ๐จ๐๐ฝ๐๐บ"""
    TTS_TXT = """Help: <b> TTS ๐ค module:</b>
Translate text to speech
<b>Commands and Usage:</b>
โข /tts <text> : convert text to speech
<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข IMDb can translate texts to 200+ languages."""
    PURGE_TXT = """<b>Purge</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 
โ /purge:- Delete All Messages From The Replied To Message, To The Current Message"""
    PIN_TXT ="""<b>PIN MODULE</b>
<b>๐ฟ๐ธ๐ฝ ๐ฐ ๐ผ๐ด๐๐๐ฐ๐ถ๐ด../</b>
<b>๐ฐ๐ป๐ป ๐๐ท๐ด ๐ฟ๐ธ๐ฝ ๐๐ด๐ป๐ฐ๐๐ด๐ณ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐ ๐ฒ๐ฐ๐ฝ ๐ฑ๐ด ๐ต๐พ๐๐ฝ๐ณ ๐ท๐ด๐๐ด::</b>
<b>๐๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐ ๐ฐ๐ฝ๐ณ ๐๐๐ฐ๐ถ๐ด๐</b>
โ /pin :- ๐๐พ ๐ฟ๐ธ๐ฝ ๐๐ท๐ด ๐ผ๐ด๐๐๐ฐ๐ถ๐ด ๐พ๐ฝ ๐๐พ๐๐ ๐ฒ๐ท๐ฐ๐๐
โ /unpin :- ๐๐พ ๐๐ฝ๐ฟ๐ธ๐ฝ ๐๐ท๐ด ๐ฒ๐๐๐๐ด๐ด๐ฝ๐ ๐ฟ๐ธ๐ฝ๐ฝ๐ด๐ณ ๐ผ๐ด๐๐ฐ๐ฐ๐ถ๐ด"""
    PASTE_TXT = """Help: <b>Paste</b>
Paste some texts or documents on a website!
<b>Commands and Usage:</b>
โข /paste [text] - paste the given text on Pasty
<b>NOTE:</b>
โข These commands works on both pm and group.
โข These commands can be used by any group member."""
    FUN_TXT ="""<b>Gแดแดแดs</b> 
    
<b>โก ๐น๐๐๐ ๐๐พ๐ผ๐ด ๐บ๐ธ๐ฝ๐ณ ๐พ๐ต ๐ต๐๐ฝ ๐๐ท๐ธ๐ฝ๐ถ'๐ โก</b>
 
๐ฃ. /dice - ๐๐พ๐ป๐ด ๐๐ท๐ด ๐ณ๐ธ๐ฒ๐ด 
๐ค. /Throw ๐๐ /Dart - ๐๐พ ๐ผ๐ฐ๐บ๐ด ๐ณ๐ฐ๐๐ 
3. /Runs - ๐๐พ๐ผ๐ด ๐๐ฐ๐ฝ๐ณ๐พ๐ผ ๐ณ๐ธ๐ฐ๐ป๐พ๐ถ๐๐ด๐ 
4. /Goal or /Shoot - ๐๐พ ๐ผ๐ฐ๐บ๐ด ๐ฐ ๐ถ๐พ๐ฐ๐ป ๐พ๐ ๐๐ท๐พ๐พ๐
5. /luck or /cownd - ๐๐ฟ๐ธ๐ฝ ๐ฐ๐ฝ๐ณ ๐๐๐ ๐๐พ๐๐ ๐ป๐๐ฒ๐บ"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details
โข/whois :-give a user full details"""
    TELE_TXT = """<b>โซ๏ธHELP: Telegraphโช๏ธ</b>
Do as you wish with telegra.ph module!
</b>USAGE:</b>
๐คง /telegraph - Send me Picture or Vide Under (5MB)
<b>NOTE:</b>
โข This Command Is Available in goups and pms
โข This Command Can be used by everyone"""
    MAMMOKA_TXT = """๐๐๐๐๐๐๐ : <b>Iแดแดแด Fแดษดs Aสแด Pสแดสษชสษชแดแดแด Nแดแดส Tสษชs แดสแดแด</b> 
    
<b> ๐๐๐ผ๐๐๐: </b>
Tสษชs าษชสแดแดส แดแดษดแดแดษชษดs แดแดxษชแด าแดษดษดส sแดษชแดแดแดสs ๐๐๐
    
<b> ๐พ๐๐๐๐ผ๐๐ฟ: </b>
/ikka โบโบ"""
    STICKER_TXT = """๐๐พ๐ ๐ฒ๐ฐ๐ฝ ๐๐๐ด ๐๐ท๐ธ๐ ๐ผ๐พ๐ณ๐๐ป๐ด ๐๐พ ๐ต๐ธ๐ฝ๐ณ ๐ฐ๐ฝ๐ ๐๐๐ธ๐ฒ๐บ๐ด๐๐ ๐ธ๐ณ.
โข ๐๐๐๐๐
To Get Sticker ID
 
  โญ ๐๐ค๐ฌ ๐๐ค ๐๐จ๐
 
โ Reply To Any Sticker [/stickerid]"""
    FILTER_TXT = """๐ฐ๐ธ๐ผ๐ฟ๐พ๐๐๐ฐ๐ฝ๐ ๐ฝ๐พ๐๐ธ๐ฒ๐ด ๐ต๐พ๐ ๐ผ๐พ๐๐ธ๐ด ๐ถ๐๐พ๐๐ฟ ๐พ๐๐ฝ๐ด๐๐๐ฐ

ษช๊ฐ yแดแดสแด แดแดแดแดแด แดสษช๊ฑ สแดแด ๊ฐแดส แดแดแด ษชแด ษขสแดแดแดฉ yแดแด สแดแด แด แดแด แดแดแด แดแด แดแด แดสแด ษขสแดแดแดฉ แดษดแด แดแดษด'แด ๊ฐแดสษขแดแด แดแด แดษด แดแดแดแด๊ฐษชสแดแดส สแดแดก ๊ฑแดกษชแดแดส แดษด แดแดแดแด๊ฐษชสแดแดส?
แดสษชแดแด แดสแด แดแดxแด แดษดแด แดแดแดฉy ษชแด แดษด yแดแดสแด ษขสแดแดแดฉ :/autofilter on
โ๏ธโ๏ธโ๏ธโ๏ธโ๏ธโ๏ธโ๏ธโ๏ธโ๏ธโ๏ธ
เด เดฌเตเดเตเดเดฟเดจเต เดจเดฟเดเตเดเตพ เดฎเตเดตเดฟ เดฒเดญเดฟเดเตเดเดพเตป เดตเตเดฃเตเดเดฟเดฏเดพ เดเดชเดฏเตเดเดฟเดเตเดเตเดจเตเดจเต เดเดเตเดเดฟเตฝ เดฌเตเดเตเดเดฟเดจเต เดเตเดฐเตเดชเตเดชเดฟเตฝ เดเดกเตเดฎเดฟเตป เดเดเตเดเดฏเตเด
เด เดเดพเดฃเตเดจเตเดจ เดเตเดเตเดธเตเดฑเตเดฑเต เดเตเดฒเดฟเดเตเดเต เดเตเดฏเตเดคเต เดเตเดฐเตเดชเตเดชเดฟเตฝ เดชเตเดธเตเดฑเตเดฑเต เดเตเดฏเตเดฏเตเดเดฏเตเด เดเตเดฏเตเดฏเตเด :
/autofilter on

A lot of People don't know how to Turn on the AutoFilter feature of this Bot.

๐ COMMANDS & USAGE:
- /autofilter on: Send this command in your group to turn on Auto-Filter."""
    STATUS_TXT = """โ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐๐๐ด๐๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐ฒ๐ท๐ฐ๐๐: <code>{}</code>
โ ๐๐๐ด๐ณ ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ
โ ๐ต๐๐ด๐ด ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ"""
    LOG_TEXT_G = """#Home
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#Person
ID - <code>{}</code>
Name - {}
"""
