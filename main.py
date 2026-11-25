import os
from PIL import Image, ImageDraw, ImageFont
W,H=1024,1024
BG=(250,246,236); INK=(22,22,22); RED=(178,34,34); NAVY=(18,42,76); LINE=(190,180,160)
SERIF="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"; SANS="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"; SANSB="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def F(p,s):
    try: return ImageFont.truetype(p,s)
    except Exception: return ImageFont.load_default()
def wrap(d,txt,font,mw):
    ls=[]; cur=""
    for w in txt.split():
        t=(cur+" "+w).strip()
        if d.textlength(t,font=font)<=mw: cur=t
        else:
            if cur: ls.append(cur)
            cur=w
    if cur: ls.append(cur)
    return ls
CHIP={"CONFIRMED":(34,139,34),"OFFICIAL":(25,80,160),"REPORTED":(96,96,96),"CLAIM":(200,110,0),"ONGOING":(176,132,28)}
def chip(d,x,y,label):
    c=CHIP.get(label,(96,96,96)); f=F(SANSB,8); tw=d.textlength(label,font=f); d.rounded_rectangle([x,y,x+tw+8,y+12],2,fill=c); d.text((x+4,y+1.5),label,fill=(255,255,255),font=f); return tw+12
def scene(d,b,k):
    x0,y0,x1,y1=b; w=x1-x0; h=y1-y0; tmp=Image.new("RGB",(328,88)); dd=ImageDraw.Draw(tmp); _scene(dd,k); img.paste(tmp.resize((w,h)),(x0,y0))
