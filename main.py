import colorsys

xkoor1, ykoor1 = 10, 10
xkoor2, ykoor2 = 55, 10
xkoor3, ykoor3 = 10, 55
xkoor4, ykoor4 = 55, 55

bredde = 35
hoyde = 35

mainfill = "#ff4444"

fill1 = mainfill
fill2 = "#ffff44"
fill3 = "#44ffff"
fill4 = "#4444ff"




svgstreng = f"""<svg viewBox="0 0 100 100" width="500mm" height="500mm" xmlns="http://www.w3.org/2000/svg">
 <rect x="0" y="0" width="100%" height="100%" fill="white" />
 <rect x="{xkoor1}" y="{ykoor1}" width="{bredde}" height="{hoyde}" stroke="black" fill="{fill1}" />
 <rect x="{xkoor2}" y="{ykoor2}" width="{bredde}" height="{hoyde}" stroke="black" fill="{fill2}" />
 <rect x="{xkoor3}" y="{ykoor3}" width="{bredde}" height="{hoyde}" stroke="black" fill="{fill3}" />
 <rect x="{xkoor4}" y="{ykoor4}" width="{bredde}" height="{hoyde}" stroke="black" fill="{fill4}" />
</svg>"""

filnavn = "leksjon3.svg"

# Vi må fortelle Python at vi vil 'åpne' en fil
fd = open(filnavn, "w")   # 'fd' er nå et filobjekt
fd.write(svgstreng)
fd.close()