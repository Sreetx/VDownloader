# main.py
#
# Copyright 2024 Programmer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
    
import sys, socket, os, time
if sys.platform in ["linux", "linux2", "win32", "win64"]:
    orange = "\033[93m"
    putih = "\033[39m"
    merah = "\033[91m"
    hijau = "\033[92m"
    biru = "\033[94m"
    borange = "\033[1;93m"
    bputih = "\033[1;39m"
    bmerah = "\033[1;91m"
    bhijau = "\033[1;92m"
    bbiru = "\033[1;94m"
    reset = '\033[0m'
else:
    orange = ""
    putih = ""
    merah = ""
    hijau = ""
    biru = ""
    borange = ""
    bputih = ""
    bmerah = ""
    bhijau = ""
    bbiru = ""
    reset = ''

try:
    print (merah+" [~] Importing Module's"+reset)
    from pytube import YouTube
    from tqdm import tqdm
    import requests
    print(orange+" [~] Membuat folder untuk unduhan...."+reset);time.sleep(0.5)
    os.system('mkdir YouTube')
    os.system('mkdir "YouTube Musik"')
except ImportError:
    if sys.platform in ['linux', 'linux2']:
        os.system('sudo apt update')
        os.system('sudo apt install python3-pip')
        os.system('sudo pip install pytube')
        os.system('sudo pip install tqdm')
        pilih = input(borange+'\n  [?] Apakah anda memiliki maalah dengan python3-pip ? [y/n]: ')
        if pilih.lower() == "y":
            os.system('sudo apt install python3-tqdm')
            try:
                import requests
            except ImportError:
                os.system('sudo apt install python3-requests')
            #Pytube
            pytubes = requests.get('https://files.pythonhosted.org/packages/d8/e7/16fec46c8d255c4bbc4b185d89c91dc92cdb802836570d8004d0db169c91/pytube-15.0.0.tar.gz')
            if pytubes.status_code == 200:
                with open('pytube.tar.gz', 'wb') as x:
                    x.write(pytubes.content)
                os.system('sudo tar -xzf pytube.tar.gz')
                os.system('sudo cp -r pytube*/pytube /lib/python3.11/')
            else: pass
        else: pass
    else:
        os.system('pip install pytube')
        os.system('pip install tqdm')
def youtubes():
    print(hijau+'\n [*] Mode: (1) Downloader YouTube')
    link = input(borange+" [>] Masukkan Link: "+reset)
    resolusi = input(borange+" [>] Pilih Resolusi (144p, 360p, 480p, 720p, 1080p): "+reset)
    try:
        try:
            yt = YouTube(str(link))
        except: print(merah+'[!] Video tidak ditemukan');sys.exit()
        print(borange+"\n<========================================>")
        print(" | "+bputih+"            Informasi Video            "+borange+" | ")
        print("<========================================>"+reset)
        print (' |'+hijau+' [😁] Judul Video:"'+biru, yt.title, '"')
        print(" |"+hijau+" [*] Ditonton:"+biru, yt.views, "penonton")
        print(' |'+hijau+' [*] Rating: '+biru, yt.rating)
        print(" |"+hijau+" [*] Panjang Video:"+biru, yt.length, "detik")
        print(" |"+hijau+" [*] Resolusi yang dipilih: "+biru+resolusi)
        print(" |"+hijau+" [*] Deskripsi Video:"+biru, yt.description)
        print(borange+" >================================================<"+reset)

        pilihann = input(borange+' [?] Unduh Video atau Audio aja(musik) [V/A]: '+reset)
        if pilihann.strip() == "V" or pilihann.strip() == 'v':
            print(merah+' [~] Harap tunggu...'+reset)
            try:
                 yt.timeout = 300
                 stream = yt.streams.filter(progressive=True, res=resolusi, file_extension="mp4").first()
                 print(hijau+' [~] Mengunduh Video....')
                 vid_url = stream.url
                 nama_video = yt.title
                 size = stream.filesize
                 respon = requests.get(vid_url, stream=True)
                 with open('YouTube/'+str(nama_video) + ".mp4", 'ab') as f:
                     with tqdm(total=size, unit="B", unit_scale=True, desc=hijau + ' [~] Mengunduh ' + reset) as pbar:
                         for chunk in respon.iter_content(chunk_size=1024):
                            if chunk:
                                yt.retries = 3
                                f.write(chunk)
                                pbar.update(len(chunk))
                 print(borange+' [*] Berhasil....'+reset)
                 print(borange+' [*] File disimpan dengan nama ', yt.title, 'di folder "YouTube"');sys.exit()
            except KeyboardInterrupt:
                print(merah+' [*] Dibatalkan....');sys.exit()
        elif pilihann.strip() == "A" or pilihann.strip() == "a":
            print(merah+' [~] Harap tunggu....'+reset)
            try:
                 print(merah+' [!] Pengunduh musik mungkin memiliki beberapa bug!'+reset )
                 yt.timeout = 300
                 audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
                 print(hijau+' [~] Mengunduh Musikk....')
                 musik_url = audio_stream.url
                 nama_audio = yt.title
                 sizez = audio_stream.filesize
                 responss = requests.get(musik_url, stream=True)
                 with open('YouTube Musik/'+str(nama_audio) + ".mp3", 'wb') as fs:
                     with tqdm(total=sizez, unit="B", unit_scale=True, desc=hijau + ' [~] Mengunduh ' + reset) as pbars:
                         for chunks in responss.iter_content(chunk_size=1024):
                            if chunks:
                                yt.retries = 3
                                fs.write(chunks)
                                pbars.update(len(chunks))
                 print(borange+' [*] Berhasil....'+reset)
                 print(borange+' [*] File disimpan dengan nama ', yt.title, 'di folder "YouTube Musik"');sys.exit()
            except KeyboardInterrupt:
                print(merah+' [*] Dibatalkan....');sys.exit()
        else: print('lol');sys.exit()
    except Exception as e:
        print(e)

