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
	shrx	%ebx, %ebp, %edx
	movq	%r12, %rsi
	andl	$1, %edx
	movl	$1, %edi
	xorl	%eax, %eax
	decl	%ebx
	call	__printf_chk@PLT
	cmpl	$-1, %ebx
	jne	.L2
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	movq	stdout(%rip), %rsi
	movl	$10, %edi
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
	decl	%esi
	js	.L7
	movl	%edi, %ebp
	movl	%esi, %ebx
	leaq	.LC0(%rip), %r12
	.p2align 4,,10
	.p2align 3
.L8:
	shrx	%ebx, %ebp, %edx
	movq	%r12, %rsi
	andl	$1, %edx
	movl	$1, %edi
	xorl	%eax, %eax
	decl	%ebx
	call	__printf_chk@PLT
	cmpl	$-1, %ebx
	jne	.L8
.L7:
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	movq	stdout(%rip), %rsi
	movl	$10, %edi
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
	movzbl	%al, %eax
	incl	%ebp
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
	jle	.L27
	leal	-1(%rsi), %eax
	cmpl	$6, %eax
	jbe	.L28
	movl	%esi, %edx
	vmovd	%edi, %xmm7
	vmovdqa	.LC1(%rip), %ymm3
	vmovdqa	.LC2(%rip), %ymm6
	vmovdqa	.LC3(%rip), %ymm4
	vmovdqa	.LC4(%rip), %ymm5
	shrl	$3, %edx
	vpbroadcastd	%xmm7, %ymm7
	xorl	%eax, %eax
	vpxor	%xmm8, %xmm8, %xmm8
	.p2align 4,,10
	.p2align 3
.L24:
	vmovdqa	%ymm3, %ymm2
	vpsrlvd	%ymm2, %ymm7, %ymm0
	vpslld	$1, %ymm2, %ymm1
	vpand	%ymm4, %ymm0, %ymm0
	vpaddd	%ymm2, %ymm1, %ymm1
	vpsllvd	%ymm1, %ymm0, %ymm9
	vpaddd	%ymm4, %ymm1, %ymm2
	vpaddd	%ymm5, %ymm1, %ymm1
	vpsllvd	%ymm2, %ymm0, %ymm2
	vpsllvd	%ymm1, %ymm0, %ymm0
	vpor	%ymm9, %ymm2, %ymm2
	vpor	%ymm8, %ymm0, %ymm0
	incl	%eax
	vpaddd	%ymm6, %ymm3, %ymm3
	vpor	%ymm0, %ymm2, %ymm8
	cmpl	%edx, %eax
	jne	.L24
	vextracti128	$0x1, %ymm8, %xmm0
	vpor	%xmm0, %xmm8, %xmm0
	vpsrldq	$8, %xmm0, %xmm1
	vpor	%xmm1, %xmm0, %xmm0
	vpsrldq	$4, %xmm0, %xmm1
	vpor	%xmm1, %xmm0, %xmm0
	movl	%esi, %ecx
	vmovd	%xmm0, %eax
	andl	$-8, %ecx
	testb	$7, %sil
	je	.L32
	vzeroupper
