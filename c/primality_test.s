	.file	"primality_test.c"
	.text
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC1:
	.string	"%d,%d\n"
	.section	.text.startup,"ax",@progbits
	.p2align 4
	.globl	main
	.type	main, @function
main:
.LFB39:
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
	leaq	-36864(%rsp), %r11
	.cfi_def_cfa 11, 36896
.LPSRL0:
	subq	$4096, %rsp
	orq	$0, (%rsp)
	cmpq	%r11, %rsp
	jne	.LPSRL0
	.cfi_def_cfa_register 7
	subq	$3200, %rsp
	.cfi_def_cfa_offset 40096
	xorl	%esi, %esi
	movl	$3, %r12d
	movl	$1, %ebx
	movq	%fs:40, %rax
	movq	%rax, 40056(%rsp)
	xorl	%eax, %eax
	leaq	16(%rsp), %rdi
	movl	$2, 48(%rsp)
	leaq	48(%rsp), %rbp
	call	gettimeofday@PLT
	movl	$2, %ecx
	movl	$1, %edx
	xorl	%eax, %eax
	leaq	.LC1(%rip), %rsi
	movl	$1, %edi
	call	__printf_chk@PLT
	movsd	.LC0(%rip), %xmm1
	pxor	%xmm3, %xmm3
	movsd	.LC3(%rip), %xmm2
	.p2align 4,,10
	.p2align 3
.L2:
	addsd	%xmm2, %xmm1
	movl	%ebx, %r9d
	movq	%rbp, %rsi
	leaq	0(%rbp,%r9,4), %r8
	cvttsd2siq	%xmm1, %rdi
	.p2align 4,,10
	.p2align 3
.L8:
	movl	(%rsi), %ecx
	movl	%r12d, %eax
	xorl	%edx, %edx
	divl	%ecx
	testl	%edx, %edx
	je	.L6
	cmpl	%edi, %ecx
	ja	.L7
	addq	$4, %rsi
	cmpq	%rsi, %r8
	jne	.L8
.L7:
	addl	$1, %ebx
	movl	%r12d, %ecx
	leaq	.LC1(%rip), %rsi
	xorl	%eax, %eax
	movl	%ebx, %edx
	movl	$1, %edi
	movl	%r12d, 48(%rsp,%r9,4)
	call	__printf_chk@PLT
	movq	.LC3(%rip), %rax
	pxor	%xmm3, %xmm3
	movq	%rax, %xmm2
.L6:
	addl	$1, %r12d
	cmpl	$10000, %ebx
	je	.L18
	movl	%r12d, %eax
	pxor	%xmm0, %xmm0
	cvtsi2sdq	%rax, %xmm0
	ucomisd	%xmm0, %xmm3
	movapd	%xmm0, %xmm1
	sqrtsd	%xmm1, %xmm1
	jbe	.L2
	movsd	%xmm1, 8(%rsp)
	call	sqrt@PLT
	movq	.LC3(%rip), %rax
	movsd	8(%rsp), %xmm1
	pxor	%xmm3, %xmm3
	movq	%rax, %xmm2
	jmp	.L2
	.p2align 4,,10
	.p2align 3
.L18:
	xorl	%esi, %esi
	leaq	32(%rsp), %rdi
	call	gettimeofday@PLT
	movq	40056(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L19
	addq	$40064, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 32
	xorl	%eax, %eax
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
.L19:
	.cfi_restore_state
	call	__stack_chk_fail@PLT
	.cfi_endproc
.LFE39:
	.size	main, .-main
	.section	.rodata.cst8,"aM",@progbits,8
	.align 8
.LC0:
	.long	3898100906
	.long	1073460858
	.align 8
.LC3:
	.long	0
	.long	1072693248
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
