	.file	"opt.c"
	.text
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"usage: %s <number>\n"
.LC1:
	.string	"%d > %d\n"
	.section	.text.startup,"ax",@progbits
	.p2align 4
	.globl	main
	.type	main, @function
main:
.LFB39:
	.cfi_startproc
	endbr64
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	cmpl	$1, %edi
	jle	.L6
	movq	8(%rsi), %rdi
	xorl	%edx, %edx
	xorl	%esi, %esi
	call	strtol@PLT
	leaq	.LC1(%rip), %rsi
	movl	$1, %edi
	movq	%rax, %rcx
	leal	1(%rax), %edx
	xorl	%eax, %eax
	call	__printf_chk@PLT
	xorl	%eax, %eax
.L1:
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 8
	ret
.L6:
	.cfi_restore_state
	movq	(%rsi), %rcx
	movq	stderr(%rip), %rdi
	movl	$1, %esi
	xorl	%eax, %eax
	leaq	.LC0(%rip), %rdx
	call	__fprintf_chk@PLT
	movl	$1, %eax
	jmp	.L1
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