.L23:
	leal	(%rcx,%rcx,2), %r9d
	leal	1(%r9), %edx
	shrx	%ecx, %edi, %r8d
	andl	$1, %r8d
	shlx	%r9d, %r8d, %r10d
	shlx	%edx, %r8d, %edx
	orl	%r10d, %edx
	orl	%edx, %eax
	addl	$2, %r9d
	leal	1(%rcx), %edx
	shlx	%r9d, %r8d, %r8d
	orl	%r8d, %eax
	cmpl	%edx, %esi
	jle	.L31
	leal	(%rdx,%rdx,2), %r9d
	shrx	%edx, %edi, %r8d
	leal	1(%r9), %edx
	andl	$1, %r8d
	shlx	%r9d, %r8d, %r10d
	shlx	%edx, %r8d, %edx
	orl	%r10d, %edx
	orl	%edx, %eax
	addl	$2, %r9d
	leal	2(%rcx), %edx
	shlx	%r9d, %r8d, %r8d
	orl	%r8d, %eax
	cmpl	%edx, %esi
	jle	.L31
	leal	(%rdx,%rdx,2), %r9d
	shrx	%edx, %edi, %r8d
	leal	1(%r9), %edx
	andl	$1, %r8d
	shlx	%r9d, %r8d, %r10d
	shlx	%edx, %r8d, %edx
	orl	%r10d, %edx
	orl	%edx, %eax
	addl	$2, %r9d
	leal	3(%rcx), %edx
	shlx	%r9d, %r8d, %r8d
	orl	%r8d, %eax
	cmpl	%edx, %esi
	jle	.L31
	leal	(%rdx,%rdx,2), %r9d
	shrx	%edx, %edi, %r8d
	leal	1(%r9), %edx
	andl	$1, %r8d
	shlx	%r9d, %r8d, %r10d
	shlx	%edx, %r8d, %edx
	orl	%r10d, %edx
	orl	%edx, %eax
	addl	$2, %r9d
	leal	4(%rcx), %edx
	shlx	%r9d, %r8d, %r8d
	orl	%r8d, %eax
	cmpl	%edx, %esi
	jle	.L31
	leal	(%rdx,%rdx,2), %r9d
	shrx	%edx, %edi, %r8d
	leal	1(%r9), %edx
	andl	$1, %r8d
	shlx	%r9d, %r8d, %r10d
	shlx	%edx, %r8d, %edx
	orl	%r10d, %edx
	orl	%edx, %eax
	addl	$2, %r9d
	leal	5(%rcx), %edx
	shlx	%r9d, %r8d, %r8d
	orl	%r8d, %eax
	cmpl	%edx, %esi
	jle	.L31
	leal	(%rdx,%rdx,2), %r9d
	shrx	%edx, %edi, %r8d
	leal	1(%r9), %edx
	andl	$1, %r8d
	shlx	%r9d, %r8d, %r10d
	shlx	%edx, %r8d, %edx
	orl	%r10d, %edx
	orl	%edx, %eax
	addl	$2, %r9d
	addl	$6, %ecx
	shlx	%r9d, %r8d, %r8d
	orl	%r8d, %eax
	cmpl	%ecx, %esi
	jle	.L31
	leal	(%rcx,%rcx,2), %esi
	shrx	%ecx, %edi, %edx
	leal	1(%rsi), %ecx
	andl	$1, %edx
	shlx	%ecx, %edx, %ecx
	shlx	%esi, %edx, %edi
	orl	%edi, %ecx
	orl	%eax, %ecx
	leal	2(%rsi), %eax
	shlx	%eax, %edx, %eax
	orl	%ecx, %eax
	ret
.L27:
	xorl	%eax, %eax
.L31:
	ret
.L32:
	vzeroupper
	ret
.L28:
	xorl	%ecx, %ecx
	xorl	%eax, %eax
	jmp	.L23
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
	jle	.L37
	xorl	%r9d, %r9d
	xorl	%r10d, %r10d
	xorl	%r12d, %r12d
	movl	$1, %r11d
	.p2align 4,,10
	.p2align 3
.L36:
	leal	2(%r9), %ecx
	leal	1(%r9), %edx
	shrx	%ecx, %edi, %ecx
	shrx	%edx, %edi, %edx
	andl	$1, %ecx
	andl	$1, %edx
	leal	(%rcx,%rdx), %ecx
	shrx	%r9d, %edi, %edx
	andl	$1, %edx
	addl	%ecx, %edx
	shlx	%r10d, %r11d, %eax
	movl	%r12d, %ecx
	orl	%r12d, %eax
	cmpl	$1, %edx
	cmova	%eax, %ecx
	incl	%r10d
	movl	%ecx, %r12d
	addl	$3, %r9d
	cmpl	%r10d, %esi
	jne	.L36
	movl	%r12d, %eax
	popq	%r12
	.cfi_remember_state
	.cfi_def_cfa_offset 8
	ret
