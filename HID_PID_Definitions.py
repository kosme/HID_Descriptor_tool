Main_Items={
    "Input"          : 0x80,
    "Output"         : 0x90,
    "Feature"        : 0xB0,
    "Collection"     : 0xA0,
    "End_Collection" : 0xC0,
}
Global_Items={
    "Usage_Page"       : 0x04,
    "Logical_Minimum"  : 0x14,
    "Logical_Maximum"  : 0x24,
    "Physical_Minimum" : 0x34,
    "Physical_Maximum" : 0x44,
    "Unit_Exponent"    : 0x54,
    "Unit"             : 0x64,
    "Report_Size"      : 0x74,
    "Report_ID"        : 0x84,
    "Report_Count"     : 0x94,
}
Local_Items={
    "Usage"         : 0x08,
    "Usage_Minimum" : 0x18,
    "Usage_Maximum" : 0x28,
}
IOF_Constants={
    "IOF_Array"         : 0x0,
    "IOF_ConstArry"     : 0x1,
    "IOF_Variable"      : 0x2,
    "IOF_ConstVar"      : 0x3,
    "IOF_VarRelArry"    : 0x6,
    "IOF_VarNoPreferred": 0x22,
    "IOF_VariableBuffer": 0x0102,
    "IOF_Constant"      : 0x01,
    "IOF_Absolute"      : 0x00,
    "IOF_Array"         : 0x00,
    "IOF_Relative"      : 0x04,
    "IOF_Wrap"          : 0x08,
    "IOF_Non_Linear"    : 0x10,
    "IOF_No_Prefered"   : 0x20,
    "IOF_Null_State"    : 0x40,
    "IOF_Volatile"      : 0x80,
}
Clc_Constants={
    "Clc_Physical"     : 0x00,
    "Clc_Application"  : 0x01,
    "Clc_Logical"      : 0x02,
    "Clc_Report"       : 0x03,
    "Clc_Named_Array"  : 0x04,
    "Clc_Usage_Switch" : 0x05,
}
Unit_Constants={
    "Eng_Lin_Time": 0x1003,
    "Eng_Rot_Angular_Pos": 0x14,
    "Unit_None" : 0x00,
}
Usage_Page_Constants={
    "Generic_Desktop_ID" : 0x01,
    "Simulation_ID"      : 0x02,
    "Generic_device_ID"  : 0x06,
    "Key_Codes_ID"       : 0x07,
    "LEDS_ID"            : 0x08,
    "Button_ID"          : 0x09,
    "Ordinal_ID"         : 0x0A,
    "Consumer_Page_ID"   : 0x0C,
    "Digitizer_Page_ID"  : 0x0D,
    "Physical_Interface" : 0x0F,
    "Vendor_Defined_ID"  : 0xFF,
    "Undefined_0xffbc_ID": 0xFFBC,
    "Undefined_0xff00_ID": 0xFF00,
    "Undefined_0xff01_ID": 0xFF01,
}

Exponents_Constants={
    "0"     : 0x00,
    "1"     : 0x01,
    "2"     : 0x02,
    "3"     : 0x03,
    "4"     : 0x04,
    "5"     : 0x05,
    "6"     : 0x06,
    "7"     : 0x07,
    "-8"    : 0x08,
    "-7"    : 0x09,
    "-6"    : 0x0a,
    "-5"    : 0x0b,
    "-4"    : 0x0c,
    "-3"    : 0x0d,
    "-2"    : 0x0e,
    "-1"    : 0x0f,
}
GenericDesktop_Constants={
#Generic Desktop Page
    "Pointer_ID"        : 0x01,
    "Mouse_ID"          : 0x02,
    "Joystick_ID"       : 0x04,
    "Game_Pad_ID"       : 0x05,
    "Keyboard_ID"       : 0x06,
    "Multi-Axis_ID"     : 0x08,
    "X_ID"              : 0x30,
    "Y_ID"              : 0x31,
    "Z_ID"              : 0x32,
    "Rx_ID"             : 0x33,
    "Ry_ID"             : 0x34,
    "Rz_ID"             : 0x35,
    "Dial_ID"           : 0x37,
    "Wheel_ID"          : 0x38,
    "Byte_Count"        : 0x3B,
    "Start_ID"          : 0x3D,
    "Reserved_0x55_ID"  : 0x55,
    "System_Control_ID" : 0x80,
    "System_sleep_ID"   : 0x82,
}
SimulationControl_Constants={
#Simulation Control Page
    "Throttle_ID"  : 0xBB,
}
LED_Constants={

}

