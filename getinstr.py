#!/usr/bin/env python

#https://github.com/zeroepoch/ibatlvl/blob/master/lldb-trace.py

import sys, os
import argparse
from collections import OrderedDict
from tabulate import tabulate

class Call(object):
	def __init__(self, ins, target):
		self.opcode = str(ins.GetMnemonic(target))
		self.section_address = str(ins.GetAddress())
		self.file_address = ins.GetAddress().GetFileAddress()
		self.operands = str(ins.GetOperands(target))
		self.count = 1
		self.branch = ins.is_branch

class Calls():
	def __init__(self):
		self.calls = OrderedDict()

	def add_call(self, call):
		addr = call.file_address
		if self.calls.get(addr):
			self.calls.get(addr).count += 1
		else:
			self.calls[addr] = call

	def print_to_file(self,filename):
		with open(filename, 'w') as f:
			#f.write(tabulate(self.calls))
			for file_address,call in self.calls.items():
				f.write(str(hex(file_address)))
				f.write('\t')
				f.write(str(call.section_address))
				f.write('\t')
				f.write(str(call.opcode))
				f.write('\t')
				f.write(str(call.operands))
				f.write('\t')
				f.write(str(call.count))
				f.write('\t')
				f.write(str(call.branch))
				f.write('\n')

def main(binary = None, symbol= None, limit= None, triple = 'x86_64'):
	# lldb python path
	# LLDB_PYPATH = "/Applications/Xcode.app/Contents/SharedFrameworks/LLDB.framework/Versions/A/Resources/Python"
	LLDB_PYPATH = "/Library/Developer/CommandLineTools/Library/PrivateFrameworks/LLDB.framework/Resources/Python"

	# target parameters
	TARGET_PLATFORM = "host"
	REMOTE_URL = "connect://localhost:2159"

	# format target triple
	target_triple = triple + "-apple-macosx10.13.0"

	# check if symbol is usable
	if symbol and not binary:
	    sys.stderr.write(
	        "Error: Symbol argument given without binary argument!\n\n")
	    parser.print_help()
	    sys.exit(1)

	# import lldb library
	sys.path.append(LLDB_PYPATH)
	import lldb

	# create new debugger connection
	lldb.debugger = lldb.SBDebugger.Create()
	lldb.debugger.SetAsync(False)

	# get reusable lldb vars
	error = lldb.SBError()
	listener = lldb.debugger.GetListener()

	# setup lldb platform/target
	lldb.target = lldb.debugger.CreateTarget(binary, target_triple, TARGET_PLATFORM, True, error)
	if not lldb.target.IsValid() or not error.Success():
	    sys.stderr.write(
	        "Error: Failed to setup lldb platform/target!\n")
	    sys.exit(1)

	main = lldb.target.BreakpointCreateByName("main", lldb.target.GetExecutable().GetFilename())

	# connect to remote target
	# lldb.process = lldb.target.ConnectRemote(listener, REMOTE_URL, None, error)
	#lldb.process = lldb.target.LaunchSimple(None, None, os.getcwd())
	# lldb.process = lldb.target.Launch(listener=listener, argv=None, envp=None,
	# 									stdin_path=None, stdout_path=None, stderr_path=None, 
	# 									working_directory=os.getcwd(), launch_flags=None, stop_at_entry=False, error=error)
	lldb.process = lldb.target.Launch(listener, None, None,
	                                    None, None, None,
	                                    os.getcwd(), 0, False, error)
	if not lldb.process.IsValid() or not error.Success():
	    sys.stderr.write(
	        "Error: Failed to connect to remote target!\n")
	    sys.exit(1)

	# get active (only) thread
	lldb.thread = lldb.process.GetSelectedThread()
	if not lldb.thread.IsValid():
	    sys.stderr.write(
	        "Error: Failed to get currently active thread!\n")
	    sys.exit(1)

	# run until entry symbol
	if symbol:
	    breakpoint = lldb.target.BreakpointCreateByName(symbol, lldb.target.GetExecutable().GetFilename())
	    print breakpoint
	    lldb.process.Continue()

	# save start address
	start_addr = lldb.thread.GetSelectedFrame().addr

	insnCount = 0
	calls = Calls()

	while True:

	    # disasm next instruction
	    lldb.frame = lldb.thread.GetSelectedFrame()
	    insn = lldb.target.ReadInstructions(lldb.frame.addr, 1)[0]

	    if not (str(insn.addr).startswith(binary)):
	    	break
	    
	    insnCount += 1

	    # print instruction trace line
	    #print "%8d: %s" % (insnCount, insn)
	    #print insn.addr.symbol

	    call = Call(insn, lldb.target)
	    calls.add_call(call)

	    # step next instruction
	    lldb.thread.StepInstruction(False)
	    if lldb.thread.stop_reason != lldb.eStopReasonPlanComplete:
	        break
	    if lldb.thread.GetSelectedFrame().addr == start_addr:  # repeat
	        break

	    # check if instruction limit reached
	    if limit and (insnCount == limit):
	        break

	#sys.stderr.write("Trace Complete!\n")
	calls.print_to_file('out.txt')

if __name__ == '__main__':
	# parse command line args
	parser = argparse.ArgumentParser()
	parser.add_argument('-b', '--binary',
	    help='set binary being debugged on target')
	parser.add_argument('-s', '--symbol',
	    help='run until symbol before dumping')
	parser.add_argument('-l', '--limit', type=int,
	    help='limit number of instructions traced')
	parser.add_argument('-t', '--triple', default='x86_64',
	    help='target architecture for the binary')
	args = parser.parse_args()

	main(args.binary, args.symbol, args.limit, args.triple)