.L37:
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
	shrl	%esi
	movl	%edi, %edx
	movl	%edi, %eax
	shrl	$3, %edx
	shrl	$2, %eax
	movl	%esi, %ecx
	xorl	%edx, %ecx
	xorl	%eax, %edx
	xorl	%edi, %ecx
	xorl	%edx, %edi
	andl	$1, %ecx
	andl	$1, %edi
	sall	$2, %ecx
	leal	(%rdi,%rdi), %eax
	xorl	%esi, %edx
	orl	%ecx, %eax
	andl	$1, %edx
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
	shrl	$4, %r8d
	movl	%edi, %edx
	shrl	$6, %edx
	movl	%edi, %eax
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
	xorl	%eax, %ecx
	andl	$1, %ecx
	addl	%ecx, %ecx
	xorl	%r8d, %edx
	orl	%esi, %ecx
	andl	$1, %edx
	orl	%ecx, %edx
	movl	%edi, %ecx
	andl	$7, %ecx
	xorl	%ecx, %edx
	decl	%edx
	cmpl	$6, %edx
	ja	.L43
	leaq	CSWTCH.13(%rip), %rax
	xorl	(%rax,%rdx,4), %edi
	movl	%edi, %eax
	shrl	$3, %eax
.L43:
	ret
	.cfi_endproc
.LFE45:
	.size	decHamCode7_4, .-decHamCode7_4
	.section	.rodata.str1.1
.LC5:
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
	jle	.L57
	movl	$0, 32(%rsp)
	movl	$0, 28(%rsp)
	movl	$0, 24(%rsp)
	movl	$0, 12(%rsp)
	movl	%esi, %r15d
	.p2align 4,,10
	.p2align 3
.L56:
	call	rand@PLT
	andl	$15, %eax
	movl	%eax, %r12d
	movl	$4, %ebp
	xorl	%r13d, %r13d
	.p2align 4,,10
	.p2align 3
.L46:
	call	rand@PLT
	addl	%r13d, %r13d
	cmpl	%eax, %r15d
	setge	%al
	movzbl	%al, %eax
	orl	%eax, %r13d
	decl	%ebp
	jne	.L46
	cmpl	$1, %r13d
	movl	%r12d, %ecx
	sbbl	$-1, 24(%rsp)
	andl	$1, %ecx
	leal	(%rcx,%rcx), %ebx
	leal	0(,%rcx,4), %esi
	movl	%r12d, %r14d
	shrl	$3, %r14d
	orl	%esi, %ebx
	orl	%ecx, %ebx
	movl	%r14d, %ecx
	sall	$9, %ecx
	orl	%ecx, %ebx
	movl	%r12d, %eax
	movl	%r14d, %ecx
	shrl	%eax
	sall	$10, %ecx
	movl	%eax, %edx
	orl	%ecx, %ebx
	movl	%r14d, %ecx
	andl	$1, %edx
	sall	$11, %ecx
	orl	%ecx, %ebx
	leal	0(,%rdx,8), %ecx
	orl	%ecx, %ebx
	movl	%eax, 16(%rsp)
	movl	%edx, %ecx
	movl	%r12d, %eax
	shrl	$2, %eax
	sall	$4, %ecx
	sall	$5, %edx
	movl	%eax, 20(%rsp)
	orl	%ecx, %ebx
	andl	$1, %eax
	orl	%edx, %ebx
	movl	%eax, %edx
	sall	$6, %edx
	orl	%edx, %ebx
	movl	%eax, %edx
	sall	$7, %edx
	orl	%edx, %ebx
	sall	$8, %eax
	orl	%eax, %ebx
	movl	$12, %r13d
	.p2align 4,,10
	.p2align 3
