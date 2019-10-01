	.section	__TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 13
	.globl	_bubble_sort            ## -- Begin function bubble_sort
	.p2align	4, 0x90
_bubble_sort:                           ## @bubble_sort
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	movq	%rdi, -8(%rbp)
	movl	%esi, -12(%rbp)
	movl	$0, -16(%rbp)
	movl	$0, -20(%rbp)
	movl	$0, -16(%rbp)
LBB0_1:                                 ## =>This Loop Header: Depth=1
                                        ##     Child Loop BB0_3 Depth 2
	movl	-16(%rbp), %eax
	cmpl	-12(%rbp), %eax
	jge	LBB0_10
## %bb.2:                               ##   in Loop: Header=BB0_1 Depth=1
	movl	$0, -20(%rbp)
LBB0_3:                                 ##   Parent Loop BB0_1 Depth=1
                                        ## =>  This Inner Loop Header: Depth=2
	movl	-20(%rbp), %eax
	movl	-12(%rbp), %ecx
	subl	-16(%rbp), %ecx
	subl	$1, %ecx
	cmpl	%ecx, %eax
	jge	LBB0_8
## %bb.4:                               ##   in Loop: Header=BB0_3 Depth=2
	movq	-8(%rbp), %rax
	movslq	-20(%rbp), %rcx
	movl	(%rax,%rcx,4), %edx
	movq	-8(%rbp), %rax
	movl	-20(%rbp), %esi
	addl	$1, %esi
	movslq	%esi, %rcx
	cmpl	(%rax,%rcx,4), %edx
	jle	LBB0_6
## %bb.5:                               ##   in Loop: Header=BB0_3 Depth=2
	movq	-8(%rbp), %rax
	movslq	-20(%rbp), %rcx
	movl	(%rax,%rcx,4), %edx
	movl	%edx, -24(%rbp)
	movq	-8(%rbp), %rax
	movl	-20(%rbp), %edx
	addl	$1, %edx
	movslq	%edx, %rcx
	movl	(%rax,%rcx,4), %edx
	movq	-8(%rbp), %rax
	movslq	-20(%rbp), %rcx
	movl	%edx, (%rax,%rcx,4)
	movl	-24(%rbp), %edx
	movq	-8(%rbp), %rax
	movl	-20(%rbp), %esi
	addl	$1, %esi
	movslq	%esi, %rcx
	movl	%edx, (%rax,%rcx,4)
LBB0_6:                                 ##   in Loop: Header=BB0_3 Depth=2
	jmp	LBB0_7
LBB0_7:                                 ##   in Loop: Header=BB0_3 Depth=2
	movl	-20(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -20(%rbp)
	jmp	LBB0_3
LBB0_8:                                 ##   in Loop: Header=BB0_1 Depth=1
	jmp	LBB0_9
LBB0_9:                                 ##   in Loop: Header=BB0_1 Depth=1
	movl	-16(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -16(%rbp)
	jmp	LBB0_1
LBB0_10:
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function

.subsections_via_symbols
