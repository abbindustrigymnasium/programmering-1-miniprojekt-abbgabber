# HypixelAPI
### W.I.P Preview
![Preview](https://i.gyazo.com/ab4aa31a70a7f64dfa2498e12c698021.jpg)

## Projektet

Jag spelar ofta minecraft på Hypixel Skyblock vilket är en server där det finns olika sorters items med olika stats. Servern har en API där man kan hämta nästan allt om spelaren som vapen, pengar, lagmedlemmar etc. Därför vill jag göra en hemsida, i HTML, där man kan se alla spelarans bl.a. stats och items.

Hypixel har en egen API för alla sorters stats på hela deras nätverk däremot är den kass och det finns inte särskilt mycket dokumentation om den så därför använder jag, utöver deras api, Slothpixel API som en annan person har gjort som är mycket enklare att använda.
Hypixels API använder jag för att ta reda på id:erna till profilerna som man har och efter det använder jag Slothpixel API för att ta reda på info om profilen. För att göra det med Hypixel API:en så måste man decode all data från, tror det var, Base64 vilket gör hela proccessen onödigt komplicerat.

Efter att jag har fått datan för profilen så vill jag visa itemsen som spelaren har ungefär på samma sätt som det gör i minecraft själva med att när man håller över ikonen av itemet så visas deras stats m.m. (se bifogad bild). Det vore också ganska häftigt om jag skulle kunna lägga till så att man skulle kunna se massor med andra grejer utöver items som t.ex. spelarens combat skill eller pets.

För att göra sidan mindre tom så finns det också en bild på spelarens avatar, en egen backgrunds bild och en ikon för de flesta olika items som finns i spelet.

#### ex. Hypixel API : https://api.hypixel.net/player?key=d4eaf4e7-23aa-4196-9440-fe9af430f614&name=Stranght
#### ex Slothpixel API : https://api.slothpixel.me/api/skyblock/profile/Stranght/23a72998770e4614b230a15a282c967e


### W.I.P Preview
![Preview](https://i.gyazo.com/ab4aa31a70a7f64dfa2498e12c698021.jpg)

#### Items i spelet
![items](https://i.gyazo.com/7f3d489ceece92c5b9ecda38fcc1b74c.png)

## Syfte

Syftet är att jag ska bli bättre på att använda mig utav API:er och hur de kan användes i ett mer generellt syfte. 
