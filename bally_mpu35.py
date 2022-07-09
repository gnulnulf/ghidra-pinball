#create memory map for bally mpu35
#@author Arco van Geest
#@category Pinball
#@keybinding
#@menupath
#@toolbar

#import ghidra
from ghidra.program.model.data import PointerDataType

# for decompiler
from ghidra.app.decompiler import DecompileOptions
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

#TODO: Add script code here
memory = currentProgram.getMemory()
#fb = memory.getAllFileBytes()    

memory.createUninitializedBlock("RAM_U7", toAddr(0x0),0x80, False)
memory.createUninitializedBlock("RAM_U8", toAddr(0x200),0x100, False)

memory.createUninitializedBlock("PIA_U10", toAddr(0x88),0x4, False)
memory.createUninitializedBlock("PIA_U11", toAddr(0x90),0x4, False)

memory.createByteMappedBlock("vector_table",toAddr(0xFFF8),toAddr(0x5FF8),8,False)

createLabel( toAddr(0x88),"PIA_U10_PDRA",True)
createLabel( toAddr(0x89),"PIA_U10_CRA",True)
createLabel( toAddr(0x8a),"PIA_U10_PDRB",True)
createLabel( toAddr(0x8b),"PIA_U10_CRB",True)

createLabel( toAddr(0x90),"PIA_U11_PDRA",True)
createLabel( toAddr(0x91),"PIA_U11_CRA",True)
createLabel( toAddr(0x92),"PIA_U11_PDRB",True)
createLabel( toAddr(0x93),"PIA_U11_CRB",True)

createData(toAddr(0xFFF8), PointerDataType() )
createData(toAddr(0xFFFA), PointerDataType() )
createData(toAddr(0xFFFC), PointerDataType() )
createData(toAddr(0xFFFE), PointerDataType() )

createData(toAddr(0x5FF8), PointerDataType() )
createData(toAddr(0x5FFA), PointerDataType() )
createData(toAddr(0x5FFC), PointerDataType() )
createData(toAddr(0x5FFE), PointerDataType() )

irq_addr= reset_addr= (memory.getShort(toAddr(0x5FF8)) & 0xffff )
swi_addr= reset_addr= (memory.getShort(toAddr(0x5FFA)) & 0xffff )
nmi_addr= reset_addr= (memory.getShort(toAddr(0x5FFC)) & 0xffff )
reset_addr= reset_addr= (memory.getShort(toAddr(0x5FFE)) & 0xffff )

createFunction(toAddr(reset_addr),"FUN_RESET")
createFunction(toAddr(irq_addr),"FUN_IRQ")
#createFunction(toAddr(swi_addr),"FUN_SWI")
createFunction(toAddr(nmi_addr),"FUN_NMI")

disassemble(toAddr(reset_addr))
disassemble(toAddr(nmi_addr))
#disassemble(toAddr(swi_addr))
disassemble(toAddr(irq_addr))


# scratch 
'''
blk = memory.getBlock(toAddr(0x5800))
vectorbytes=[0]*8
blk.getBytes(toAddr(0x5FF8),vectorbytes)



memory.createInitializedBlock("vector_table", toAddr(0xFFF8),0x8,0, False)
blk2 = memory.getBlock(toAddr(0xFFF8))
for i in range(0,7):
    print i
    vectorbytes[i]=memory.getByte(toAddr(0x5FF8+i))
    memory.setByte(toAddr(0xFFF8+i),vectorbytes[i])
    
memory.createInitializedBlock("vector_table", toAddr(0xFFF8), fb[0], 16+0x800-8, 8 , False)
    

    blk2.putByte(toAddr(0xFFF8+i), vectorbyte)
    
memory.createByteMappedBlock("vector_table",toAddr(0xFFF8),toAddr(0x5FF8),8,False)
'''