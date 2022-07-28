	.file	"experiment.c"
	.text
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"%d"
	.text
	.p2align 4
	.globl	printBin32
	.type	printBin32, @function
printBin32:
.LFB39:
	.cfi_startproc
	endbr64
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	leaq	.LC0(%rip), %r12
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	movl	%edi, %ebp
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movl	$31, %ebx
	.p2align 4,,10
	.p2align 3
.L2:
	movl	%ebx, %ecx
	movl	%ebp, %edx
	movq	%r12, %rsi
	movl	$1, %edi
	shrl	%cl, %edx
	xorl	%eax, %eax
	subl	$1, %ebx
	andl	$1, %edx
	call	__printf_chk@PLT
	cmpl	$-1, %ebx
	jne	.L2
	movq	stdout(%rip), %rsi
	popq	%rbx
	.cfi_def_cfa_offset 24
	movl	$10, %edi
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	jmp	putc@PLT
	.cfi_endproc
.LFE39:
	.size	printBin32, .-printBin32
	.p2align 4
	.globl	printBinN
	.type	printBinN, @function
printBinN:
.LFB40:
	.cfi_startproc
	endbr64
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	subl	$1, %esi
	js	.L7
	movl	%edi, %ebp
	movl	%esi, %ebx
	leaq	.LC0(%rip), %r12
	.p2align 4,,10
	.p2align 3
.L8:
	movl	%ebx, %ecx
	movl	%ebp, %edx
	movq	%r12, %rsi
	movl	$1, %edi
	shrl	%cl, %edx
	xorl	%eax, %eax
	subl	$1, %ebx
	andl	$1, %edx
	call	__printf_chk@PLT
	cmpl	$-1, %ebx
	jne	.L8
.L7:
	movq	stdout(%rip), %rsi
	popq	%rbx
	.cfi_def_cfa_offset 24
	movl	$10, %edi
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	jmp	putc@PLT
	.cfi_endproc
.LFE40:
	.size	printBinN, .-printBinN
	.p2align 4
	.globl	makeErrorBits
	.type	makeErrorBits, @function
makeErrorBits:
.LFB41:
	.cfi_startproc
	endbr64
	testl	%edi, %edi
	jle	.L14
	pushq	%r13
	.cfi_def_cfa_offset 16
	.cfi_offset 13, -16
	xorl	%eax, %eax
	movl	%esi, %r13d
	pushq	%r12
	.cfi_def_cfa_offset 24
	.cfi_offset 12, -24
	movl	%edi, %r12d
	pushq	%rbp
	.cfi_def_cfa_offset 32
	.cfi_offset 6, -32
	xorl	%ebp, %ebp
	pushq	%rbx
	.cfi_def_cfa_offset 40
	.cfi_offset 3, -40
	subq	$8, %rsp
	.cfi_def_cfa_offset 48
	.p2align 4,,10
	.p2align 3
.L13:
	leal	(%rax,%rax), %ebx
	call	rand@PLT
	cmpl	%r13d, %eax
	setle	%al
	addl	$1, %ebp
	movzbl	%al, %eax
	orl	%ebx, %eax
	cmpl	%ebp, %r12d
	jne	.L13
	addq	$8, %rsp
	.cfi_def_cfa_offset 40
	popq	%rbx
	.cfi_def_cfa_offset 32
	popq	%rbp
	.cfi_def_cfa_offset 24
	popq	%r12
	.cfi_def_cfa_offset 16
	popq	%r13
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L14:
	.cfi_restore 3
	.cfi_restore 6
	.cfi_restore 12
	.cfi_restore 13
	xorl	%eax, %eax
	ret
	.cfi_endproc
.LFE41:
	.size	makeErrorBits, .-makeErrorBits
	.p2align 4
	.globl	encRepCode3
	.type	encRepCode3, @function
encRepCode3:
.LFB42:
	.cfi_startproc
	endbr64
	testl	%esi, %esi
	jle	.L23
	xorl	%r8d, %r8d
	xorl	%r9d, %r9d
	xorl	%r10d, %r10d
	.p2align 4,,10
	.p2align 3
.L22:
	movl	%r9d, %ecx
	movl	%edi, %eax
	addl	$1, %r9d
	shrl	%cl, %eax
	leal	1(%r8), %ecx
	andl	$1, %eax
	movl	%eax, %edx
	movl	%eax, %r11d
	sall	%cl, %edx
	movl	%r8d, %ecx
	sall	%cl, %r11d
	leal	2(%r8), %ecx
	addl	$3, %r8d
	orl	%r11d, %edx
	sall	%cl, %eax
	orl	%edx, %eax
	orl	%eax, %r10d
	cmpl	%r9d, %esi
	jne	.L22
	movl	%r10d, %eax
	ret
