import random
import colorsys

xkoor1, ykoor1 = 10, 10
xkoor2, ykoor2 = 55, 10
xkoor3, ykoor3 = 10, 55
xkoor4, ykoor4 = 55, 55

bredde = 35
hoyde = 35

mainfill = "#ff4444"
main_r = mainfill[1:3]   # main_r -> "ff"
main_g = mainfill[3:5]   # main_g -> "44"
main_b = mainfill[5:7]   # main_b -> "44"

# Vi må disse verdiene først til heltall 0 - 255

main_r_int = int(main_r, base=16)
main_g_int = int(main_g, base=16)
main_b_int = int(main_b, base=16)

# så til desimaltall 0.0 - 1.0

main_r_float = main_r_int / 255   # 1.0000
main_g_float = main_g_int / 255   # 0.2667
main_b_float = main_b_int / 255   # 0.2667

# main_h er en fargetone, vinkel i hsv
# main_s er en fargemetning, radius i hsv
# main_v er en lysintensitet, høyde i hsv
main_h, main_s, main_v = colorsys.rgb_to_hsv(main_r_float, main_g_float, main_b_float)

# To farger "matcher" når de har samme s- og v-verdier
# Vi setter firkant 1 til å ha "main"-fargen vår
c1_h = main_h
c2_h = random.random() # tilfeldig tall mellom 0 og 1
c3_h = random.random() # tilfeldig tall mellom 0 og 1
c4_h = random.random() # tilfeldig tall mellom 0 og 1

# Vi må nå gå tilbake til rgb-verdier -- alle disse er mellom 0 og 1
c1_r, c1_g, c1_b = colorsys.hsv_to_rgb(c1_h, main_s, main_v)
c2_r, c2_g, c2_b = colorsys.hsv_to_rgb(c2_h, main_s, main_v)
c3_r, c3_g, c3_b = colorsys.hsv_to_rgb(c3_h, main_s, main_v)
c4_r, c4_g, c4_b = colorsys.hsv_to_rgb(c4_h, main_s, main_v)

# Vi gjør de til heltall mellom 0 og 255
c1_r, c1_g, c1_b = int(c1_r*255), int(c1_g*255), int(c1_b*255)
c2_r, c2_g, c2_b = int(c2_r*255), int(c2_g*255), int(c2_b*255)
c3_r, c3_g, c3_b = int(c3_r*255), int(c3_g*255), int(c3_b*255)
c4_r, c4_g, c4_b = int(c4_r*255), int(c4_g*255), int(c4_b*255)


# Disse må vi nå få over til teksstrenger av type "#ff123f"
# å få disse over til heksadesimale tall er en "formateringsjobb"
fill1 = f"#{c1_r:02x}{c1_g:02x}{c1_b:02x}"
fill2 = f"#{c2_r:02x}{c2_g:02x}{c2_b:02x}"
fill3 = f"#{c3_r:02x}{c3_g:02x}{c3_b:02x}"
fill4 = f"#{c4_r:02x}{c4_g:02x}{c4_b:02x}"

svgstreng = f"""<svg viewBox="0 0 100 100" width="500mm" height="500mm" xmlns="http://www.w3.org/2000/svg">
 <rect x="0" y="0" width="100%" height="100%" fill="white" />
 <rect x="{xkoor1}" y="{ykoor1}" width="{bredde}" height="{hoyde}" stroke="black" fill="{fill1}" />
 <rect x="{xkoor2}" y="{ykoor2}" width="{bredde}" height="{hoyde}" stroke="black" fill="{fill2}" />
 <rect x="{xkoor3}" y="{ykoor3}" width="{bredde}" height="{hoyde}" stroke="black" fill="{fill3}" />
 <rect x="{xkoor4}" y="{ykoor4}" width="{bredde}" height="{hoyde}" stroke="black" fill="{fill4}" />
</svg>"""

filnavn = "leksjon4.svg"

# Vi må fortelle Python at vi vil 'åpne' en fil
fd = open(filnavn, "w")   # 'fd' er nå et filobjekt
fd.write(svgstreng)
fd.close()