import re

# Membaca data dari file teks
with open('data.txt', 'r') as file:
    data = file.read()

# Ekstraksi URL menggunakan regular expression
final_urls = re.findall(r'Final URL: (https?://[^\s]+)', data)

# Menyimpan hasil ekstraksi ke file finalurl.txt
with open('finalurl.txt', 'w') as output_file:
    for url in final_urls:
        output_file.write(url + '\n')

print("URLs telah diekstrak dan disimpan di finalurl.txt")
