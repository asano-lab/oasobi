	.file	"primality_test.c"
	.text
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"%d: "
.LC1:
	.string	"smallest prime factor is %d\n"
.LC2:
	.string	"prime number"
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
	movl	$3, %r14d
	pushq	%r13
	.cfi_def_cfa_offset 24
	.cfi_offset 13, -24
	pushq	%r12
	.cfi_def_cfa_offset 32
	.cfi_offset 12, -32
	pushq	%rbp
	.cfi_def_cfa_offset 40
	.cfi_offset 6, -40
	leaq	.LC0(%rip), %rbp
	pushq	%rbx
	.cfi_def_cfa_offset 48
	.cfi_offset 3, -48
	movl	$1, %ebx
	subq	$416, %rsp
	.cfi_def_cfa_offset 464
	movq	%fs:40, %rax
	movq	%rax, 408(%rsp)
	xorl	%eax, %eax
	movl	$2, (%rsp)
	movq	%rsp, %r13
	leaq	4(%rsp), %r12
	.p2align 4,,10
	.p2align 3
.L5:
	movq	%rbp, %rsi
	movl	%r14d, %edx
	movl	$1, %edi
	xorl	%eax, %eax
	call	__printf_chk@PLT
	leal	-1(%rbx), %eax
	movq	%r13, %rcx
	leaq	(%r12,%rax,4), %rsi
	.p2align 4,,10
	.p2align 3
.L4:
	movl	(%rcx), %r8d
	movl	%r14d, %eax
	xorl	%edx, %edx
	divl	%r8d
	testl	%edx, %edx
	je	.L11
	addq	$4, %rcx
	cmpq	%rsi, %rcx
	jne	.L4
	leaq	.LC2(%rip), %rdi
	call	puts@PLT
	movslq	%ebx, %rax
	addl	$1, %ebx
	movl	%r14d, (%rsp,%rax,4)
.L3:
	addl	$1, %r14d
	cmpl	$100, %ebx
	jne	.L5
	movq	408(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L12
	addq	$416, %rsp
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
	.p2align 4,,10
	.p2align 3
.L11:
	.cfi_restore_state
	movl	%r8d, %edx
	leaq	.LC1(%rip), %rsi
	movl	$1, %edi
	xorl	%eax, %eax
	call	__printf_chk@PLT
	jmp	.L3
.L12:
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
