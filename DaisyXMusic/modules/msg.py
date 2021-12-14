# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from DaisyXMusic.config import SOURCE_CODE
from DaisyXMusic.config import ASSISTANT_NAME
from DaisyXMusic.config import PROJECT_NAME
from DaisyXMusic.config import SUPPORT_GROUP
from DaisyXMusic.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**Salam 👋 [{}](tg://user?id={})!**\n\n🤖 Mənə Səsli çatlarda Musiqi oxumaq və Teleqram qruplarına xoş gəlmisiniz\n\n✅ Mənə  /help Yazaraq məlumat ala bilərsiniz."
      HELP_MSG = [
        ".",
f"""
**Hey ♪ xoş gəlmisiniz {PROJECT_NAME}

⚪️ {PROJECT_NAME} qrup səsli söhbətinizdə və kanal səsli söhbətinizdə musiqi oxuya bilər

⚪️ Assistant Adı >> @{ASSISTANT_NAME}\n\nClick next for instructions**
""",

f"""
**Tənzimləmə**

1) Bot admini olun (cplay istifadə edirsinizsə qrupda və kanalda)
2) səsli söhbətə başlayın
3) bir admin tərəfindən ilk dəfə [mahnı adı] cəhd edin/oynayın
* ) Əgər Userbot qoşulubsa, musiqidən həzz alın, əks halda qrupunuza qoşulun @{ASSISTANT_NAME} əlavə edin və yenidən cəhd edin

** Kanal musiqisinin səsləndirilməsi üçün**
1) meni kanalina admin et
2) Əlaqəli qrupda / userbotjoinchanneldə təqdim edin
3) İndi əlaqəli qrupda əmrlər göndərin
""",
f"""
**Əmrlər**

**=>> Mahnı Oynat 🎧**

- /oynat: musiqiyə başlayır
- /oynat: [yt url] : Göstərdiyiniz Yt url-ni təyin etsəniz, o işləyəcək.
- /oynat: [reply yo audio]: istənilən musiqini axtara bilərsiniz
- /dplay: Deezer-dən musiqi
- /splay: sp Musiqinizi platformadan başlayır
- /ytplay: Youtube-dan Musiqi Oynadır

**=>> Oynatma ⏯**

- /player: Musiqi Menyu Açılır
- /skip: musiqini atlayırsan
- /pause: musiqi dayanır
- /resume: musiqi davam edir
- /end: media musiqisini dayandırın
- /current: Cari ifa olunan treki göstərir
- /playlist: Pleylist göstərir

*Player cmd ve /play, /current ve /playlist yalnız qrupun adminləri istisna olmaqla, bütün digər cmd.
""",

f"""
**=>> Kanal Musiqi Oynamaq 🛠**

✔ Yalnız əlaqəli qrup adminləri üçün:

- /cplay [mahnı adı] - istədiyiniz mahnını çalın
- /cdplay [mahnı adı] - istədiyiniz mahnını deezer vasitəsilə səsləndirin
- /csplay [mahnı adı] - jio saavn vasitəsilə istənilən mahnını səsləndirin
- /cplaylist-indi pleylist göstər
- /cccurrent-show indi oynayır
- /cplayer-açıq musiqi pleyeri parametrləri paneli
- /cpause-fasilə mahnının oxudulması
- /cresume-mahnı çalmağa davam edin
- /cskıp-növbəti mahnını çalın
- /cend-stop musiqi çalın
- /userbotjoinchannel- köməkçinizi söhbətinizə dəvət edin

Kanal c yerinə də istifadə edilə bilər (/cplay = / channelplay )

⚪️ Əgər belə oynamırsansa, ortaq qrupda :

1) kanal identifikatorunuzu alın.
2) Başlığı ilə qrup yaradın: Kanal musiqisi: kanalınızın_id
3) tam icazə ilə botu kanal meneceri kimi əlavə edin
4) @{ASSISTANT_NAME} adlı şəxsi kanala admin kimi əlavə edin.
5) sadəcə qrupunuza əmrlər göndərin. (əvəzinə /ytplay /play istifadə etməyi unutmayın)
""",

f"""
**=>> daha çox alət 🧑🔧**

- /musicplayer [on / off]: musiqi pleyeri aktivləşdirin/deaktiv edin
- /admincache: Qrupunuzun admin məlumatlarını yeniləyir. Botun admin tərəfindən tanınmadığı halda cəhd edin
- /userbotjoin: @{ASSISTANT_NAME} istifadəçini söhbətinizə dəvət edin
""",
f"""
**=>> Mahnı Yüklə 🎸**

- /video [mahnı adı]: youtube-dan video mahnı yükləmək
- /mahnı [mahnı adı]: youtube-dan audio mahnı yükləmək
- /saavn [mahnı adı]: saavn-dan mahnıları endir
- /deezer [mahnı adı]: deeze-dən mahnı yükləmək

**=>> Axtarış alətləri 📄**

- /search [mahnı adı]: mahnıları YouTube-da axtarın
- /lyrics lyrics [mahnı adı]: Lyrics alın
""",

f"""
**=>> Sudo istifadəçiləri üçün əmrlər:**

 - /userbotleaveall-Assistenti bütün söhbətlərdən silin
 - /yayım <Mesajı cavablandır> - bütün çatlara cavab mesajını qlobal olaraq yayımlayın
 - /pmpermit [on/off] - pmpermit mesajını aktivləşdirin/deaktiv edin
*sudo istifadəçiləri istənilən qrupda istənilən əmri işlədə bilərlər

"""
      ]