.L48:
	call	rand@PLT
	addl	%ebp, %ebp
	cmpl	%eax, %r15d
	setge	%al
	movzbl	%al, %eax
	orl	%eax, %ebp
	decl	%r13d
	jne	.L48
	xorl	%ebx, %ebp
	movl	%ebp, %eax
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
	cmpl	$1, %eax
	movl	%ebp, %esi
	seta	%al
	movl	%ebp, %ecx
	shrl	$3, %esi
	movl	%esi, %edi
	shrl	$4, %ecx
	andl	$1, %edi
	andl	$1, %ecx
	leal	(%rdi,%rcx), %esi
	movl	%ebp, %ecx
	shrl	$5, %ecx
	movzbl	%al, %eax
	andl	$1, %ecx
	addl	%esi, %ecx
	movl	%eax, %esi
	orl	$2, %esi
	cmpl	$1, %ecx
	cmova	%esi, %eax
	movl	%ebp, %esi
	shrl	$6, %esi
	movl	%ebp, %ecx
	movl	%esi, %edi
	shrl	$7, %ecx
	andl	$1, %edi
	andl	$1, %ecx
	leal	(%rdi,%rcx), %esi
	movl	%ebp, %ecx
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
	shrl	$10, %ecx
	andl	$1, %esi
	andl	$1, %ecx
	shrl	$11, %ebp
	addl	%esi, %ecx
	andl	$1, %ebp
	addl	%ecx, %ebp
	movl	%eax, %ecx
	orl	$8, %ecx
	cmpl	$1, %ebp
	cmova	%ecx, %eax
	movl	16(%rsp), %edi
	movzbl	20(%rsp), %ecx
	cmpl	%eax, %r12d
	setne	%al
	movl	%edi, %esi
	xorl	%r14d, %ecx
	xorl	%edi, %r14d
	movzbl	%al, %eax
	xorl	%ecx, %esi
	xorl	%r12d, %r14d
	addl	%eax, 28(%rsp)
	andl	$1, %esi
	leal	0(,%r12,8), %eax
	andl	$1, %r14d
	xorl	%r12d, %ecx
	orl	%eax, %esi
	andl	$1, %ecx
	leal	0(,%r14,4), %eax
	orl	%esi, %eax
	addl	%ecx, %ecx
	orl	%ecx, %eax
	movl	%eax, %ebp
	movl	$7, %ebx
	.p2align 4,,10
	.p2align 3
.L53:
	call	rand@PLT
	addl	%r13d, %r13d
	cmpl	%eax, %r15d
	setge	%al
	movzbl	%al, %eax
	orl	%eax, %r13d
	decl	%ebx
	jne	.L53
	xorl	%r13d, %ebp
	movl	%ebp, %esi
	shrl	$4, %esi
	movl	%ebp, %eax
	shrl	$6, %eax
	movl	%ebp, %edx
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
	xorl	%edx, %ecx
	andl	$1, %ecx
	addl	%ecx, %ecx
	xorl	%esi, %eax
	orl	%edi, %ecx
	andl	$1, %eax
	orl	%ecx, %eax
	movl	%ebp, %ecx
	andl	$7, %ecx
	xorl	%ecx, %eax
	decl	%eax
	cmpl	$6, %eax
	ja	.L54
	leaq	CSWTCH.13(%rip), %rdi
	movl	(%rdi,%rax,4), %edx
	xorl	%ebp, %edx
	shrl	$3, %edx
.L54:
	xorl	%eax, %eax
	cmpl	%edx, %r12d
	setne	%al
	incl	12(%rsp)
	addl	%eax, 32(%rsp)
	movl	12(%rsp), %eax
	cmpl	%eax, 36(%rsp)
	jne	.L56
.L45:
	movl	32(%rsp), %r9d
	movl	28(%rsp), %r8d
	movl	24(%rsp), %ecx
	movq	40(%rsp), %rdi
	leaq	.LC5(%rip), %rdx
	movl	$1, %esi
	xorl	%eax, %eax
	call	__fprintf_chk@PLT
	addq	$56, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
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
	xorl	%eax, %eax
	popq	%r15
	.cfi_def_cfa_offset 8
	ret
