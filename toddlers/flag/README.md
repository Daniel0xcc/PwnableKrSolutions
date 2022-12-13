
## PWNABLE.KR - FLAG
---

> `I will malloc() and strcpy the flag there. take it.`

This is revese task, here is checksec result: 
 
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)

If we will drop `flag` in to a diassembler like Ida, everything is gonna be cryptic. The reason is - UPX. The file is comperssed with upx(Ultimate Packer for Executables) which uses a compression algorithem to obfuscate the binary to make the life of a reverse engineer much more difficult. However, this is a compression algorithem which can be decompressed by the user. In linux we have a command that lets compress & decompress such a binary: 

> `$ upx -d flag`

This command will decompress the binary and unpack it. Then we can load the binary to IDA and we will see the functions which allocates & strcpy's the flag, then the flag gonna be inside the `.data` section of the binary. 
