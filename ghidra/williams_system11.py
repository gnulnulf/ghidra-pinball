#create memory map for williams system11
#@author Arco van Geest
#@category Pinball
#@keybinding
#@menupath
#@toolbar

#ROM_U26	4000	7fff	0x4000	true	true	true	false	false	Default	true	File: bk2k_u26.l4: 0x0	Binary Loader	
#ROM_U27	8000	ffff	0x8000	true	true	true	false	false	Default	true	File: bk2k_u27.l4: 0x0	Binary Loader	

#import ghidra
from ghidra.program.model.data import PointerDataType,ByteDataType

# for decompiler
from ghidra.app.decompiler import DecompileOptions
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

#comment
from ghidra.program.model.address.Address import *
from ghidra.program.model.listing.CodeUnit import *
from ghidra.program.model.listing.Listing import *

minAddress = currentProgram.getMinAddress()
listing = currentProgram.getListing()

codeUnit = listing.getCodeUnitAt(minAddress)
codeUnit.setComment(codeUnit.PLATE_COMMENT, "AddCommentToProgramScript - This is an added comment!")

memory = currentProgram.getMemory()
#fb = memory.getAllFileBytes()    

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


memory.createUninitializedBlock("RAM_U25", toAddr(0x0),0x800, False)


pia(0x2100,"PIA_U10","solenoid sound")
pia(0x3000,"PIA_U38","switch")
pia(0x2c00,"PIA_U41","ALFADISPLAY")
pia(0x3400,"PIA_U42","DISPLAY/WIDGET")
pia(0x2800,"PIA_U51","DISPLAY")
pia(0x2400,"PIA_U54","LAMPS")

listing.createData(toAddr(0xFFF8), PointerDataType() )
listing.createData(toAddr(0xFFFA), PointerDataType() )
listing.createData(toAddr(0xFFFC), PointerDataType() )
listing.createData(toAddr(0xFFFE), PointerDataType() )

irq_addr=(memory.getShort(toAddr(0xFFF8)) & 0xffff )
swi_addr= (memory.getShort(toAddr(0xFFFA)) & 0xffff )
nmi_addr=(memory.getShort(toAddr(0xFFFC)) & 0xffff )
reset_addr=(memory.getShort(toAddr(0xFFFE)) & 0xffff )

listing.createFunction(toAddr(reset_addr),"FUN_RESET",false)
createFunction(toAddr(irq_addr),"FUN_IRQ")
createFunction(toAddr(swi_addr),"FUN_SWI")
createFunction(toAddr(nmi_addr),"FUN_NMI")

disassemble(toAddr(reset_addr))
disassemble(toAddr(nmi_addr))
disassemble(toAddr(swi_addr))
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