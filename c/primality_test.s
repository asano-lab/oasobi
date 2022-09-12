	.file	"primality_test.c"
	.text
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC4:
	.string	"%d\n"
.LC5:
	.string	"%f\n"
.LC6:
	.string	"%d,"
	.section	.text.startup,"ax",@progbits
	.p2align 4
	.globl	main
	.type	main, @function
main:
.LFB39:
	.cfi_startproc
	endbr64
	pushq	%r13
	.cfi_def_cfa_offset 16
	.cfi_offset 13, -16
	xorl	%esi, %esi
	pushq	%r12
	.cfi_def_cfa_offset 24
	.cfi_offset 12, -24
	movl	$3, %r12d
	pushq	%rbp
	.cfi_def_cfa_offset 32
	.cfi_offset 6, -32
	pushq	%rbx
	.cfi_def_cfa_offset 40
	.cfi_offset 3, -40
	movl	$1, %ebx
	subq	$4072, %rsp
	.cfi_def_cfa_offset 4112
	movq	%fs:40, %rax
	movq	%rax, 4056(%rsp)
	xorl	%eax, %eax
	leaq	16(%rsp), %rdi
	movl	$2, 48(%rsp)
	leaq	48(%rsp), %r13
	call	gettimeofday@PLT
	movsd	.LC0(%rip), %xmm1
	pxor	%xmm3, %xmm3
	movsd	.LC2(%rip), %xmm2
	.p2align 4,,10
	.p2align 3
.L2:
	addsd	%xmm2, %xmm1
	movl	%ebx, %ebp
	movq	%r13, %rsi
	leaq	0(%r13,%rbp,4), %r8
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
	movl	%r12d, %edx
	leaq	.LC6(%rip), %rsi
	xorl	%eax, %eax
	addl	$1, %ebx
	movl	$1, %edi
	call	__printf_chk@PLT
	movq	.LC2(%rip), %rax
	movl	%r12d, 48(%rsp,%rbp,4)
	pxor	%xmm3, %xmm3
	movq	%rax, %xmm2
.L6:
	addl	$1, %r12d
	cmpl	$1000, %ebx
	je	.L18
	movl	%r12d, %eax
	pxor	%xmm0, %xmm0
	cvtsi2sdq	%rax, %xmm0
	ucomisd	%xmm0, %xmm3
	movapd	%xmm0, %xmm1
	sqrtsd	%xmm1, %xmm1
	jbe	.L2
	movsd	%xmm1, (%rsp)
	call	sqrt@PLT
	movq	.LC2(%rip), %rax
	movsd	(%rsp), %xmm1
	pxor	%xmm3, %xmm3
	movq	%rax, %xmm2
	jmp	.L2
	.p2align 4,,10
	.p2align 3
.L18:
	movq	stdout(%rip), %rsi
	movl	$10, %edi
	call	putc@PLT
	xorl	%esi, %esi
	leaq	32(%rsp), %rdi
	call	gettimeofday@PLT
	pxor	%xmm1, %xmm1
	pxor	%xmm0, %xmm0
	xorl	%eax, %eax
	cvtsi2sdq	24(%rsp), %xmm1
	movsd	.LC3(%rip), %xmm2
	movl	4044(%rsp), %edx
	leaq	.LC4(%rip), %rsi
	cvtsi2sdq	16(%rsp), %xmm0
	movl	$1, %edi
	mulsd	%xmm2, %xmm1
	addsd	%xmm0, %xmm1
	pxor	%xmm0, %xmm0
	cvtsi2sdq	40(%rsp), %xmm0
	movsd	%xmm1, (%rsp)
	pxor	%xmm1, %xmm1
	cvtsi2sdq	32(%rsp), %xmm1
	mulsd	%xmm2, %xmm0
	addsd	%xmm1, %xmm0
	movsd	%xmm0, 8(%rsp)
	call	__printf_chk@PLT
	movsd	8(%rsp), %xmm0
	subsd	(%rsp), %xmm0
	leaq	.LC5(%rip), %rsi
	movl	$1, %edi
	movl	$1, %eax
	call	__printf_chk@PLT
	movq	4056(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L19
	addq	$4072, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 40
	xorl	%eax, %eax
	popq	%rbx
	.cfi_def_cfa_offset 32
	popq	%rbp
	.cfi_def_cfa_offset 24
	popq	%r12
	.cfi_def_cfa_offset 16
	popq	%r13
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
.LC2:
	.long	0
	.long	1072693248
	.align 8
.LC3:
	.long	2696277389
	.long	1051772663
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
