	.file	"primality_test.c"
	.text
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC1:
	.string	"%d\n"
.LC2:
	.string	"%f\n"
	.section	.text.startup,"ax",@progbits
	.p2align 4
	.globl	main
	.type	main, @function
main:
.LFB39:
	.cfi_startproc
	endbr64
	leaq	-397312(%rsp), %r11
	.cfi_def_cfa 11, 397320
.LPSRL0:
	subq	$4096, %rsp
	orq	$0, (%rsp)
	cmpq	%r11, %rsp
	jne	.LPSRL0
	.cfi_def_cfa_register 7
	subq	$2760, %rsp
	.cfi_def_cfa_offset 400080
	xorl	%esi, %esi
	movq	%fs:40, %rax
	movq	%rax, 400056(%rsp)
	xorl	%eax, %eax
	leaq	16(%rsp), %rdi
	movl	$2, 48(%rsp)
	call	gettimeofday@PLT
	movl	$3, %esi
	movl	$1, %r8d
	leaq	48(%rsp), %r10
	leaq	52(%rsp), %r9
	.p2align 4,,10
	.p2align 3
.L2:
	leal	-1(%r8), %eax
	movq	%r10, %rcx
	leaq	(%r9,%rax,4), %rdi
	.p2align 4,,10
	.p2align 3
.L4:
	movl	%esi, %eax
	xorl	%edx, %edx
	divl	(%rcx)
	testl	%edx, %edx
	je	.L3
	addq	$4, %rcx
	cmpq	%rdi, %rcx
	jne	.L4
	movslq	%r8d, %rax
	addl	$1, %r8d
	movl	%esi, 48(%rsp,%rax,4)
.L3:
	addl	$1, %esi
	cmpl	$100000, %r8d
	jne	.L2
	xorl	%esi, %esi
	leaq	32(%rsp), %rdi
	call	gettimeofday@PLT
	pxor	%xmm1, %xmm1
	pxor	%xmm0, %xmm0
	xorl	%eax, %eax
	cvtsi2sdq	24(%rsp), %xmm1
	movsd	.LC0(%rip), %xmm2
	movl	400044(%rsp), %edx
	leaq	.LC1(%rip), %rsi
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
	leaq	.LC2(%rip), %rsi
	movl	$1, %edi
	movl	$1, %eax
	call	__printf_chk@PLT
	movq	400056(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L16
	xorl	%eax, %eax
	addq	$400072, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 8
	ret
.L16:
	.cfi_restore_state
	call	__stack_chk_fail@PLT
	.cfi_endproc
.LFE39:
	.size	main, .-main
	.section	.rodata.cst8,"aM",@progbits,8
	.align 8
.LC0:
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
