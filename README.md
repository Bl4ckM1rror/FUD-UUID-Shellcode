# FUD-UUID-Shellcode
<p align="center">
  <img src="https://github.com/Bl4ckM1rror/FUD-UUID-Shellcode/blob/main/logo.png"> <br> 
</p>


## Introduction
Another shellcode injection technique using C++ that attempts to bypass Windows Defender using XOR encryption sorcery and UUID strings **madness** :).

# How it works
## Shellcode generation
* Firstly, generate a payload in binary format( using either `CobaltStrike` or `msfvenom` ) for instance, in `msfvenom`, you can do it like so( the payload I'm using is for **illustration** purposes, you can use whatever payload you want ):
    ```sh
    msfvenom -p windows/messagebox  -f raw -o shellcode.bin
    ```

* Then convert the shellcode( in binary/raw format ) into a `UUID` string format using the Python3 script, `bin_to_uuid.py`: 
  ```sh
  ./bin_to_uuid.py -p shellcode.bin > uuid.txt
  ```

* `xor` encrypt the `UUID` strings in the `uuid.txt` using the Python3 script, `xor_encryptor.py`. 
  ```sh
  ./xor_encryptor.py uuid.txt > xor_crypted_out.txt
  ```

* Copy the `C-style` array in the file, `xor_crypted_out.txt`, and paste it in the C++ file as an array of `unsigned char` i.e. `unsigned char payload[]{your_output_from_xor_crypted_out.txt}`

## Execution
This shellcode injection technique comprises the following subsequent steps:
* First things first, it allocates virtual memory for payload execution and residence via `VirtualAlloc`
* It `xor` decrypts the payload using the `xor` key value 
* Uses `UuidFromStringA` to convert `UUID` strings into their binary representation and store them in the previously allocated memory. This is used to avoid the usage of suspicious APIs like `WriteProcessMemory` or `memcpy`.
* Use `EnumChildWindows` to execute the payload previously loaded into memory( in step 1 )

# What makes it unique?
* It doesn't use standard functions like `memcpy` or `WriteProcessMemory` which are known to raise alarms to AVs/EDRs, this program uses the Windows API function called `UuidFromStringA` which can be used to decode data as well as write it to memory( **Isn't that great folks?** *And please don't say "NO!"* :) ).
* It uses the **function call obfuscation** trick to call the Windows API functions
* Lastly, because it looks unique :) ( *Isn't it?* :) )

# Important
* You have to change the `xor` key(row 86) to what you wish. This can be done in the `./xor_encryptor.py` python3 script by changing the `KEY` variable.
* You have to change the default `executable filename` value(row 90) to your filename.
* `mingw` was used but you can use whichever compiler you prefer. :)

## Compile
* Simply run this at your terminal/shell:
```sh
make
```

# Proof-of-Concept( PoC )

![AV Scan](https://github.com/Bl4ckM1rror/FUD-UUID-Shellcode/blob/main/PoC.png?raw=true)

# Static Analysis

![AV Scan](https://github.com/Bl4ckM1rror/FUD-UUID-Shellcode/blob/main/static-analysis.png?raw=true)

# AV Scan results
The binary was scanned using [antiscan.me](https://antiscan.me/scan/new/result?id=3IYj6CtMq6h8) on 01/08/2022.

![AV Scan](https://github.com/Bl4ckM1rror/FUD-UUID-Shellcode/blob/main/antiscan.png?raw=true)

# Credits
https://research.nccgroup.com/2021/01/23/rift-analysing-a-lazarus-shellcode-execution-method/  
