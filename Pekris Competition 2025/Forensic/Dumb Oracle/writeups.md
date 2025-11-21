- wireshark analysis
1. looking for statistics > protocol hierarcy, i found the UDP protocol useful because it sends data in the form of packets.
2. looking at the packets one by one, i found a pattern that there's an unique character named **AMAZING**

- filtering using `strings`
1. filtering packets using `strings chall.pcap` and finding a pattern that each packet's content before the unique character **AMAZING** forms a pattern, and when combined, will produce a string in the form of a link.
2. make a script `extract_packets.py` to filter packet automaticly
3. get a link `ristek.link/779b0633b8946d68900c62f832a9ff7f91200cace976991c4af6d4b280b3dc8d25f62865b7e484530265102cb7fd6835de1567b3efb2d02e63c33e082ea157039b0e8845289fae38a58198e5106e44cd558b95b9ffe0e56df6766af5bb555a33e92197c2ff3462fc12385f430cf62746115b7e197174b69b203f3188fa810cd04519facae44625d79323702e81302f190e15fde3972cb88b0c05b0eeb5b3a942d43a29b698f3f75523e07415678fab57a473fdf04c378fc66b5d1655b7ba5b865709b5a339004ef5cf36435a3402c5db0bdbc9526bf241a7740024740075e12b342a271bd6e5467b09d5e55bbe6f952b9720a6f27095d4a43996f75c1b91f0838012d234a805d6d75c4412667fe05464d625edb8103b435c8665595eae77c4c839b2ca65f04e315785f2d5d0206d78bec0b9c5baa15d6e84f106177362fdd5173eba3aececf25715d0ae16977018d8013052c74baf285de0cb56abbcbc2b1088da155fe3082c6cc41a550421080e504819184f21fc7650c56924aa8df48ac2a2`
4. found the file flag.zip, but it's locked by the password

- password cracking using `bkcrack`
1. password cracking flag.zip into flag.png

`../bkcrack/build/src/cli/bkcrack -C ../flag.zip -c flag.png -p plaintext.bin
bkcrack 1.8.1 - 2025-10-25
[05:06:14] Z reduction using 5 bytes of known plaintext
100.0 % (5 / 5)
[05:06:15] Attack on 1121816 Z values at index 6
Keys: f2a3db5a 1a930ac5 7465972e
70.4 % (789259 / 1121816) 
Found a solution. Stopping.
You may resume the attack with the option: --continue-attack 789259
[05:28:35] Keys
f2a3db5a 1a930ac5 7465972e`

2. found the keys to unzip file

`Keys: f2a3db5a 1a930ac5 7465972e`

3. decrypt the flag.png

`../bkcrack/build/src/cli/bkcrack -C ../flag.zip -c flag.png -k f2a3db5a 1a930ac5 7465972e -d ../bkcrack/build/src/cli/bkcrack -C ../flag.zip -c flag.png -k f2a3db5a 1a930ac5 7465972e -d flag_decrypted.png`

4. analysis flag_decrypted.png

`exiftool flag_decrypted.png`

5. found flag in the Title of png

flag: `COMPFEST17{welkam_to_digital_forensics_category_:p_d708d27d09}`