.L23:
	xorl	%r10d, %r10d
	movl	%r10d, %eax
	ret
	.cfi_endproc
.LFE42:
	.size	encRepCode3, .-encRepCode3
	.p2align 4
	.globl	decRepCode3
	.type	decRepCode3, @function
decRepCode3:
.LFB43:
	.cfi_startproc
	endbr64
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	testl	%esi, %esi
	jle	.L29
	xorl	%r9d, %r9d
	xorl	%r10d, %r10d
	xorl	%r12d, %r12d
	movl	$1, %r11d
	.p2align 4,,10
	.p2align 3
.L28:
	leal	2(%r9), %ecx
	movl	%edi, %r8d
	movl	%edi, %edx
	movl	%r11d, %eax
	shrl	%cl, %r8d
	leal	1(%r9), %ecx
	shrl	%cl, %edx
	andl	$1, %r8d
	movl	%r9d, %ecx
	andl	$1, %edx
	addl	%edx, %r8d
	movl	%edi, %edx
	shrl	%cl, %edx
	movl	%r10d, %ecx
	andl	$1, %edx
	sall	%cl, %eax
	addl	%r8d, %edx
	orl	%r12d, %eax
	movl	%r12d, %r8d
	cmpl	$1, %edx
	cmova	%eax, %r8d
	addl	$1, %r10d
	addl	$3, %r9d
	movl	%r8d, %r12d
	cmpl	%r10d, %esi
	jne	.L28
	movl	%r12d, %eax
	popq	%r12
	.cfi_remember_state
	.cfi_def_cfa_offset 8
	ret
.L29:
	.cfi_restore_state
	xorl	%r12d, %r12d
	movl	%r12d, %eax
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE43:
	.size	decRepCode3, .-decRepCode3
	.p2align 4
	.globl	makeParityHamCode7_4
	.type	makeParityHamCode7_4, @function
makeParityHamCode7_4:
.LFB44:
	.cfi_startproc
	endbr64
	movl	%edi, %esi
	movl	%edi, %edx
	movl	%edi, %eax
	shrl	%esi
	shrl	$3, %edx
	shrl	$2, %eax
	movl	%esi, %ecx
	xorl	%edx, %ecx
	xorl	%eax, %edx
	xorl	%edi, %ecx
	xorl	%edx, %edi
	xorl	%esi, %edx
	andl	$1, %ecx
	andl	$1, %edi
	andl	$1, %edx
	sall	$2, %ecx
	leal	(%rdi,%rdi), %eax
	orl	%ecx, %eax
	orl	%edx, %eax
	ret
	.cfi_endproc
.LFE44:
	.size	makeParityHamCode7_4, .-makeParityHamCode7_4
	.p2align 4
	.globl	decHamCode7_4
	.type	decHamCode7_4, @function
decHamCode7_4:
.LFB45:
	.cfi_startproc
	endbr64
	movl	%edi, %r8d
	movl	%edi, %edx
	movl	%edi, %eax
	shrl	$4, %r8d
	shrl	$6, %edx
	movl	%r8d, %ecx
	shrl	$3, %eax
	xorl	%edx, %ecx
	xorl	%eax, %ecx
	andl	$1, %ecx
	leal	0(,%rcx,4), %esi
	movl	%edi, %ecx
	shrl	$5, %ecx
	xorl	%ecx, %edx
	movl	%edx, %ecx
	xorl	%r8d, %edx
	xorl	%eax, %ecx
	andl	$1, %edx
	andl	$1, %ecx
	addl	%ecx, %ecx
	orl	%esi, %ecx
	orl	%ecx, %edx
	movl	%edi, %ecx
	andl	$7, %ecx
	xorl	%ecx, %edx
	subl	$1, %edx
	cmpl	$6, %edx
	ja	.L33
	leaq	CSWTCH.13(%rip), %rax
	xorl	(%rax,%rdx,4), %edi
	movl	%edi, %eax
	shrl	$3, %eax
.L33:
	ret
	.cfi_endproc
.LFE45:
	.size	decHamCode7_4, .-decHamCode7_4
	.section	.rodata.str1.1
.LC1:
	.string	"%d %d %d\r\n"
	.text
	.p2align 4
	.globl	compareErrorProb
	.type	compareErrorProb, @function
