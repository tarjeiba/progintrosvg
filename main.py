xkoor = -150
ykoor = 0
bredde = 134
hoyde = 231

svgstreng = f"""<svg viewBox="-200 -200 400 400" width="500mm" xmlns="http://www.w3.org/2000/svg">
 <rect x="-200" y="-200" width="400" height="400" fill="white" />
 <rect x="{xkoor}" y="{ykoor}" width="{bredde}" height="{hoyde}" stroke="black" fill="#ff4444" />
</svg>"""

filnavn = "leksjon2-v2.svg"

# Vi må fortelle Python at vi vil 'åpne' en fil
fd = open(filnavn, "w")   # 'fd' er nå et filobjekt
fd.write(svgstreng)
fd.close()