def _scene(d,k):
    if k=="riyadh":
        d.rectangle([0,0,328,88],fill=(16,24,48))
        for sx,sy in [(18,10),(58,7),(108,14),(180,8),(238,12),(298,9),(150,18),(270,20)]: d.ellipse([sx,sy,sx+2,sy+2],fill=(255,255,255))
        for bx,bw,bh in [(0,34,44),(38,26,58),(68,30,38),(102,24,66),(130,30,50),(164,26,60),(196,30,42),(230,26,56),(260,30,40),(294,26,52)]: d.rectangle([bx,88-bh,bx+bw,88],fill=(52,64,96))
        d.polygon([(150,6),(168,6),(164,88),(154,88)],fill=(120,140,180)); d.rectangle([150,6,168,14],fill=(200,210,235))
        d.ellipse([196,16,238,48],fill=(255,140,0)); d.ellipse([206,24,228,44],fill=(255,200,60)); d.ellipse([186,8,214,26],fill=(120,120,130)); d.ellipse([222,12,248,30],fill=(100,100,110)); d.polygon([(250,30),(262,26),(262,34),(250,34)],fill=(200,200,200))
    elif k=="shanghai":
        d.rectangle([0,0,328,88],fill=(206,214,222)); d.rectangle([0,62,328,88],fill=(120,130,140))
        d.rectangle([40,34,140,62],fill=(150,40,40)); d.rectangle([56,52,124,62],fill=(90,20,20))
        for cx in [64,84,104]: d.rectangle([cx,56,cx+8,62],fill=(220,200,150))
        d.rectangle([180,22,300,62],fill=(70,84,110))
        for r in range(4):
            for c in range(5): d.rectangle([190+c*22,30+r*14,200+c*22,38+r*14],fill=(255,220,120))
        d.rectangle([150,52,196,74],fill=(255,255,255)); d.rectangle([152,54,194,72],outline=(30,30,30),width=1); d.text((158,57),"FILE",fill=(178,34,34),font=F(SANSB,9)); d.ellipse([176,62,190,72],fill=(178,34,34))
    elif k=="court":
        d.rectangle([0,0,328,88],fill=(214,208,196)); d.rectangle([0,72,328,88],fill=(150,140,125)); d.polygon([(60,8),(268,8),(300,34),(28,34)],fill=(90,70,60))
        for cx in [52,102,152,202,252]: d.rectangle([cx,36,cx+14,72],fill=(235,228,212))
        d.rectangle([140,56,188,72],fill=(60,50,45)); d.rectangle([20,52,44,60],fill=(120,110,95)); d.rectangle([30,60,34,72],fill=(120,110,95)); d.rectangle([284,52,308,60],fill=(120,110,95)); d.rectangle([294,60,298,72],fill=(120,110,95)); d.text((228,44),"10 / 12",fill=(178,34,34),font=F(SANSB,16))
    elif k=="drone":
        d.rectangle([0,0,328,88],fill=(24,30,58))
        for sx,sy in [(20,8),(90,6),(160,12),(230,7),(290,10)]: d.ellipse([sx,sy,sx+2,sy+2],fill=(255,255,255))
        for bx,bw,bh in [(0,40,20),(44,30,30),(78,36,16),(118,30,26),(152,40,18),(196,30,28),(230,36,16),(270,30,24)]: d.rectangle([bx,88-bh,bx+bw,88],fill=(40,48,80))
        d.ellipse([120,14,150,34],fill=(255,150,40)); d.ellipse([128,19,142,29],fill=(255,210,90)); d.ellipse([220,10,236,20],fill=(200,200,200)); d.line([212,15,244,15],fill=(200,200,200),width=2)
    elif k=="trophy":
        d.rectangle([0,0,328,88],fill=(30,90,60)); d.ellipse([60,6,140,34],fill=(255,215,0)); d.polygon([(92,30),(108,30),(104,52),(96,52)],fill=(255,215,0)); d.rectangle([82,52,118,58],fill=(200,170,0))
        d.arc([48,10,72,30],180,360,fill=(255,215,0),width=3); d.arc([128,10,152,30],0,180,fill=(255,215,0),width=3); d.rectangle([180,20,300,30],fill=(255,255,255)); d.rectangle([180,38,280,46],fill=(220,60,60))
    elif k=="ship":
        d.rectangle([0,0,328,88],fill=(150,190,220)); d.rectangle([0,74,328,88],fill=(30,70,110)); d.rectangle([40,58,260,74],fill=(140,40,40))
        for cx in range(6): d.rectangle([50+cx*34,42,78+cx*34,58],fill=(255,200,60) if cx%2 else (40,120,180))
        d.rectangle([250,30,270,58],fill=(90,90,90)); d.ellipse([280,8,300,22],fill=(255,220,120))
    elif k=="chart":
        d.rectangle([0,0,328,88],fill=(235,240,235)); d.line([10,76,318,76],fill=(60,60,60),width=1)
        d.line([(14,54),(60,50),(110,42),(160,46),(210,32),(270,26)],fill=(34,139,34),width=3); d.line([200,40,318,40],fill=(178,34,34),width=1); d.text((230,24),"50,000",fill=(178,34,34),font=F(SANSB,9)); d.text((12,24),"50,018",fill=(34,139,34),font=F(SANSB,11))
    elif k=="server":
        d.rectangle([0,0,328,88],fill=(40,16,16))
        for i in range(4):
            d.rectangle([14+i*70,8,74+i*70,80],fill=(70,70,80))
            for r in range(3): d.ellipse([20+i*70,14+r*14,26+i*70,20+r*14],fill=(255,60,60))
        d.text((120,20),"CODE RED",fill=(255,255,255),font=F(SANSB,13))
    elif k=="heli":
        d.rectangle([0,0,328,88],fill=(170,190,205)); d.polygon([(90,22),(150,22),(160,34),(90,34)],fill=(60,90,60)); d.ellipse([150,20,170,36],fill=(60,90,60)); d.line([170,28,230,24],fill=(60,90,60),width=3); d.line([60,10,180,10],fill=(40,40,40),width=2)
        d.polygon([(20,44),(70,44),(78,56),(30,56)],fill=(110,120,90)); d.polygon([(90,36),(130,36),(136,48),(96,48)],fill=(60,90,60))
    elif k=="market":
        d.rectangle([0,0,328,88],fill=(200,220,230)); d.rectangle([20,10,300,40],fill=(180,60,60)); d.rectangle([20,44,300,80],fill=(240,235,220))
        for i in range(5): d.rectangle([34+i*52,52,74+i*52,72],fill=(90,130,180))
        d.text((90,18),"SUPERMARKET",fill=(255,255,255),font=F(SANSB,13))
    elif k=="desert":
        d.rectangle([0,0,328,88],fill=(235,215,160)); d.ellipse([260,6,292,30],fill=(255,220,120)); d.polygon([(0,88),(120,30),(220,88)],fill=(200,170,110)); d.polygon([(140,88),(260,40),(328,88)],fill=(185,150,95)); d.rectangle([30,34,70,44],fill=(90,90,90)); d.rectangle([46,28,54,34],fill=(90,90,90))
    elif k=="bus":
        d.rectangle([0,0,328,88],fill=(150,170,190)); d.rectangle([0,72,328,88],fill=(80,80,80)); d.rectangle([30,16,150,44],fill=(220,180,40))
        for i in range(4): d.rectangle([40+i*28,22,60+i*28,34],fill=(180,220,240))
        d.ellipse([52,44,66,54],fill=(30,30,30)); d.ellipse([116,44,130,54],fill=(30,30,30)); d.rectangle([190,26,290,44],fill=(140,60,60)); d.ellipse([210,44,224,54],fill=(30,30,30)); d.ellipse([256,44,270,54],fill=(30,30,30))
    elif k=="rocket":
        d.rectangle([0,0,328,88],fill=(18,28,52))
        for sx,sy in [(20,10),(70,6),(150,12),(230,8),(300,14),(260,24)]: d.ellipse([sx,sy,sx+2,sy+2],fill=(255,255,255))
        d.polygon([(150,8),(162,26),(138,26)],fill=(200,60,60)); d.rectangle([138,26,162,52],fill=(235,235,235)); d.polygon([(138,40),(126,54),(138,50)],fill=(200,60,60)); d.polygon([(162,40),(174,54),(162,50)],fill=(200,60,60)); d.polygon([(144,52),(156,52),(150,66)],fill=(255,160,40)); d.ellipse([120,50,132,62],fill=(200,200,210))
