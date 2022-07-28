	.file	"experiment.c"
	.text
	.section	.rodata
.LC0:
	.string	"%d"
	.text
	.globl	printBin32
	.type	printBin32, @function
printBin32:
.LFB6:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$32, %rsp
	movl	%edi, -20(%rbp)
	movl	$31, -4(%rbp)
	jmp	.L2
.L3:
	movl	-4(%rbp), %eax
	movl	-20(%rbp), %edx
	shrx	%eax, %edx, %eax
	andl	$1, %eax
	movl	%eax, %esi
	leaq	.LC0(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	decl	-4(%rbp)
.L2:
	cmpl	$0, -4(%rbp)
	jns	.L3
	movl	$10, %edi
	call	putchar@PLT
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE6:
	.size	printBin32, .-printBin32
	.globl	printBinN
	.type	printBinN, @function
printBinN:
.LFB7:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$32, %rsp
	movl	%edi, -20(%rbp)
	movl	%esi, -24(%rbp)
	movl	-24(%rbp), %eax
	decl	%eax
	movl	%eax, -4(%rbp)
	jmp	.L5
.L6:
	movl	-4(%rbp), %eax
	movl	-20(%rbp), %edx
	shrx	%eax, %edx, %eax
	andl	$1, %eax
	movl	%eax, %esi
	leaq	.LC0(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	decl	-4(%rbp)
.L5:
	cmpl	$0, -4(%rbp)
	jns	.L6
	movl	$10, %edi
	call	putchar@PLT
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE7:
	.size	printBinN, .-printBinN
	.globl	makeErrorBits
	.type	makeErrorBits, @function
makeErrorBits:
.LFB8:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$32, %rsp
	movl	%edi, -20(%rbp)
	movl	%esi, -24(%rbp)
	movl	$0, -8(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L8
.L9:
	sall	-8(%rbp)
	call	rand@PLT
	cmpl	%eax, -24(%rbp)
	setge	%al
	movzbl	%al, %eax
	orl	%eax, -8(%rbp)
	incl	-4(%rbp)
.L8:
	movl	-4(%rbp), %eax
	cmpl	-20(%rbp), %eax
	jl	.L9
	movl	-8(%rbp), %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE8:
	.size	makeErrorBits, .-makeErrorBits
	.globl	encRepCode3
	.type	encRepCode3, @function
encRepCode3:
.LFB9:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	%edi, -20(%rbp)
	movl	%esi, -24(%rbp)
	movl	$0, -16(%rbp)
	movl	$0, -12(%rbp)
	jmp	.L12
.L15:
	movl	-12(%rbp), %eax
	movl	-20(%rbp), %edx
	shrx	%eax, %edx, %eax
	andl	$1, %eax
	movl	%eax, -4(%rbp)
	movl	$0, -8(%rbp)
	jmp	.L13
.L14:
	movl	-12(%rbp), %edx
	movl	%edx, %eax
	addl	%eax, %eax
	addl	%eax, %edx
	movl	-8(%rbp), %eax
	addl	%edx, %eax
	movl	-4(%rbp), %edx
	shlx	%eax, %edx, %eax
	orl	%eax, -16(%rbp)
	incl	-8(%rbp)
.L13:
	cmpl	$2, -8(%rbp)
	jle	.L14
	incl	-12(%rbp)
.L12:
	movl	-12(%rbp), %eax
	cmpl	-24(%rbp), %eax
	jl	.L15
	movl	-16(%rbp), %eax
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE9:
	.size	encRepCode3, .-encRepCode3
	.globl	decRepCode3
	.type	decRepCode3, @function
decRepCode3:
.LFB10:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	%edi, -20(%rbp)
	movl	%esi, -24(%rbp)
	movl	$0, -16(%rbp)
	movl	$0, -12(%rbp)
	jmp	.L18
.L22:
	movl	$0, -4(%rbp)
	movl	$0, -8(%rbp)
	jmp	.L19
.L20:
	movl	-12(%rbp), %edx
	movl	%edx, %eax
	addl	%eax, %eax
	addl	%eax, %edx
	movl	-8(%rbp), %eax
	addl	%edx, %eax
	movl	-20(%rbp), %edx
	shrx	%eax, %edx, %eax
	andl	$1, %eax
	movl	%eax, %edx
	movl	-4(%rbp), %eax
	addl	%edx, %eax
	movl	%eax, -4(%rbp)
	incl	-8(%rbp)
.L19:
	cmpl	$2, -8(%rbp)
	jle	.L20
	cmpl	$1, -4(%rbp)
	jle	.L21
	movl	-12(%rbp), %eax
	movl	$1, %edx
	shlx	%eax, %edx, %eax
	orl	%eax, -16(%rbp)
.L21:
	incl	-12(%rbp)
.L18:
	movl	-12(%rbp), %eax
	cmpl	-24(%rbp), %eax
	jl	.L22
	movl	-16(%rbp), %eax
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE10:
	.size	decRepCode3, .-decRepCode3
	.globl	makeParityHamCode7_4
	.type	makeParityHamCode7_4, @function
makeParityHamCode7_4:
.LFB11:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	%edi, -20(%rbp)
	movl	-20(%rbp), %eax
	shrl	$3, %eax
	andl	$1, %eax
	movb	%al, -8(%rbp)
	movl	-20(%rbp), %eax
	shrl	$2, %eax
	andl	$1, %eax
	movb	%al, -7(%rbp)
	movl	-20(%rbp), %eax
	shrl	%eax
	andl	$1, %eax
	movb	%al, -6(%rbp)
	movl	-20(%rbp), %eax
	andl	$1, %eax
	movb	%al, -5(%rbp)
	movzbl	-8(%rbp), %eax
	xorb	-6(%rbp), %al
	xorb	-5(%rbp), %al
	movzbl	%al, %eax
	sall	$2, %eax
	movl	%eax, -4(%rbp)
	movzbl	-8(%rbp), %eax
	xorb	-7(%rbp), %al
	xorb	-5(%rbp), %al
	movzbl	%al, %eax
	addl	%eax, %eax
	orl	%eax, -4(%rbp)
	movzbl	-8(%rbp), %eax
	xorb	-7(%rbp), %al
	xorb	-6(%rbp), %al
	movzbl	%al, %eax
	orl	%eax, -4(%rbp)
	movl	-4(%rbp), %eax
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE11:
	.size	makeParityHamCode7_4, .-makeParityHamCode7_4
	.globl	decHamCode7_4
	.type	decHamCode7_4, @function
decHamCode7_4:
.LFB12:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$24, %rsp
	movl	%edi, -20(%rbp)
	movl	-20(%rbp), %eax
	shrl	$3, %eax
	movl	%eax, %edi
	call	makeParityHamCode7_4
	movl	-20(%rbp), %edx
	andl	$7, %edx
	xorl	%edx, %eax
	cmpl	$7, %eax
	ja	.L27
	movl	%eax, %eax
	leaq	0(,%rax,4), %rdx
	leaq	.L29(%rip), %rax
	movl	(%rdx,%rax), %eax
	movslq	%eax, %rdx
	leaq	.L29(%rip), %rax
	addq	%rdx, %rax
	notrack jmp	*%rax
	.section	.rodata
	.align 4
	.align 4
.L29:
	.long	.L36-.L29
	.long	.L35-.L29
	.long	.L34-.L29
	.long	.L33-.L29
	.long	.L32-.L29
	.long	.L31-.L29
	.long	.L30-.L29
	.long	.L28-.L29
	.text
.L36:
	movl	$0, -4(%rbp)
	jmp	.L37
.L28:
	movl	$64, -4(%rbp)
	jmp	.L37
.L33:
	movl	$32, -4(%rbp)
	jmp	.L37
.L31:
	movl	$16, -4(%rbp)
	jmp	.L37
.L30:
	movl	$8, -4(%rbp)
	jmp	.L37
.L32:
	movl	$4, -4(%rbp)
	jmp	.L37
.L34:
	movl	$2, -4(%rbp)
	jmp	.L37
.L35:
	movl	$1, -4(%rbp)
	jmp	.L37
.L27:
	movl	$127, -4(%rbp)
	nop
.L37:
	movl	-20(%rbp), %eax
	xorl	-4(%rbp), %eax
	shrl	$3, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE12:
	.size	decHamCode7_4, .-decHamCode7_4
	.section	.rodata
.LC1:
	.string	"%d %d %d\r\n"
	.text
	.globl	compareErrorProb
	.type	compareErrorProb, @function
compareErrorProb:
.LFB13:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	pushq	%rbx
	subq	$56, %rsp
	.cfi_offset 3, -24
	movl	%edi, -52(%rbp)
	movl	%esi, -56(%rbp)
	movq	%rdx, -64(%rbp)
	movl	$0, -44(%rbp)
	movl	$0, -40(%rbp)
	movl	$0, -36(%rbp)
	movl	$0, -48(%rbp)
	jmp	.L40
.L44:
	call	rand@PLT
	andl	$15, %eax
	movl	%eax, -32(%rbp)
	movl	-56(%rbp), %eax
	movl	%eax, %esi
	movl	$4, %edi
	call	makeErrorBits
	xorl	-32(%rbp), %eax
	movl	%eax, -28(%rbp)
	movl	-32(%rbp), %eax
	cmpl	-28(%rbp), %eax
	je	.L41
	incl	-44(%rbp)
.L41:
	movl	-32(%rbp), %eax
	movl	$4, %esi
	movl	%eax, %edi
	call	encRepCode3
	movl	%eax, -24(%rbp)
	movl	-56(%rbp), %eax
	movl	%eax, %esi
	movl	$12, %edi
	call	makeErrorBits
	xorl	-24(%rbp), %eax
	movl	%eax, -20(%rbp)
	movl	-20(%rbp), %eax
	movl	$4, %esi
	movl	%eax, %edi
	call	decRepCode3
	movl	%eax, -28(%rbp)
	movl	-32(%rbp), %eax
	cmpl	-28(%rbp), %eax
	je	.L42
	incl	-40(%rbp)
.L42:
	movl	-32(%rbp), %eax
	leal	0(,%rax,8), %ebx
	movl	-32(%rbp), %eax
	movl	%eax, %edi
	call	makeParityHamCode7_4
	orl	%ebx, %eax
	movl	%eax, -24(%rbp)
	movl	-56(%rbp), %eax
	movl	%eax, %esi
	movl	$7, %edi
	call	makeErrorBits
	xorl	-24(%rbp), %eax
	movl	%eax, -20(%rbp)
	movl	-20(%rbp), %eax
	movl	%eax, %edi
	call	decHamCode7_4
	movl	%eax, -28(%rbp)
	movl	-32(%rbp), %eax
	cmpl	-28(%rbp), %eax
	je	.L43
	incl	-36(%rbp)
.L43:
	incl	-48(%rbp)
.L40:
	movl	-48(%rbp), %eax
	cmpl	-52(%rbp), %eax
	jl	.L44
	movl	-36(%rbp), %esi
	movl	-40(%rbp), %ecx
	movl	-44(%rbp), %edx
	movq	-64(%rbp), %rax
	movl	%esi, %r8d
	leaq	.LC1(%rip), %rsi
	movq	%rax, %rdi
	movl	$0, %eax
	call	fprintf@PLT
	movl	$0, %eax
	addq	$56, %rsp
	popq	%rbx
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE13:
	.size	compareErrorProb, .-compareErrorProb
	.section	.rodata
.LC2:
	.string	"./dat/e_prob%02d.txt"
.LC3:
	.string	"w"
.LC4:
	.string	"\007%s can't be opened.\n"
.LC7:
	.string	"nothing repetition hamming\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB14:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$4096, %rsp
	orq	$0, (%rsp)
	subq	$48, %rsp
	movq	%fs:40, %rax
	movq	%rax, -8(%rbp)
	xorl	%eax, %eax
	movl	$0, %edi
	call	time@PLT
	movl	%eax, %edi
	call	srand@PLT
	movl	$0, -4132(%rbp)
	jmp	.L47
.L54:
	movl	-4132(%rbp), %edx
	movl	%edx, %eax
	sall	$2, %eax
	addl	%eax, %edx
	leaq	-4112(%rbp), %rax
	movl	%edx, %ecx
	leaq	.LC2(%rip), %rdx
	movl	$4096, %esi
	movq	%rax, %rdi
	movl	$0, %eax
	call	snprintf@PLT
	leaq	-4112(%rbp), %rax
	leaq	.LC3(%rip), %rsi
	movq	%rax, %rdi
	call	fopen@PLT
	movq	%rax, -4120(%rbp)
	cmpq	$0, -4120(%rbp)
	jne	.L48
	leaq	-4112(%rbp), %rax
	movq	%rax, %rsi
	leaq	.LC4(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	$-1, %eax
	jmp	.L55
.L48:
	cmpl	$0, -4132(%rbp)
	jne	.L50
	movl	$-1, -4124(%rbp)
	jmp	.L51
.L50:
	vcvtsi2sdl	-4132(%rbp), %xmm0, %xmm0
	vmovsd	.LC5(%rip), %xmm1
	vmulsd	%xmm1, %xmm0, %xmm0
	vmovsd	.LC6(%rip), %xmm1
	vmulsd	%xmm1, %xmm0, %xmm0
	vcvttsd2sil	%xmm0, %eax
	movl	%eax, -4124(%rbp)
.L51:
	movq	-4120(%rbp), %rax
	movq	%rax, %rcx
	movl	$27, %edx
	movl	$1, %esi
	leaq	.LC7(%rip), %rdi
	call	fwrite@PLT
	movl	$0, -4128(%rbp)
	jmp	.L52
.L53:
	movq	-4120(%rbp), %rdx
	movl	-4124(%rbp), %eax
	movl	%eax, %esi
	movl	$10000, %edi
	call	compareErrorProb
	incl	-4128(%rbp)
.L52:
	cmpl	$99, -4128(%rbp)
	jle	.L53
	movq	-4120(%rbp), %rax
	movq	%rax, %rdi
	call	fclose@PLT
	incl	-4132(%rbp)
.L47:
	cmpl	$10, -4132(%rbp)
	jle	.L54
	movl	$0, %eax
.L55:
	movq	-8(%rbp), %rcx
	xorq	%fs:40, %rcx
	je	.L56
	call	__stack_chk_fail@PLT
.L56:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE14:
	.size	main, .-main
	.section	.rodata
	.align 8
.LC5:
	.long	2576980378
	.long	1068079513
	.align 8
.LC6:
	.long	4290772992
	.long	1105199103
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