.L57:
	.cfi_restore_state
	movl	$0, 32(%rsp)
	movl	$0, 28(%rsp)
	movl	$0, 24(%rsp)
	jmp	.L45
	.cfi_endproc
.LFE46:
	.size	compareErrorProb, .-compareErrorProb
	.section	.rodata.str1.1
.LC6:
	.string	"./dat/e_prob%02d.txt"
.LC7:
	.string	"w"
.LC8:
	.string	"\007%s can't be opened.\n"
.LC11:
	.string	"nothing repetition hamming\n"
	.section	.text.startup,"ax",@progbits
	.p2align 4
	.globl	main
	.type	main, @function
main:
.LFB47:
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
	subq	$4096, %rsp
	.cfi_def_cfa_offset 4152
	orq	$0, (%rsp)
	subq	$72, %rsp
	.cfi_def_cfa_offset 4224
	xorl	%edi, %edi
	movq	%fs:40, %rax
	movq	%rax, 4152(%rsp)
	xorl	%eax, %eax
	call	time@PLT
	movq	%rax, %rdi
	call	srand@PLT
	leaq	48(%rsp), %rax
	movl	$0, 36(%rsp)
	movq	%rax, 40(%rsp)
	.p2align 4,,10
	.p2align 3
.L82:
	movl	36(%rsp), %eax
	movq	40(%rsp), %rbx
	leal	(%rax,%rax,4), %r9d
	leaq	.LC6(%rip), %r8
	movl	$4096, %ecx
	movl	$1, %edx
	movl	$4096, %esi
	movq	%rbx, %rdi
	xorl	%eax, %eax
	call	__snprintf_chk@PLT
	leaq	.LC7(%rip), %rsi
	movq	%rbx, %rdi
	call	fopen@PLT
	movq	%rax, 24(%rsp)
	testq	%rax, %rax
	je	.L95
	movl	36(%rsp), %eax
	movl	$-1, (%rsp)
	testl	%eax, %eax
	je	.L68
	vxorpd	%xmm1, %xmm1, %xmm1
	vcvtsi2sdl	%eax, %xmm1, %xmm0
	vmulsd	.LC9(%rip), %xmm0, %xmm0
	vmulsd	.LC10(%rip), %xmm0, %xmm0
	vcvttsd2sil	%xmm0, %eax
	movl	%eax, (%rsp)
.L68:
	movq	24(%rsp), %rcx
	movl	$27, %edx
	movl	$1, %esi
	leaq	.LC11(%rip), %rdi
	call	fwrite@PLT
	movl	$100, 32(%rsp)
	.p2align 4,,10
	.p2align 3
.L69:
	movl	$10000, 20(%rsp)
	xorl	%r13d, %r13d
	xorl	%ebp, %ebp
	xorl	%r12d, %r12d
	.p2align 4,,10
	.p2align 3
.L80:
	call	rand@PLT
	andl	$15, %eax
	movl	%eax, %r14d
	movl	$4, %r15d
	xorl	%ebx, %ebx
	.p2align 4,,10
	.p2align 3