CONT=[ [(-168,66),(-140,70),(-125,71),(-110,68),(-95,69),(-85,66),(-80,73),(-70,62),(-65,60),(-55,52),(-60,47),(-70,44),(-75,39),(-80,32),(-81,26),(-90,21),(-97,16),(-105,20),(-110,23),(-117,33),(-125,40),(-125,49),(-135,58),(-155,58),(-165,60)], [(-58,64),(-45,60),(-40,64),(-30,68),(-25,70),(-35,76),(-55,76),(-60,74)], [(-80,9),(-72,12),(-62,10),(-52,5),(-50,0),(-44,-3),(-35,-8),(-40,-20),(-48,-28),(-58,-38),(-65,-45),(-70,-54),(-73,-44),(-73,-30),(-70,-18),(-80,-5)], [(-17,15),(-10,30),(-5,35),(10,37),(20,32),(32,31),(35,28),(43,12),(51,11),(48,0),(40,-10),(35,-18),(28,-33),(20,-35),(15,-27),(12,-18),(9,-1),(9,4),(-8,4)], [(-10,36),(-9,43),(-2,48),(-4,50),(2,51),(8,57),(10,59),(18,56),(21,55),(24,59),(28,60),(30,62),(30,70),(40,68),(45,68),(48,60),(45,55),(40,50),(38,47),(30,46),(28,44),(23,40),(19,42),(12,44),(8,44),(3,42),(0,38)], [(30,70),(45,68),(60,69),(75,73),(90,75),(110,76),(130,72),(160,70),(178,66),(170,60),(162,56),(158,52),(142,50),(140,40),(135,35),(129,33),(127,40),(130,42),(135,44),(141,46),(142,52),(156,59),(162,60),(170,66),(178,65),(170,62),(160,55),(155,50),(140,45),(135,38),(127,33),(122,38),(120,32),(112,22),(108,12),(105,8),(100,8),(98,15),(95,16),(92,21),(89,22),(86,20),(80,13),(77,8),(75,12),(72,20),(66,25),(61,25),(57,26),(56,27),(52,28),(50,29),(48,30),(44,29),(40,32),(36,36),(33,36),(30,36),(28,40),(26,40),(30,45),(28,47),(30,46),(35,47),(40,50),(45,55),(48,60),(45,68),(40,68),(35,70)], [(113,-22),(114,-30),(115,-35),(124,-33),(129,-32),(132,-32),(135,-35),(140,-38),(145,-38),(150,-37),(153,-32),(153,-27),(150,-22),(146,-19),(142,-15),(142,-11),(137,-12),(135,-15),(132,-12),(130,-13),(126,-14),(122,-17),(118,-20)], [(109,1),(113,4),(117,6),(119,1),(117,-3),(112,-3),(109,0)], [(95,5),(98,3),(101,0),(104,-3),(106,-6),(103,-5),(100,0),(97,4)], [(131,-1),(136,-2),(141,-3),(146,-6),(150,-9),(147,-9),(143,-8),(138,-8),(132,-4)] ]
UTC=[("02:15","NATO vows space defence"),("08:16","Hanoi blast"),("10:42","Saudi strikes Yemen"),("14:27","Riyadh tower hit"),("16:51","Houthis 60 km from Aden"),("18:58","Hormuz ship attack"),("20:41","Huawei guilty")]
NUMS=[("11","hurt in Riyadh"),("9","killed in Ukraine"),("50,018","Dow close"),("+8.99%","Taiex record"),("25","killed / missing in Yemen"),("26","Cikande fire toll"),("10/12","Huawei guilty"),("5,258","England heat deaths")]
REGIONS=[("Europe",7,(31,119,180)),("Middle East",8,(214,110,39)),("Asia",9,(44,160,44)),("Africa",5,(148,103,189)),("Americas",5,(227,119,194)),("Oceania",0,(127,127,127)),("World/Space",4,(23,190,207))]
HEROES=[("1 RIYADH · MIDDLE EAST","CONFIRMED","Saudi officials · AP","Houthi drone hits Riyadh's tallest tower again, 11 hurt","A Houthi drone struck the PIF tower, the tallest in Riyadh, injuring 11 — 2 Saudis, 2 Indians, 3 Nepalis, 4 Egyptians. The second strike on the same tower in a week.","riyadh"),("2 SHANGHAI · ASIA","OFFICIAL","CCDI · Xinhua","China probes Shanghai party chief Chen Jining","Chen Jining, 62, is probed for 'serious violations' — the fourth Politburo member to fall in a probe this year, the biggest shock to the Party elite in 2026.","shanghai"),("3 NEW YORK · US / TECH","CONFIRMED","US federal court · Reuters","Huawei guilty on 10 of 12 counts","Huawei guilty on 10 of 12 counts — trade-secret theft and bank fraud — but cleared of racketeering. Sentencing Sep 2027; appeal planned.","court")]
CARDS=[("4 ZAPORIZHZHIA · EUROPE / WAR","REPORTED","Ukrainian officials","Russian attacks kill 9 across Ukraine in a day","Nine killed, 81 wounded in a day; 96 drones fired, 73 shot down.","drone"),("5 DAKAR · AFRICA / SPORT","OFFICIAL","CAS","CAS hands Senegal back the AFCON title","Morocco forfeit 3–0, so Senegal win 1–0 and take the title back.","trophy"),("6 HORMUZ · MIDDLE EAST","REPORTED","UKMTO · wires","IRGC attacks container ship in Hormuz","A container ship was attacked at 18:58 UTC; navigation disabled near Khasab.","ship"),("7 NEW YORK · WORLD / MARKETS","CONFIRMED","Market close","Dow closes above 50,000 for the first time","The Dow closed at 50,018, first above 50,000; Nasdaq −1.5%, Taiex +8.99%.","chart"),("8 REDMOND · WORLD / TECH","REPORTED","Reuters","Microsoft declares 'Code Red' after historic outage","After a 24-hour outage, the worst ever, Microsoft aims to recover in 1 hour.","server"),("9 ESKISEHIR · EUROPE","REPORTED","Turkish officials","Turkish military helicopter crash kills 5","An AS-532 military helicopter crashed in Eskisehir at 19:52 UTC, killing all 5.","heli"),("10 CARTAGENA · AMERICAS","REPORTED","Colombian officials","Supermarket hostages: 25 held in Cartagena","25 held in Cartagena supermarket; 5 elderly women freed, flights held.","market"),("11 ADEN · MIDDLE EAST","REPORTED","wires","Houthis advance within 60 km of Aden","Houthi forces advanced to within 60 km of Aden, Yemen, at 16:51 UTC.","desert"),("12 LAHJ · MIDDLE EAST","REPORTED","Yemeni officials","Saudi strikes kill 25, wound 6 in Yemen","Saudi strikes on a bus and truck in Lahj killed or left missing 25, wounded 6.","bus"),("13 JIUQUAN · WORLD / SPACE","OFFICIAL","CMSA","China names first foreign astronaut for Tiangong","Crew: Tang Hongbo, Wu Yi and Muhammad Zeeshan Ali of Pakistan.","rocket")]
ALSO=["14 Ankara: Haftar visits Turkey for the first time (wires)","15 London: UK sanctions Houthis + 4 officials (UK govt)","16 Villavicencio: Car bomb injures 23 (wires)","17 Gaza: Israel kills Hamas internal security chief (wires)","18 Baghdad: Iraq orders federal control of Kurdish oilfields (Iraqi govt)","19 Gaza: Meningitis alert — 272 infections in Oct, 15 dead in 2026","20 DR Congo: Missing Cessna 208, rebels claim shootdown (claim)","21 Hanoi: Hot-pot explosion kills at least 6, at least 10 hurt (wires)","22 Gulf of Finland: Ukraine hits ship Sparta II, 16 evacuated (wires)","23 Kuala Lumpur: Malaysia to return migrants to Myanmar (govt)","24 Ulleungdo: S. Korea shelter order as Russian jets enter ADIZ (Seoul)","25 Dhaka: Hasina plans return 16 Dec (wires)","26 The Hague: 14 nations endorse ICJ Myanmar ruling (wires)","27 Jakarta: Indonesia nominates 2 VP candidates (MPR)","28 Beijing: China sentences official Ma to death for spying (court)","29 Brussels: NATO vows defence against space threat (Rutte)","30 Mexico City: US drone aided El Chapo capture; Mexico to try him","31 San Salvador: Bukele names 3 soldiers killed in Haiti (govt)","32 Ottawa: Pentagon rebukes Canada — 41.9% of air fleet ready","33 Washington: US adds Megaspeed to trade blacklist (US govt)","34 Kyiv: Zelensky urges Ukraine / Russia / US / Europe talks (wires)","35 Ras Al Khaimah: UAE bus-truck crash kills 13 (wires)","36 London: England record 5,258 heat deaths, summer 2026 (UKHSA)","37 Kourou: Ariane 6 lofts 36 Amazon satellites (Arianespace)","38 Cikande: Factory-fire toll rises to 26 (wires)"]
PINS=[(1,46.7,24.7),(2,121.5,31.2),(3,-74.0,40.7),(4,35.2,47.8),(5,-17.4,14.7),(6,56.3,26.6),(7,-74.0,40.7),(8,-122.1,47.7),(9,30.5,39.8),(10,-75.5,10.4),(11,45.0,12.8),(12,44.9,13.0),(13,98.5,39.7)]
img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img); M=14; X0=M; X1=W-M
d.text((X0,8),"THE WORLD ON ONE DAY",fill=RED,font=F(SANSB,11)); d.text((X1,8),"38 STORIES · 7 REGIONS · 13 FIELDS · ALL FROM TUESDAY 24 NOVEMBER 2026",fill=INK,font=F(SANSB,10),anchor="ra")
d.line([X0,26,X1,26],fill=INK,width=2)
d.text((X0,30),"Tuesday 24 November 2026",fill=INK,font=F(SERIF,30))
d.text((X0,64),"Riyadh tower hit again · Shanghai party chief probed · Huawei guilty on 10 of 12 counts",fill=RED,font=F(SERIF,13))
d.line([X0,84,X1,84],fill=LINE,width=1)
bx=X0; tot=sum(c for _,c,_ in REGIONS)
for name,c,col in REGIONS:
    wseg=int(996*c/tot) if c else 0
    if wseg>0: d.rectangle([bx,88,bx+wseg,108],fill=col); d.text((bx+4,92),f"{name} {c}",fill=(255,255,255),font=F(SANSB,10)); bx+=wseg