compareErrorProb:
.LFB46:
	.cfi_startproc
	endbr64
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$56, %rsp
	.cfi_def_cfa_offset 112
	movl	%edi, 36(%rsp)
	movq	%rdx, 40(%rsp)
	testl	%edi, %edi
	jle	.L48
	movl	$0, 32(%rsp)
	movl	%esi, %r15d
	movl	$0, 28(%rsp)
	movl	$0, 24(%rsp)
	movl	$0, 12(%rsp)
	.p2align 4,,10
	.p2align 3
.L47:
	call	rand@PLT
	movl	$4, %ebp
	xorl	%r13d, %r13d
	andl	$15, %eax
	movl	%eax, %r12d
	.p2align 4,,10
	.p2align 3
.L37:
	call	rand@PLT
	addl	%r13d, %r13d
	cmpl	%eax, %r15d
	setge	%al
	movzbl	%al, %eax
	orl	%eax, %r13d
	subl	$1, %ebp
	jne	.L37
	movl	%r12d, %ecx
	cmpl	$1, %r13d
	sbbl	$-1, 24(%rsp)
	movl	%r12d, %r14d
	andl	$1, %ecx
	shrl	$3, %r14d
	movl	%r12d, %eax
	movl	$12, %r13d
	leal	(%rcx,%rcx), %ebx
	leal	0(,%rcx,4), %esi
	shrl	%eax
	orl	%esi, %ebx
	movl	%eax, %edx
	movl	%eax, 16(%rsp)
	movl	%r12d, %eax
	orl	%ecx, %ebx
	movl	%r14d, %ecx
	andl	$1, %edx
	shrl	$2, %eax
	sall	$9, %ecx
	movl	%eax, 20(%rsp)
	andl	$1, %eax
	orl	%ecx, %ebx
	movl	%r14d, %ecx
	sall	$10, %ecx
	orl	%ecx, %ebx
	movl	%r14d, %ecx
	sall	$11, %ecx
	orl	%ecx, %ebx
	leal	0(,%rdx,8), %ecx
	orl	%ecx, %ebx
	movl	%edx, %ecx
	sall	$5, %edx
	sall	$4, %ecx
	orl	%ecx, %ebx
	orl	%edx, %ebx
	movl	%eax, %edx
	sall	$6, %edx
	orl	%edx, %ebx
	movl	%eax, %edx
	sall	$8, %eax
	sall	$7, %edx
	orl	%edx, %ebx
	orl	%eax, %ebx
	.p2align 4,,10
	.p2align 3
.L39:
	call	rand@PLT
	addl	%ebp, %ebp
	cmpl	%eax, %r15d
	setge	%al
	movzbl	%al, %eax
	orl	%eax, %ebp
	subl	$1, %r13d
	jne	.L39
	xorl	%ebx, %ebp
	movl	$7, %ebx
	movl	%ebp, %eax
	movl	%ebp, %esi
	shrl	%eax
	andl	$1, %eax
	movl	%eax, %ecx
	movl	%ebp, %eax
	shrl	$2, %eax
	andl	$1, %eax
	addl	%ecx, %eax
	movl	%ebp, %ecx
	andl	$1, %ecx
	addl	%ecx, %eax
	movl	%ebp, %ecx
	cmpl	$1, %eax
	seta	%al
	shrl	$3, %esi
	movl	%esi, %edi
	shrl	$4, %ecx
	movzbl	%al, %eax
	andl	$1, %edi
	andl	$1, %ecx
	leal	(%rdi,%rcx), %esi
	movl	%ebp, %ecx
	shrl	$5, %ecx
	andl	$1, %ecx
	addl	%esi, %ecx
	movl	%eax, %esi
	orl	$2, %esi
	cmpl	$1, %ecx
	movl	%ebp, %ecx
	cmova	%esi, %eax
	movl	%ebp, %esi
	shrl	$7, %ecx
	shrl	$6, %esi
	andl	$1, %ecx
	movl	%esi, %edi
	andl	$1, %edi
	leal	(%rdi,%rcx), %esi
	movl	%ebp, %ecx
	movl	16(%rsp), %edi
	shrl	$8, %ecx
	andl	$1, %ecx
	addl	%esi, %ecx
	movl	%eax, %esi
	orl	$4, %esi
	cmpl	$1, %ecx
	movl	%ebp, %ecx
	cmova	%esi, %eax
	shrl	$9, %ecx
	movl	%ecx, %esi
	movl	%ebp, %ecx
	shrl	$11, %ebp
	shrl	$10, %ecx
	andl	$1, %esi
	andl	$1, %ebp
	andl	$1, %ecx
	addl	%esi, %ecx
	movl	%edi, %esi
	addl	%ecx, %ebp
	movl	%eax, %ecx
	orl	$8, %ecx
	cmpl	$1, %ebp
	cmova	%ecx, %eax
	movzbl	20(%rsp), %ecx
	cmpl	%eax, %r12d
	setne	%al
	xorl	%r14d, %ecx
	xorl	%edi, %r14d
	xorl	%ecx, %esi
	xorl	%r12d, %r14d
	movzbl	%al, %eax
	xorl	%r12d, %ecx
	addl	%eax, 28(%rsp)
	andl	$1, %esi
	andl	$1, %r14d
	andl	$1, %ecx
	leal	0(,%r12,8), %eax
	addl	%ecx, %ecx
	orl	%eax, %esi
	leal	0(,%r14,4), %eax
	orl	%esi, %eax
	orl	%ecx, %eax
	movl	%eax, %ebp
	.p2align 4,,10
	.p2align 3
