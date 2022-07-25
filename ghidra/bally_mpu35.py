#create memory map for bally mpu35
#@author Arco van Geest
#@category Pinball
#@keybinding
#@menupath
#@toolbar

#import ghidra
from ghidra.program.model.data import PointerDataType,ByteDataType

# for decompiler
from ghidra.app.decompiler import DecompileOptions
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

#TODO: Add script code here
memory = currentProgram.getMemory()
listing = currentProgram.getListing()

def pia(piaaddress,pianame,piadescription):
    memory.createUninitializedBlock(pianame, toAddr(piaaddress),0x4, False)
    createLabel( toAddr(piaaddress),pianame+"_PDRA",True)
    createLabel( toAddr(piaaddress+1),pianame+"_CRA",True)
    createLabel( toAddr(piaaddress+2),pianame+"_PDRB",True)
    createLabel( toAddr(piaaddress+3),pianame+"_CRB",True)
    createData(toAddr(piaaddress), ByteDataType() )
    createData(toAddr(piaaddress+1), ByteDataType() )
    createData(toAddr(piaaddress+2), ByteDataType() )
    createData(toAddr(piaaddress+3), ByteDataType() )
    codeUnit = listing.getCodeUnitAt(toAddr(piaaddress))
    codeUnit.setComment(codeUnit.PLATE_COMMENT, "PIA MC6821 "+piadescription)



#fb = memory.getAllFileBytes()    

memory.createUninitializedBlock("RAM_U7", toAddr(0x0),0x80, False)
memory.createUninitializedBlock("RAM_U8", toAddr(0x200),0x100, False)

#memory.createUninitializedBlock("PIA_U10", toAddr(0x88),0x4, False)
#memory.createUninitializedBlock("PIA_U11", toAddr(0x90),0x4, False)

memory.createByteMappedBlock("vector_table",toAddr(0xFFF8),toAddr(0x5FF8),8,False)


pia(0x88,"PIA_U10","6821")
pia(0x90,"PIA_U11","6821")


#createLabel( toAddr(0x88),"PIA_U10_PDRA",True)
#createLabel( toAddr(0x89),"PIA_U10_CRA",True)
#createLabel( toAddr(0x8a),"PIA_U10_PDRB",True)
#createLabel( toAddr(0x8b),"PIA_U10_CRB",True)

#createLabel( toAddr(0x90),"PIA_U11_PDRA",True)
#createLabel( toAddr(0x91),"PIA_U11_CRA",True)
#createLabel( toAddr(0x92),"PIA_U11_PDRB",True)
#createLabel( toAddr(0x93),"PIA_U11_CRB",True)

createData(toAddr(0xFFF8), PointerDataType() )
createData(toAddr(0xFFFA), PointerDataType() )
createData(toAddr(0xFFFC), PointerDataType() )
createData(toAddr(0xFFFE), PointerDataType() )

createData(toAddr(0x5FF8), PointerDataType() )
createData(toAddr(0x5FFA), PointerDataType() )
createData(toAddr(0x5FFC), PointerDataType() )
createData(toAddr(0x5FFE), PointerDataType() )

irq_addr=(memory.getShort(toAddr(0x5FF8)) & 0xffff )
swi_addr=(memory.getShort(toAddr(0x5FFA)) & 0xffff )
nmi_addr=(memory.getShort(toAddr(0x5FFC)) & 0xffff )
reset_addr=(memory.getShort(toAddr(0x5FFE)) & 0xffff )

createFunction(toAddr(reset_addr),"FUN_RESET")
createFunction(toAddr(irq_addr),"FUN_IRQ")
#createFunction(toAddr(swi_addr),"FUN_SWI")
createFunction(toAddr(nmi_addr),"FUN_NMI")

disassemble(toAddr(reset_addr))
disassemble(toAddr(nmi_addr))
#disassemble(toAddr(swi_addr))
disassemble(toAddr(irq_addr))

print hex(reset_addr)

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