d.text((X0,114),"THE DAY IN UTC",fill=RED,font=F(SANSB,11))
ux=X0; uw=996//7
for t,ev in UTC:
    d.text((ux,128),t,fill=RED,font=F(SANSB,11)); d.text((ux,141),ev,fill=INK,font=F(SANS,9)); ux+=uw
d.line([X0,156,X1,156],fill=LINE,width=1)
d.text((X0,160),"THE DAY IN NUMBERS",fill=RED,font=F(SANSB,11))
nx=X0; nw=996//8
for v,lab in NUMS:
    d.text((nx,174),v,fill=INK,font=F(SANSB,19)); d.text((nx,194),lab,fill=(90,90,90),font=F(SANS,9)); nx+=nw
d.line([X0,212,X1,212],fill=INK,width=2)
hy=218; hw=328; hg=188
for i,(kick,ch,src,head,deck,sk) in enumerate(HEROES):
    hx=X0+i*(hw+6)
    d.rectangle([hx,hy,hx+hw,hy+hg],outline=LINE,width=1,fill=(255,255,255))
    scene(d,(hx+1,hy+1,hx+hw-1,hy+88),sk)
    d.text((hx+8,hy+94),kick,fill=RED,font=F(SANSB,10))
    cx=chip(d,hx+8,hy+108,ch); d.text((hx+8+cx,hy+109),src,fill=(110,110,110),font=F(SANS,8))
    for j,l in enumerate(wrap(d,head,F(SANSB,12),hw-16)[:2]): d.text((hx+8,hy+123+j*15),l,fill=INK,font=F(SANSB,12))
    for j,l in enumerate(wrap(d,deck,F(SANS,10),hw-16)[:3]): d.text((hx+8,hy+152+j*12),l,fill=(50,50,50),font=F(SANS,10))
cy=hy+hg+8; cw=194; chh=104
for i,(kick,ch,src,head,deck,sk) in enumerate(CARDS):
    r,c=divmod(i,5); cx0=X0+c*(cw+6); cy0=cy+r*(chh+6)
    d.rectangle([cx0,cy0,cx0+cw,cy0+chh],outline=LINE,width=1,fill=(255,255,255))
    scene(d,(cx0+1,cy0+1,cx0+cw-1,cy0+30),sk)
    d.text((cx0+6,cy0+33),kick,fill=RED,font=F(SANSB,8))
    chip(d,cx0+6,cy0+45,ch)
    for j,l in enumerate(wrap(d,head,F(SANSB,10),cw-12)[:2]): d.text((cx0+6,cy0+59+j*12),l,fill=INK,font=F(SANSB,10))
    for j,l in enumerate(wrap(d,deck,F(SANS,9),cw-12)[:2]): d.text((cx0+6,cy0+83+j*10),l,fill=(60,60,60),font=F(SANS,9))
my=cy+2*(chh+6)+8; mh=128
d.text((X0,my),"THE WORLD — 13 STORIES PINNED",fill=RED,font=F(SANSB,11))
mx0,my0,mx1,my1=X0,my+16,X0+688,my+16+mh-18
d.rectangle([mx0,my0,mx1,my1],outline=LINE,width=1,fill=(212,228,238))
def proj(lon,lat): return (mx0+(lon+170)/360.0*(mx1-mx0), my0+(84-lat)/144.0*(my1-my0))
for poly in CONT: d.polygon([proj(lo,la) for lo,la in poly],fill=(120,170,110),outline=(70,110,70))
d.text((mx0+700,my+16),"LEGEND",fill=RED,font=F(SANSB,10))
for i,(name,c,col) in enumerate(REGIONS):
    ly=my+32+i*14; d.rectangle([mx0+700,ly,mx0+712,ly+10],fill=col); d.text((mx0+716,ly),f"{name} — {c}",fill=INK,font=F(SANS,9))
d.text((mx0+700,my+32+7*14+4),"Pins 1–13 = story numbers.",fill=(80,80,80),font=F(SANS,9))
d.text((mx0+700,my+32+7*14+18),"Map: equirectangular,",fill=(80,80,80),font=F(SANS,9)); d.text((mx0+700,my+32+7*14+30),"real lat / lon.",fill=(80,80,80),font=F(SANS,9))
off={7:(9,0),12:(7,-7)}
for n,lon,lat in PINS:
    ox,oy=off.get(n,(0,0)); px,py=proj(lon,lat); px+=ox; py+=oy
    d.ellipse([px-8,py-8,px+8,py+8],fill=RED,outline=(255,255,255),width=1); d.text((px,py),str(n),fill=(255,255,255),font=F(SANSB,8),anchor="mm")
ay=my+mh+8
d.text((X0,ay),"ALSO ON TUESDAY 24 NOVEMBER — 25 MORE STORIES",fill=RED,font=F(SANSB,11))
acol=996//3; af=F(SANS,9)
for i,t in enumerate(ALSO):
    col,row=divmod(i,9); ax=X0+col*acol; ayy=ay+18+row*11
    s=t
    while d.textlength(s,font=af)>acol-8 and len(s)>10: s=s[:-4]+"…"
    d.text((ax,ayy),s,fill=INK,font=af)
