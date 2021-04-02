from zippyshare_downloader import Zippyshare

zippy = Zippyshare()

f_out = open("direct-links.txt", "w+")

with open('links.txt') as f_in: 
    lines = list(line for line in (l.strip() for l in f_in) if line)
    for i in lines:
        info = zippy.extract_info(i, download=False)
        print(info['download_url'])
        f_out.write(info['download_url'])
        f_out.write("\n")


f_in.close
f_out.close