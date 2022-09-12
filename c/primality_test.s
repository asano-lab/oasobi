	.file	"primality_test.c"
	.text
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"%d\n"
	.section	.text.startup,"ax",@progbits
	.p2align 4
	.globl	main
	.type	main, @function
main:
.LFB39:
	.cfi_startproc
	endbr64
	pushq	%r14
	.cfi_def_cfa_offset 16
	.cfi_offset 14, -16
	leaq	.LC0(%rip), %r14
	pushq	%r13
	.cfi_def_cfa_offset 24
	.cfi_offset 13, -24
	pushq	%r12
	.cfi_def_cfa_offset 32
	.cfi_offset 12, -32
	movl	$3, %r12d
	pushq	%rbp
	.cfi_def_cfa_offset 40
	.cfi_offset 6, -40
	pushq	%rbx
	.cfi_def_cfa_offset 48
	.cfi_offset 3, -48
	movl	$1, %ebx
	subq	$1040, %rsp
	.cfi_def_cfa_offset 1088
	movq	%fs:40, %rax
	movq	%rax, 1032(%rsp)
	xorl	%eax, %eax
	movl	$2, (%rsp)
	movq	%rsp, %r13
	leaq	4(%rsp), %rbp
	.p2align 4,,10
	.p2align 3
.L2:
	leal	-1(%rbx), %eax
	movq	%r13, %rcx
	leaq	0(%rbp,%rax,4), %rsi
	.p2align 4,,10
	.p2align 3
.L4:
	movl	%r12d, %eax
	xorl	%edx, %edx
	divl	(%rcx)
	testl	%edx, %edx
	je	.L3
	addq	$4, %rcx
	cmpq	%rsi, %rcx
	jne	.L4
	movl	%r12d, %edx
	movq	%r14, %rsi
	movl	$1, %edi
	xorl	%eax, %eax
	call	__printf_chk@PLT
	movslq	%ebx, %rax
	addl	$1, %ebx
	movl	%r12d, (%rsp,%rax,4)
.L3:
	addl	$1, %r12d
	cmpl	$256, %ebx
	jne	.L2
	movq	1032(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L16
	addq	$1040, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 48
	xorl	%eax, %eax
	popq	%rbx
	.cfi_def_cfa_offset 40
	popq	%rbp
	.cfi_def_cfa_offset 32
	popq	%r12
	.cfi_def_cfa_offset 24
	popq	%r13
	.cfi_def_cfa_offset 16
	popq	%r14
	.cfi_def_cfa_offset 8
	ret
.L16:
	.cfi_restore_state
	call	__stack_chk_fail@PLT
	.cfi_endproc
.LFE39:
	.size	main, .-main
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
