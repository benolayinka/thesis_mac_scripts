	.section	__TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 13
	.globl	_bubble_sort            ## -- Begin function bubble_sort
_bubble_sort:                           ## @bubble_sort
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	pushq	%rbx
	.cfi_offset %rbx, -24
                                        ## kill: def %esi killed %esi def %rsi
	testl	%esi, %esi
	jle	LBB0_9
## %bb.1:
	leal	-1(%rsi), %r9d
	leaq	4(%rdi), %r8
	xorl	%r10d, %r10d
	movl	%r9d, %r11d
LBB0_2:                                 ## =>This Loop Header: Depth=1
                                        ##     Child Loop BB0_4 Depth 2
	movl	%r11d, %r11d
	movl	%r9d, %eax
	subl	%r10d, %eax
	testl	%eax, %eax
	jle	LBB0_8
## %bb.3:                               ##   in Loop: Header=BB0_2 Depth=1
	movl	(%rdi), %edx
	movq	%r11, %rcx
	movq	%r8, %rax
LBB0_4:                                 ##   Parent Loop BB0_2 Depth=1
                                        ## =>  This Inner Loop Header: Depth=2
	movl	(%rax), %ebx
	cmpl	%ebx, %edx
	jle	LBB0_5
## %bb.6:                               ##   in Loop: Header=BB0_4 Depth=2
	movl	%ebx, -4(%rax)
	movl	%edx, (%rax)
	jmp	LBB0_7
LBB0_5:                                 ##   in Loop: Header=BB0_4 Depth=2
	movl	%ebx, %edx
LBB0_7:                                 ##   in Loop: Header=BB0_4 Depth=2
	addq	$4, %rax
	decq	%rcx
	jne	LBB0_4
LBB0_8:                                 ##   in Loop: Header=BB0_2 Depth=1
	incl	%r10d
	decl	%r11d
	cmpl	%esi, %r10d
	jne	LBB0_2
LBB0_9:
	popq	%rbx
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function

.subsections_via_symbols
