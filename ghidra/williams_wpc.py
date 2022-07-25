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


memory.createUninitializedBlock("RAM_U8", toAddr(0x0),0x800, False)
#memory.createUninitializedBlock("RAM_DMD_WPC95a", toAddr(0x3000),0x400, False)
#memory.createUninitializedBlock("RAM_DMD_WPC95b", toAddr(0x3400),0x400, False)
memory.createUninitializedBlock("RAM_DMD", toAddr(0x3800),0x400, False)
memory.createUninitializedBlock("ASIC", toAddr(0x3C00),0x400, False)


#pia(0x2100,"PIA_U10","solenoid sound")
createLabel( toAddr(0x3D60),"WPC_DEBUG_DATA_PORT",True)
'''
WPC_DEBUG_DATA_PORT (0x3D60)
WPC_DEBUG_CONTROL_PORT (0x3D61)
WPC_SERIAL_CONTROL_PORT (0x3E66)
WPC_SERIAL_DATA_PORT (0x3E67)
WPC_DMD_3200_PAGE (0x3FB8) [WPC-95 only]
    3-0: W: The page of display RAM mapped into the 2nd region, from 0x3200-0x33FF.
WPC_DMD_3000_PAGE (0x3FB9) [WPC-95 only]
    3-0: W: The page of display RAM mapped into the 1st region, from 0x3000-0x31FF.
WPC_DMD_3600_PAGE (0x3FBA) [WPC-95 only]
WPC_DMD_3400_PAGE (0x3FBB) [WPC-95 only]
WPC_DMD_HIGH_PAGE (0x3FBC)
    3-0: W: The page of display RAM mapped into the 2nd (6th on WPC95) region, from 0x3A00-0x3BFF.
WPC_DMD_SCANLINE (0x3FBD)
    7-0: W: Request an FIRQ after a particular scanline is drawn 5-0: R: The last scanline that was drawn
WPC_DMD_LOW_PAGE 0x3FBE
    3-0: W: The page of display RAM mapped into the 1st (5th on WPC95) region, from 0x3800-0x39FF.
WPC_DMD_ACTIVE_PAGE 0x3FBF
    3-0: W: The page of display RAM to be used for refreshing the display. Writes to this register take effect just prior to drawing scanline 0.
WPC_PARALLEL_STATUS_PORT (0x3FC0)
WPC_PARALLEL_DATA_PORT (0x3FC1)
WPC_PARALLEL_STROBE_PORT (0x3FC2)
WPC_SERIAL_DATA_OUTPUT (0x3FC3)
WPC_SERIAL_CONTROL_OUTPUT (0x3FC4)
WPC_SERIAL_BAUD_SELECT (0x3FC5)
WPC_TICKET_DISPENSE (0x3FC6)
WPC_FLIPTRONIC_PORT_A (0x3FD4)
    7: W: Enable upper-left flipper hold 6: W: Enable upper-left flipper power 5: W: Enable upper-right flipper hold 4: W: Enable upper-right flipper power 3: W: Enable lower-left flipper hold 2: W: Enable lower-left flipper power 1: W: Enable lower-right flipper hold 0: W: Enable lower-right flipper power 7: R: Upper-left flipper EOS input 6: R: Upper-left flipper cabinet input 5: R: Upper-right flipper EOS input 4: R: Upper-right flipper cabinet input 3: R: Lower-left flipper EOS input 2: R: Lower-left flipper cabinet input 1: R: Lower-right flipper EOS input 0: R: Lower-right flipper cabinet input
WPC_FLIPTRONIC_PORT_B 0x3FD5
    Not used.
WPCS_DATA 0x3FDC
    7-0: R/W: Send/receive a byte of data to/from the sound board.
WPCS_CONTROL_STATUS 0x3FDD
    7: R: WPC sound board read ready 0: R: DCS sound board read ready
WPC_SOL_GEN_OUTPUT 0x3FE0
    7-0: W: Enables for solenoids 25-29
WPC_SOL_HIGHPOWER_OUTPUT 0x3FE1
    7-0: W: Enables for solenoids 1-8
WPC_SOL_FLASH1_OUTPUT 0x3FE2
    7-0: W: Enables for solenoids 17-24
WPC_SOL_LOWPOWER_OUTPUT 0x3FE3
    7-0: W: Enables for solenoids 9-16
WPC_LAMP_ROW_OUTPUT 0x3FE4
    7-0: W: Lamp matrix row output
WPC_LAMP_COL_STROBE 0x3FE5
    7-0: W: Lamp matrix column strobe At most one bit in this register should be set. If all are clear, then no controlled lamps are enabled.
WPC_GI_TRIAC 0x3FE6
    7: W: Flipper enable relay 5: W: Coin door enable relay 4-0: W: General illumination enables
WPC_SW_JUMPER_INPUT 0x3FE7
    7-0: R: Jumper/DIP switch inputs
WPC_SW_CABINET_INPUT 0x3FE8
    7: R: Fourth coin switch 6: R: Right coin switch 5: R: Center coin switch 4: R: Left coin switch 3: R: Enter (Begin Test) button 2: R: Up button 1: R: Down button 0: R: Escape (Service Credit) button
WPC_SW_ROW_INPUT 0x3FE9 *Pre-security
    7-0: R: Readings for the currently selected switch column. Bit 0 corresponds to row 1, bit 1 to row 2, and so on. A '1' indicates active voltage level. For a mechanical switch, this means the switch is closed. For an optical switch, this means the switch is open.
WPCS_PIC_READ 0x3FE9 *WPC-S
WPC_SW_COL_STROBE 0x3FEA *Pre-security
WPCS_PIC_WRITE 0x3FEA *WPC-S
    7-0: W: Switch column strobe. For pre-Security games, exactly one bit must be set. For Security games, writing to this register sends a command to the PIC chip and does not directly control the strobe line.
WPC_ALPHA_POS 0x3FEB *Alphanumeric
WPC_EXTBOARD1 0x3FEB *DMD
    On DMD games, this is a general I/O that is used for machine-specific purposes.
WPC_ALPHA_ROW1 0x3FEC *Alphanumeric
WPC_EXTBOARD2 0x3FEC *DMD
    On DMD games, this is a general I/O that is used for machine-specific purposes.
WPC_EXTBOARD3 0x3FED *DMD
    On DMD games, this is a general I/O that is used for machine-specific purposes.
WPC_ALPHA_ROW2 0x3FEE *Alphanumeric
WPC95_FLIPPER_COIL_OUTPUT 0x3FEE *WPC-95
WPC95_FLIPPER_SWITCH_INPUT 0x3FEF *WPC-95
WPC_LEDS 0x3FF2
    7: R/W : The state of the diagnostic LED. >0=Off >1=On
WPC_RAM_BANK 0x3FF3 *WPC-95
    3-0: W: The page of RAM currently mapped into the banked region.
WPC_SHIFTADDR 0x3FF4
    15-0: R/W: The base address for the bit shifter. Writing to this address initializes the shifter. Reading from this address after a shift command returns the shifted address.
WPC_SHIFTBIT 0x3FF6
    7-0: W: Sets the bit position for a shift command. 7-0: R: Returns the output of the last shift command as a bitmask.
WPC_SHIFTBIT2 0x3FF7
    7-0: R/W:
WPC_PERIPHERAL_TIMER_FIRQ_CLEAR 0x3FF8
WPC_ROM_LOCK 0x3FF9
    Not used
WPC_CLK_HOURS_DAYS 0x3FFA
    7-0: R/W : The time-of-day hour counter.
WPC_CLK_MINS 0x3FFB
    7-0: R/W : The time-of-day minute counter.
WPC_ROM_BANK 0x3FFC
    5-0: R/W: The page of ROM currently mapped into the banked region (0x4000-0x7FFF). Pages 62 and 63 correspond to the uppermost 32KB, and are not normally mapped because those pages are accessible in the fixed region (0x8000-0xFFFF). Page numbers are consecutive. Page 0 corresponds to the lowest address in a 1MB device. If a smaller ROM is installed, the uppermost bits of this register are effectively ignored.
WPC_RAM_LOCK 0x3FFD
WPC_RAM_LOCKSIZE 0x3FFE
WPC_ZEROCROSS_IRQ_CLEAR 0x3FFF
    7: R: Set to 1 when AC is currently at a zero crossing, or 0 otherwise. 7: W: Writing a 1 here clears the source of the periodic timer interrupt. 4: R/W: Periodic timer interrupt enable >0=Periodic IRQ disabled >1=Periodic IRQ enabled 2: W: Writing a 1 here resets the watchdog. 
'''
listing.createData(toAddr(0xFFF0), PointerDataType() )
listing.createData(toAddr(0xFFF2), PointerDataType() )
listing.createData(toAddr(0xFFF4), PointerDataType() )
listing.createData(toAddr(0xFFF6), PointerDataType() )
listing.createData(toAddr(0xFFF8), PointerDataType() )
listing.createData(toAddr(0xFFFA), PointerDataType() )
listing.createData(toAddr(0xFFFC), PointerDataType() )
listing.createData(toAddr(0xFFFE), PointerDataType() )