.L70:
	call	rand@PLT
	addl	%ebx, %ebx
	cmpl	%eax, (%rsp)
	setge	%al
	movzbl	%al, %eax
	orl	%eax, %ebx
	decl	%r15d
	jne	.L70
	cmpl	$1, %ebx
	movl	%r14d, %r9d
	sbbl	$-1, %r12d
	andl	$1, %r9d
	leal	(%r9,%r9), %ebx
	leal	0(,%r9,4), %r10d
	movl	%r14d, %edx
	shrl	$3, %edx
	orl	%r10d, %ebx
	orl	%r9d, %ebx
	movl	%edx, %r9d
	sall	$9, %r9d
	orl	%r9d, %ebx
	movl	%r14d, %edi
	movl	%edx, %r9d
	sall	$10, %r9d
	shrl	%edi
	orl	%r9d, %ebx
	movl	%edi, %r8d
	movl	%edx, %r9d
	andl	$1, %r8d
	sall	$11, %r9d
	orl	%r9d, %ebx
	movl	%r14d, %esi
	leal	0(,%r8,8), %r9d
	orl	%r9d, %ebx
	shrl	$2, %esi
	movl	%r8d, %r9d
	movl	%esi, %eax
	sall	$4, %r9d
	andl	$1, %eax
	sall	$5, %r8d
	orl	%r9d, %ebx
	orl	%r8d, %ebx
	movl	%eax, %r8d
	sall	$6, %r8d
	orl	%r8d, %ebx
	movl	%eax, %r8d
	sall	$7, %r8d
	orl	%r8d, %ebx
	sall	$8, %eax
	orl	%eax, %ebx
	movl	$12, %r8d
	.p2align 4,,10
	.p2align 3
.L72:
	movl	%edx, 16(%rsp)
	movl	%esi, 12(%rsp)
	movl	%edi, 8(%rsp)
	movl	%r8d, 4(%rsp)
	call	rand@PLT
	addl	%r15d, %r15d
	cmpl	%eax, (%rsp)
	setge	%al
	movl	4(%rsp), %r8d
	movzbl	%al, %eax
	orl	%eax, %r15d
	decl	%r8d
	movl	8(%rsp), %edi
	movl	12(%rsp), %esi
	movl	16(%rsp), %edx
	jne	.L72
	xorl	%ebx, %r15d
	movl	%r15d, %eax
	shrl	%eax
	andl	$1, %eax
	movl	%eax, %r9d
	movl	%r15d, %eax
	shrl	$2, %eax
	andl	$1, %eax
	addl	%r9d, %eax
	movl	%r15d, %r9d
	andl	$1, %r9d
	addl	%r9d, %eax
	cmpl	$1, %eax
	movl	%r15d, %r10d
	seta	%al
	movl	%r15d, %r9d
	shrl	$3, %r10d
	movl	%r10d, %r11d
	shrl	$4, %r9d
	andl	$1, %r11d
	andl	$1, %r9d
	leal	(%r11,%r9), %r10d
	movl	%r15d, %r9d
	shrl	$5, %r9d
	movzbl	%al, %eax
	andl	$1, %r9d
	addl	%r10d, %r9d
	movl	%eax, %r10d
	orl	$2, %r10d
	cmpl	$1, %r9d
	cmova	%r10d, %eax
	movl	%r15d, %r10d
	shrl	$6, %r10d
	movl	%r15d, %r9d
	movl	%r10d, %r11d
	shrl	$7, %r9d
	andl	$1, %r9d
	andl	$1, %r11d
	leal	(%r11,%r9), %r10d
	movl	%r15d, %r9d
	shrl	$8, %r9d
	andl	$1, %r9d
	addl	%r10d, %r9d
	movl	%eax, %r10d
	orl	$4, %r10d
	movl	%r15d, %ebx
	cmpl	$1, %r9d
	cmova	%r10d, %eax
	shrl	$9, %ebx
	andl	$1, %ebx
	movl	%ebx, %r9d
	movl	%r15d, %ebx
	shrl	$10, %ebx
	andl	$1, %ebx
	shrl	$11, %r15d
	addl	%r9d, %ebx
	andl	$1, %r15d
	addl	%ebx, %r15d
	movl	%eax, %r9d
	orl	$8, %r9d
	cmpl	$1, %r15d
	cmova	%r9d, %eax
	movl	%edx, %ebx
	cmpl	%eax, %r14d
	setne	%al
	xorl	%edx, %esi
	xorl	%edi, %ebx
	xorl	%r14d, %ebx
	xorl	%esi, %edi
	andl	$1, %ebx
	andl	$1, %edi
	leal	0(,%r14,8), %edx
	xorl	%r14d, %esi
	sall	$2, %ebx
	orl	%edx, %edi
	andl	$1, %esi
	movzbl	%al, %eax
	movl	$7, %r15d
	orl	%edi, %ebx
	addl	%esi, %esi
	orl	%esi, %ebx
	addl	%eax, %ebp
	movl	%r15d, %eax
	movl	%r13d, %r15d
	movl	%r12d, %r13d
	movl	%ebx, %r12d
	movl	%eax, %ebx
	.p2align 4,,10
	.p2align 3