def help():
    os.system('clear || cls')
    baner = borange+'''
<========================================================>
 |                    '''+bputih+'''Video Downloader                  | 
<========================================================>'''+reset+orange+'''
 | '''+hijau+'''Author:  '''+bputih+'''  Sreetx  '''+reset+'''                                 '''+orange+''' |
 | '''+hijau+'''Version:  '''+bputih+''' 0.0.2                                  '''+reset+orange+'''   |
 | '''+hijau+'''YouTube:  '''+bputih+''' https://www.youtube.com/@linggachannel4781'''+reset+orange+'''|
 | '''+hijau+'''GitHub:  '''+bputih+'''  https://github.com/Sreetx            '''+reset+orange+'''     |
 | '''+hijau+'''Desk:   '''+bputih+'''   Alat pengunduh video dari Yt, IG, dan FB '''+reset+orange+''' |
 | '''+hijau+'''Options:   [1] youtube   [2] instagram   [3] facebook    '''+reset+orange+'''  |
 | '''+hijau+'''Usage:  '''+bputih+'''   python3 '''+sys.argv[0]+''' <options>     '''+reset+orange+'''            |
 '''+borange+'''>=======================================================<'''+reset
    print(baner)
    pilih = input(orange+' [~] Pilih mode[1/2/3]: '+reset)
    try:
        socket.create_connection((socket.gethostbyname('google.com'), 80), 2)
    except: print(merah+'\n [!] Cek koneksi internet...'+reset);sys.exit()
    if pilih.lower() == '1':
        youtubes()
    if pilih.lower() == '2':
        print(merah+'\n [~] Importing module....'+reset)
        try:
            from extras import instagrams
        except ImportError:
            igs = input(borange+' [!] Instagram Video Downloader belum diunduh. Unduh sekarang? [y/n]: '+reset)
            if igs.lower() == 'y' or igs.lower() == 'Y':
                print(borange+' [~] Mengunduh....'+reset)
                os.system('mkdir extras')
                instagramh = requests.get('')
                with open('extras/'+str(instagrams.py)) as ig:
                    ig.write(instagramh.content)
                print(borange+' [-] Silakan mulai ulang script'+reset);sys.exit()
    if pilih.lower() == '3':
        print(merah+'\n [~] Importing Module....'+reset)
        try:
            from extras import fb
        except ImportError:
            igs = input(borange+' [!] Facebook Video Downloader belum diunduh. Unduh sekarang? [y/n]: '+reset)
            if igs.lower() == 'y' or igs.lower() == 'Y':
                print(borange+' [~] Mengunduh....'+reset)
                os.system('mkdir extras')
                facebookss = requests.get('')
                with open('extras/'+str(fb.py)) as fbb:
                    fbb.write(facebookss.content)
                print(borange+' [-] Silakan mulai ulang script'+reset);sys.exit()
                
                
if __name__ == '__main__':
    help()