#reserved_addr= (memory.getShort(toAddr(0xFFF0)) & 0xffff )
swi3_addr= (memory.getShort(toAddr(0xFFF2)) & 0xffff )
swi2_addr= (memory.getShort(toAddr(0xFFF4)) & 0xffff )
firq_addr= (memory.getShort(toAddr(0xFFF6)) & 0xffff )
irq_addr= (memory.getShort(toAddr(0xFFF8)) & 0xffff )
swi_addr= (memory.getShort(toAddr(0xFFFA)) & 0xffff )
nmi_addr= (memory.getShort(toAddr(0xFFFC)) & 0xffff )
reset_addr= (memory.getShort(toAddr(0xFFFE)) & 0xffff )

listing.createFunction(toAddr(reset_addr),"FUN_RESET")
listing.createFunction(toAddr(irq_addr),"FUN_IRQ")
listing.createFunction(toAddr(firq_addr),"FUN_FIRQ")
listing.createFunction(toAddr(swi_addr),"FUN_SWI")
listing.createFunction(toAddr(swi2_addr),"FUN_SWI2")
listing.createFunction(toAddr(swi3_addr),"FUN_SWI3")
listing.createFunction(toAddr(nmi_addr),"FUN_NMI")

disassemble(toAddr(reset_addr))
disassemble(toAddr(nmi_addr))
disassemble(toAddr(irq_addr))
disassemble(toAddr(swi_addr))
disassemble(toAddr(swi2_addr))
disassemble(toAddr(swi3_addr))
disassemble(toAddr(firq_addr))


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