.L77:
	leal	(%r8,%r8), %eax
	movl	%eax, 4(%rsp)
	call	rand@PLT
	xorl	%r8d, %r8d
	cmpl	%eax, (%rsp)
	setge	%r8b
	orl	4(%rsp), %r8d
	decl	%ebx
	jne	.L77
	movl	%r12d, %ebx
	xorl	%r8d, %ebx
	movl	%ebx, %eax
	shrl	$4, %eax
	movl	%ebx, %edx
	shrl	$6, %edx
	movl	%eax, %esi
	movl	%ebx, %r8d
	shrl	$3, %r8d
	xorl	%edx, %esi
	xorl	%r8d, %esi
	andl	$1, %esi
	leal	0(,%rsi,4), %edi
	movl	%ebx, %esi
	shrl	$5, %esi
	xorl	%esi, %edx
	movl	%edx, %esi
	xorl	%r8d, %esi
	andl	$1, %esi
	xorl	%edx, %eax
	addl	%esi, %esi
	orl	%edi, %esi
	andl	$1, %eax
	movl	%ebx, %edx
	orl	%esi, %eax
	andl	$7, %edx
	xorl	%edx, %eax
	decl	%eax
	movl	%r13d, %r12d
	movl	%r15d, %r13d
	cmpl	$6, %eax
	ja	.L78
	leaq	CSWTCH.13(%rip), %rcx
	xorl	(%rcx,%rax,4), %ebx
	shrl	$3, %ebx
	movl	%ebx, %r8d
.L78:
	xorl	%eax, %eax
	cmpl	%r8d, %r14d
	setne	%al
	addl	%eax, %r13d
	decl	20(%rsp)
	jne	.L80
	movq	24(%rsp), %rdi
	xorl	%eax, %eax
	movl	%r13d, %r9d
	movl	%ebp, %r8d
	movl	%r12d, %ecx
	leaq	.LC5(%rip), %rdx
	movl	$1, %esi
	call	__fprintf_chk@PLT
	decl	32(%rsp)
	jne	.L69
	movq	24(%rsp), %rdi
	call	fclose@PLT
	incl	36(%rsp)
	movl	36(%rsp), %eax
	cmpl	$11, %eax
	jne	.L82
	xorl	%eax, %eax
.L65:
	movq	4152(%rsp), %rcx
	xorq	%fs:40, %rcx
	jne	.L96
	addq	$4168, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
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
.L95:
	.cfi_restore_state
	movq	40(%rsp), %rdx
	leaq	.LC8(%rip), %rsi
	movl	$1, %edi
	call	__printf_chk@PLT
	orl	$-1, %eax
	jmp	.L65
.L96:
	call	__stack_chk_fail@PLT
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
	.section	.rodata.cst32,"aM",@progbits,32
	.align 32
.LC1:
	.long	0
	.long	1
	.long	2
	.long	3
	.long	4
	.long	5
	.long	6
	.long	7
	.align 32
.LC2:
	.long	8
	.long	8
	.long	8
	.long	8
	.long	8
	.long	8
	.long	8
	.long	8
	.align 32
.LC3:
	.long	1
	.long	1
	.long	1
	.long	1
	.long	1
	.long	1
	.long	1
	.long	1
	.align 32
.LC4:
	.long	2
	.long	2
	.long	2
	.long	2
	.long	2
	.long	2
	.long	2
	.long	2
	.section	.rodata.cst8,"aM",@progbits,8
	.align 8
.LC9:
	.long	2576980378
	.long	1068079513
	.align 8
.LC10:
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