Genericdevice_Constants={

}

Button_Constants={
#Button Usage Page
    "No_botton_ID" : 0x00,
    "Button1_ID"   : 0x01,
    "Button2_ID"   : 0x02,
    "Button3_ID"   : 0x03,
    "Button4_ID"   : 0x04,
    "Button5_ID"   : 0x05,
}
Ordinal_Constants={
    "Instance_1" : 0x01,
    "Instance_2" : 0x02,
}
Consumer_Constants={
    "Consumer_Control_ID"   : 0x01,
    "Power_ID"              : 0x30,
    "Undef_0x6F_ID"         : 0x6f,
    "Undef_0x70_ID"         : 0x70,
    "Scan_next_track_ID"       : 0xB5,
    "Scan_previous_track_ID"       : 0xB6,
    "Eject_ID"       : 0xB8,
    "Play_Pause_ID"         : 0xCD,
    "Mute_ID"               : 0xE2,
    "Volume_Incement_ID"    : 0xE9,
    "Volume_Decrement_ID"   : 0xEA,
    "App_launcher_ID"       : 0x0180,
    "Programmable_Button_Config__ID"       : 0x0182,
    "Email_Reader_ID"       : 0x018A,
    "Internet_Browser_ID"   : 0x0196,
    "Select_Task_ID"        : 0x01A2,
    "Next_Task_ID"          : 0x01A3,
    "Prev_Task_ID"          : 0x01A4,
    "Dictionary_ID"         : 0x01A9,
    "Desktop_ID"            : 0x01AA,
    "Keyboard_layout_ID"    : 0x01AE,
    "File_Explorer_ID"      : 0x01B4,
    "AL_Reserved"           : 0x01BB,
    "Generic_GUI_Ctrl_ID"   : 0x0200,
    "AC_Find_ID"            : 0x021F,
    "AC_Search_ID"          : 0x0221,
    "AC_Home_ID"            : 0x0223,
    "Refresh_ID"            : 0x0227,
    "Zoom_In_ID"            : 0x022D,
    "Zoom_Out_ID"           : 0x022E,
    "Zoom_ID"               : 0x022F,
    "Scroll_Up_ID"          : 0x0233,
    "Scroll_Down_ID"        : 0x0234,
    "Scroll_ID"             : 0x0235,
    "Pan_Left_ID"           : 0x0236,
    "Pan_Right_ID"          : 0x0237,
    "Pan_ID"                : 0x0238,
    "Rotate_ID"             : 0x0245,
    "Distribute_Horiz_ID"   : 0x029B,
    "Distribute_Vert_ID"    : 0x029C,
    "Reserved_0x307_ID"     : 0x0307,
}