.L44:
	call	rand@PLT
	addl	%r13d, %r13d
	cmpl	%eax, %r15d
	setge	%al
	movzbl	%al, %eax
	orl	%eax, %r13d
	subl	$1, %ebx
	jne	.L44
	xorl	%r13d, %ebp
	movl	%ebp, %esi
	movl	%ebp, %eax
	movl	%ebp, %edx
	shrl	$4, %esi
	shrl	$6, %eax
	movl	%esi, %ecx
	shrl	$3, %edx
	xorl	%eax, %ecx
	xorl	%edx, %ecx
	andl	$1, %ecx
	leal	0(,%rcx,4), %edi
	movl	%ebp, %ecx
	shrl	$5, %ecx
	xorl	%ecx, %eax
	movl	%eax, %ecx
	xorl	%esi, %eax
	xorl	%edx, %ecx
	andl	$1, %eax
	andl	$1, %ecx
	addl	%ecx, %ecx
	orl	%edi, %ecx
	orl	%ecx, %eax
	movl	%ebp, %ecx
	andl	$7, %ecx
	xorl	%ecx, %eax
	subl	$1, %eax
	cmpl	$6, %eax
	ja	.L45
	leaq	CSWTCH.13(%rip), %rdi
	movl	(%rdi,%rax,4), %edx
	xorl	%ebp, %edx
	shrl	$3, %edx
.L45:
	xorl	%eax, %eax
	cmpl	%edx, %r12d
	setne	%al
	addl	$1, 12(%rsp)
	addl	%eax, 32(%rsp)
	movl	12(%rsp), %eax
	cmpl	%eax, 36(%rsp)
	jne	.L47
.L36:
	movl	32(%rsp), %r9d
	movl	24(%rsp), %ecx
	movl	$1, %esi
	xorl	%eax, %eax
	movl	28(%rsp), %r8d
	movq	40(%rsp), %rdi
	leaq	.LC1(%rip), %rdx
	call	__fprintf_chk@PLT
	addq	$56, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	xorl	%eax, %eax
	popq	%rbx
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_def_cfa_offset 8
	ret
.L48:
	.cfi_restore_state
	movl	$0, 32(%rsp)
	movl	$0, 28(%rsp)
	movl	$0, 24(%rsp)
	jmp	.L36
	.cfi_endproc
.LFE46:
	.size	compareErrorProb, .-compareErrorProb
	.section	.rodata.str1.1
.LC2:
	.string	"%d\n"
	.section	.text.startup,"ax",@progbits
	.p2align 4
	.globl	main
	.type	main, @function
main:
.LFB47:
	.cfi_startproc
	endbr64
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	xorl	%edi, %edi
	call	time@PLT
	movq	%rax, %rdi
	call	srand@PLT
	movl	$8, %edx
	leaq	.LC2(%rip), %rsi
	xorl	%eax, %eax
	movl	$1, %edi
	call	__printf_chk@PLT
	xorl	%eax, %eax
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE47:
	.size	main, .-main
	.section	.rodata
	.align 16
	.type	CSWTCH.13, @object
	.size	CSWTCH.13, 28
CSWTCH.13:
	.long	1
	.long	2
	.long	32
	.long	4
	.long	16
	.long	8
	.long	64
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 8
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 8
4:
