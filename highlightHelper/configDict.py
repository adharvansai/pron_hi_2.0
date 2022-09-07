IPA_Alphabet = ['i', 'r', 'p', 'd', 'l', 'ʧ', 'ɛ', 'h', 'm', 'ə', 'ŋ', 'θ', 'k', 'o', 'ʤ', 'a', 'g', 'æ', 'u', 'f', 'e', 'ð', 'w', 'n', 'b', 'ɔ', 'j', 't', 's', 'ɪ', 'v', 'ʊ']
IPA_DICT = {1: 'i', 2: 'ɪ', 3: 'ɑ', 4: 'e', 5: 'o', 6: 'ɛ', 7: 'ʊ', 8: 'æ', 9: 'u', 10: 'ə', 11: 'aʊ', 12: 'ə', 13: 'aɪ', 14: 'ər', 15: 'ɔɪ', 16: 'm', 17: 'n',
18: 'ʧ', 19: 'p', 20: 't', 21: 'ʤ', 22: 'b', 23: 'd', 24: 'j', 25: 'w', 26: 's', 27: 'r', 28: 'f', 29: 'z',
30: 'ŋ', 31: 'v', 32: 'l', 33: 'k', 34: 'θ', 35: 'ʃ', 36: 'g', 37: 'ð', 38: 'ʒ', 39: 'h'}

COLORS = ["#FFEB6F","#FBA06E","#8EF7FA"]

# 10 and 12 are same as the library has only one symbol for both. 12 is changed from ʌ -> ə

"""
/i/   :    k<u>e</u>y, th<u>e</u>se, y<u>ea</u>st
/ɪ/	  :    w<u>i</u>n, <u>i</u>f, b<u>u</u>siness
/ɑ/	  :    c<u>o</u>d, f<u>a</u>ther, <u>o</u>n
/e/	  :    pl<u>a</u>te, vac<u>a</u>tion, ch<u>a</u>os
/o/	  :    <u>o</u>wn, bur<u>eau</u>, r<u>oa</u>d
/ɛ/	  :    r<u>e</u>d, s<u>a</u>id, pl<u>ea</u>sure
/ʊ/	  :    w<u>oo</u>d, sh<u>ou</u>ld, st<u>oo</u>d
/æ/	  :    h<u>a</u>d, har<u>a</u>ss, sp<u>a</u>n
/u/	  :    b<u>oo</u>t, L<u>u</u>ke, st<u>e</u>wed
/ə/	  :    <u>a</u>bout, tun<u>a</u>, educat<u>io</u>n
/a<sup>u</sup>/  :    <u>o</u>ut, b<u>ough</u>, t<u>o</u>wel
/ʌ/	  :    b<u>u</u>d, M<u>o</u>nday, fl<u>oo</u>d
/a<sup>i</sup>/   :    wh<u>y</u>, good<u>bye</u>, t<u>i</u>le
/ɝ/	  :    b<u>i</u>rd, n<u>u</u>rsery, w<u>o</u>rry
/o<sup>i</sup>/   :    b<u>o</u>y, expl<u>o</u>it, br<u>oi</u>ler
/m/	  :    <u>m</u>an, su<u>mm</u>er, thu<u>mb</u>
/n/	  :    <u>kn</u>ow, pla<u>nn</u>ed, si<u>gn</u>, a<u>n</u>
/tʃ/   :    <u>ch</u>eck, fu<u>t</u>ure, ques<u>t</u>ion, wa<u>tch</u>
/p/	  :    <u>p</u>an, ha<u>pp</u>y, sto<u>p</u>
/t/	  :    <u>t</u>ime, a<u>tt</u>end, walk<u>ed</u>
/dʒ/   :    <u>j</u>ust, gra<u>d</u>uate, lar<u>g</u>e, knowle<u>dge</u>
/b/	  :    <u>b</u>e, ho<u>bb</u>y, descri<u>b</u>e
/d/	  :    <u>d</u>o, a<u>dd</u>ress, call<u>ed</u>
/j/	  :    <u>y</u>es, <u>u</u>se, comp<u>u</u>ter, f<u>ew</u>
/w/	  :    <u>wh</u>y, <u>o</u>ne, ne<u>w</u>er, q<u>u</u>iet
/s/	  :    <u>s</u>un, mi<u>ss</u>, hou<u>s</u>e, <u>sc</u>ien<u>ce</u>, si<u>x</u>, <u>ps</u>ychology
/r/	  :    <u>r</u>ight, <u>wr</u>ong, ca<u>rr</u>y, a<u>r</u>e
/f/	  :    <u>ph</u>one, e<u>ff</u>ect, i<u>f</u>, lau<u>gh</u>
/z/	  :    <u>z</u>oo, ea<u>s</u>y, e<u>x</u>ample, si<u>z</u>e, ja<u>zz</u>, the<u>s</u>e, add<u>s</u>
/ŋ/	  :    fi<u>n</u>ger, thi<u>n</u>k, si<u>ng</u>
/v/	  :    <u>v</u>oice, e<u>v</u>er, o<u>f</u>
/l/	  :    <u>l</u>ike, a<u>l</u>so, wi<u>ll</u>
/k/	  :    <u>k</u>ey, <u>c</u>ould, <u>q</u>uestion, a<u>cc</u>ount, s<u>ch</u>ool, si<u>x</u>, ba<u>ck</u>, li<u>k</u>e
/θ/	  :    <u>th</u>ank, no<u>th</u>ing, brea<u>th</u>
/ʃ/	  :    <u>sh</u>e, informa<u>t</u>ion, deli<u>c</u>ious, discu<u>ss</u>ion, wi<u>sh</u>
/g/	  :    <u>gu</u>est, a<u>g</u>ain, e<u>x</u>ample, bi<u>gg</u>er, fla<u>g</u>
/ð/	  :    <u>th</u>is, o<u>th</u>er, brea<u>the</u>
/ʒ/	  :    u<u>s</u>ual, vi<u>s</u>ion, gara<u>ge</u>
/h/	  :    <u>wh</u>o, <u>h</u>appy, per<u>h</u>aps

"""
