# Ingatan

Author: Karev

Saya ketemu cara rahasia untuk masuk Netsos, tapi sayangnya tiba-tiba file saya ke encrypt semua :(

Note : Beware of malware, do not run any executable on your machine if you dont know what it does. Use a VM to be safe.

**Link:** `https://drive.google.com/drive/folders/14tYX3GOFK9BOKv6HmJbyydoJvsQlOIBa?usp=sharing`

**Password :** `gudAtiCHtKuj3iDXGhCM7sP7hNb7rn`

**Sha256hash dumpnya :** `b40ab4da18fec5361cc28bfc2f9cfbf1fe7842e28f61bbb18ff54d5509742407`

`nc ctf.netsos.id 7501`

## Hint 1:
I would suggest you to use `https://github.com/volatilityfoundation/volatility3`

## Hint 2:
If you try to run volatility on the memory dump, you'll most likely get an error saying that symbol table requirement was not fulfilled. 
That's because volatility needs a symbol table specific to the kernel of the dump to work. 
You can learn how to make it here : `https://www.hackthebox.com/blog/how-to-create-linux-symbol-tables-volatility`