dy=ay+18+9*11+6
d.rectangle([X0,dy,X1,dy+74],outline=RED,width=2,fill=(255,238,238))
d.text((X0+8,dy+5),"DATE CHECK",fill=RED,font=F(SANSB,11))
dc1="Every story above happened or was first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC."
dc2="LEFT OUT (not 24 Nov): Hormuz mine claims (Mon 23 Nov) · Nvidia's Huang returns as CEO (Mon 23 Nov) · EU 22nd sanctions package (Mon 23 Nov) · COP31 ends with no deal (Sun 22 Nov) · Corvette Merkury sinks (Sat 22 Nov) · El Chapo Isidro arrested (Fri 20 Nov) · Cikande factory fire begins (Sat 21 Nov) · Trump hush-money appeal verdict (Mon 23 Nov) · ATP Finals (Sun 22 Nov) · Las Vegas GP (Sat 21 Nov)."
dc3="NOT YET: Shenzhou-24 launch (Wed 25 Nov 00:18 UTC) · MPR session elects VP (11 Dec) · Huawei sentencing (Sep 2027) · Hasina returns to Bangladesh (16 Dec)."
for j,l in enumerate(wrap(d,dc1,F(SANS,9),996-16)): d.text((X0+8,dy+20+j*11),l,fill=INK,font=F(SANS,9))
for j,l in enumerate(wrap(d,dc2,F(SANS,9),996-16)): d.text((X0+8,dy+31+j*11),l,fill=INK,font=F(SANS,9))
for j,l in enumerate(wrap(d,dc3,F(SANS,9),996-16)): d.text((X0+8,dy+53+j*11),l,fill=INK,font=F(SANS,9))
fy=dy+82
d.text((X0,fy),"Sources: dailysummaryof.com · AP · Reuters · UKMTO · CAS · CMSA · UKHSA · official wires.",fill=(80,80,80),font=F(SANS,9))
d.text((X0,fy+12),"CONFIRMED = 2+ outlets · OFFICIAL = on record · REPORTED = one outlet · CLAIM = one side's claim · ONGOING = still running.",fill=(80,80,80),font=F(SANS,9))
d.text((X0,fy+24),"Scenes are drawn illustrations, not photographs. 38 stories · 7 regions · 13 fields.",fill=(80,80,80),font=F(SANS,9))
out=os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR","out"),"entry.png"); os.makedirs(os.path.dirname(out),exist_ok=True)
img.save(out,optimize=True); print("saved",out)