Digitizer_Constants = {
    "Digitizer_ID"          : 0x01,
    "Pen_ID"                : 0x02,
    "Light_pen_ID"          : 0x03,
    "Touchscreen_ID"        : 0x04,
    "Stylus_ID"             : 0x20,
    "Finger_ID"             : 0x22,
    "In_Range_ID"           : 0x32,
    "Tip_Switch_ID"         : 0x42,
    "Contact_Ident_ID"      : 0x51,
    "Contact_Count_ID"      : 0x54,
    "Contact_Count_MAx_ID"  : 0x55,
}
#PID usages from \
#Device Class Definition for Physical Interface Devices (PID) Version 1.0
#Table 2: Physical Input Device Page
PID_Usage_Constants={
    "PID_Undefined"                        : 0x00,
    "PID_Physical_Interface_Device"        : 0x01,
    "PID_Normal"                           : 0x20,
    "PID_Set_Effect_Report"                : 0x21,
    "PID_Effect_Block_Index"               : 0x22,
    "PID_Parameter_Block_Offset"           : 0x23,
    "PID_ROM_Flag"                         : 0x24,
    "PID_Effect_Type"                      : 0x25,
    "PID_ET_Constant_Force"                : 0x26,
    "PID_ET_Ramp"                          : 0x27,
    "PID_ET_Custom_Force_Data"             : 0x28,
    "PID_ET_Square"                        : 0x30,
    "PID_ET_Sine"                          : 0x31,
    "PID_ET_Triangle"                      : 0x32,
    "PID_ET_Sawtooth_Up"                   : 0x33,
    "PID_ET_Sawtooth_Down"                 : 0x34,
    "PID_ET_Spring"                        : 0x40,
    "PID_ET_Damper"                        : 0x41,
    "PID_ET_Inertia"                       : 0x42,
    "PID_ET_Friction"                      : 0x43,
    "PID_Duration"                         : 0x50,
    "PID_Sample_Period"                    : 0x51,
    "PID_Gain"                             : 0x52,
    "PID_Trigger_Button"                   : 0x53,
    "PID_Trigger_Repeat_Interval"          : 0x54,
    "PID_Axes_Enable"                      : 0x55,
    "PID_Direction_Enable"                 : 0x56,
    "PID_Direction"                        : 0x57,
    "PID_Type_Specific_Block_Offset"       : 0x58,
    "PID_Block_Type"                       : 0x59,
    "PID_Set_Envelope_Report"              : 0x5A,
    "PID_Attack_Level"                     : 0x5B,
    "PID_Attack_Time"                      : 0x5C,
    "PID_Fade_Level"                       : 0x5D,
    "PID_Fade_Time"                        : 0x5E,
    "PID_Set_Condition_Report"             : 0x5F,
    "PID_CP_Offset"                        : 0x60,
    "PID_Positive_Coefficient"             : 0x61,
    "PID_Negative_Coefficient"             : 0x62,
    "PID_Positive_Saturation"              : 0x63,
    "PID_Negative_Saturation"              : 0x64,
    "PID_Dead_Band"                        : 0x65,
    "PID_Download_Force_Sample"            : 0x66,
    "PID_Isoch_Custom_Force_Enable"        : 0x67,
    "PID_Custom_Force_Data_Report"         : 0x68,
    "PID_Custom_Force_Data"                : 0x69,
    "PID_Custom_Force_Vendor_Defined_Data" : 0x6A,
    "PID_Set_Custom_Force_Report"          : 0x6B,
    "PID_Custom_Force_Data_Offset"         : 0x6C,
    "PID_Sample_Count"                     : 0x6D,
    "PID_Set_Periodic_Report"              : 0x6E,
    "PID_Offset"                           : 0x6F,
    "PID_Magnitude"                        : 0x70,
    "PID_Phase"                            : 0x71,
    "PID_Period"                           : 0x72,
    "PID_Set_Constant_Force_Report"        : 0x73,
    "PID_Set_Ramp_Force_Report"            : 0x74,
    "PID_Ramp_Start"                       : 0x75,
    "PID_Ramp_End"                         : 0x76,
    "PID_Effect_Operation_Report"          : 0x77,
    "PID_Effect_Operation"                 : 0x78,
    "PID_Op_Effect_Start"                  : 0x79,
    "PID_Op_Effect_Start_Solo"             : 0x7A,
    "PID_Op_Effect_Stop"                   : 0x7B,
    "PID_Loop_Count"                       : 0x7C,
    "PID_Device_Gain_Report"               : 0x7D,
    "PID_Device_Gain"                      : 0x7E,
    "PID_PID_Pool_Report"                  : 0x7F,
    "PID_RAM_Pool_Size"                    : 0x80,
    "PID_ROM_Pool_Size"                    : 0x81,
    "PID_ROM_Effect_Block_Count"           : 0x82,
    "PID_Simultaneous_Effects_Max"         : 0x83,
    "PID_Pool_Alignment"                   : 0x84,
    "PID_PID_Pool_Move_Report"             : 0x85,
    "PID_Move_Source"                      : 0x86,
    "PID_Move_Destination"                 : 0x87,
    "PID_Move_Length"                      : 0x88,
    "PID_PID_Block_Load_Report"            : 0x89,
    "PID_Block_Load_Status"                : 0x8B,
    "PID_Block_Load_Success"               : 0x8C,
    "PID_Block_Load_Full"                  : 0x8D,
    "PID_Block_Load_Error"                 : 0x8E,
    "PID_Block_Handle"                     : 0x8F,
    "PID_PID_Block_Free_Report"            : 0x90,
    "PID_Type_Specific_Block_Handle"       : 0x91,
    "PID_PID_State_Report"                 : 0x92,
    "PID_Effect_Playing"                   : 0x94,
    "PID_PID_Device_Control_Report"        : 0x95,
    "PID_PID_Device_Control"               : 0x96,
    "PID_DC_Enable_Actuators"              : 0x97,
    "PID_DC_Disable_Actuators"             : 0x98,
    "PID_DC_Stop_All_Effects"              : 0x99,
    "PID_DC_Device_Reset"                  : 0x9A,
    "PID_DC_Device_Pause"                  : 0x9B,
    "PID_DC_Device_Continue"               : 0x9C,
    "PID_Device_Paused"                    : 0x9F,
    "PID_Actuators_Enabled"                : 0xA0,
    "PID_Safety_Switch"                    : 0xA4,
    "PID_Actuator_Override_Switch"         : 0xA5,
    "PID_Actuator_Power"                   : 0xA6,
    "PID_Start_Delay"                      : 0xA7,
    "PID_Parameter_Block_Size"             : 0xA8,
    "PID_Device_Managed_Pool"              : 0xA9,
    "PID_Shared_Parameter_Blocks"          : 0xAA,
    "PID_Create_New_Effect_Report"         : 0xAB,
    "PID_RAM_Pool_Available"               : 0xAC,
}
Vendor_Constants={
    "Usage_1" : 0x01,
    "Usage_2" : 0x02,
}
_0xffbc_Constants={

}
_0xff00_Constants={

}
_0xff01_Constants={

}
HID_Items=[Main_Items,Global_Items,Local_Items]
HID_Constants=[
    GenericDesktop_Constants,
    SimulationControl_Constants,
    LED_Constants,
    Button_Constants,
    Usage_Page_Constants,
    Unit_Constants,
    Clc_Constants,
    IOF_Constants,
    PID_Usage_Constants,
    Ordinal_Constants,
    Consumer_Constants,
    Digitizer_Constants,
    Vendor_Constants,
]
UsageByPage={
    "Generic_Desktop_ID" : GenericDesktop_Constants,
    "Simulation_ID"      : SimulationControl_Constants,
    "Generic_device_ID"  : Genericdevice_Constants,
    "LEDS_ID"            : LED_Constants,
    "Button_ID"          : Button_Constants,
    "Physical_Interface" : PID_Usage_Constants,
    "Consumer_Page_ID"   : Consumer_Constants,
    "Digitizer_Page_ID"  : Digitizer_Constants,
    "Ordinal_ID"         : Ordinal_Constants,
    "Vendor_Defined_ID"  : Vendor_Constants,
    "Undefined_0xffbc_ID": _0xffbc_Constants,
    "Undefined_0xff00_ID": _0xff00_Constants,
    "Undefined_0xff01_ID": _0xff01_Constants,
}
ConstByItem={
    "Input"          : IOF_Constants,
    "Output"         : IOF_Constants,
    "Feature"        : IOF_Constants,
    "Collection"     : Clc_Constants,
    "End_Collection" : {},
    "Usage_Page"       : Usage_Page_Constants,
    "Logical_Minimum"  : {},
    "Logical_Maximum"  : {},
    "Physical_Minimum" : {},
    "Physical_Maximum" : {},
    "Unit_Exponent"    : Exponents_Constants,
    "Unit"             : Unit_Constants,
    "Report_Size"      : {},
    "Report_ID"        : {},
    "Report_Count"     : {},
    "Usage"         : {},
    "Usage_Minimum" : {},
    "Usage_Maximum" : {},
}
