int get_control2(SMEE_UINT32 control_res_value)
{
    printf("%x", control_res_value);
    SMEE_UINT32 order = control_res_value & 0x7;
    switch (order)
    {
    case 0b1:
        printf("get IDB 8nc\n");
        break;
    case 0b100:
        printf("power Set\n");
        break;
    case 0b011:
        printf("image Scan\n");
        break;
    case 0b0:
        printf("get data\n");
        break;
    case 0b101:
        printf("flush IGB queue\n");
        break;
    case 0b10:
        printf("set ROI\n");
        break;

    default:
        printf("none\n");
        break;
    }
    control_res_value = control_res_value >> 4;
    //printf( std::hex << control_res_value << std::endl;
    SMEE_UINT32 order2 = control_res_value & 0x1;
    switch (order2)
    {
    case 0b0:
        printf("Flush N\n");
        break;
    case 0b1:
        printf("Flush Y\n");
        break;

    default:
        break;
    }
    control_res_value = control_res_value >> 1;
    //printf( std::hex << control_res_value << std::endl;
    SMEE_UINT32 order3 = control_res_value & 0x1;
    switch (order3)
    {
    case 0b0:
        printf("INTEGRATION N\n");
        break;
    case 0b1:
        printf("INTEGRATION Y\n");
        break;

    default:
        break;
    }
    control_res_value = control_res_value >> 1;
    SMEE_UINT32 order4 = control_res_value & 0b11;
    switch (order4)
    {
    case 0b0:
        printf("NO_TRANSFER\n");
        break;
    case 0b1:
        printf("PIXEL DATA\n");
        break;
    case 0b10:
        printf("TEST MODE\n");
        break;

    default:
        break;
    }
    control_res_value = control_res_value >> 2;
    SMEE_UINT32 order5 = control_res_value & 0b1111;
    printf( "SCAN ID:0x" << std::hex << order5 << std::endl;
    control_res_value = control_res_value >> 4;
    SMEE_UINT32 order6 = control_res_value & 0b11;
    switch (order6)
    {
    case 0b0:
        printf("IDB POWER DOWN\n");
        break;
    case 0b1:
        printf("IDB POWER idle\n");
        break;
    case 0b10:
        printf("IDB POWER active\n");
        break;

    default:
        break;
    }
    control_res_value = control_res_value >> 2;
    SMEE_UINT32 order7 = control_res_value & 0b1;
    switch (order7)
    {
    case 0b0:
        printf("none\n");
        break;
    case 0b1:
        printf("Refrush HSSL register\n");
        break;

    default:
        break;
    }
    return 0;
}
