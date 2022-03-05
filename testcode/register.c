#include <stdio.h>
#define SMEE_UINT32 unsigned int
SMEE_UINT32 control_res_value;
SMEE_UINT32 status_res_value;
int get_status(SMEE_UINT32 status_res_value)
{
    printf("%x\n", status_res_value);
    SMEE_UINT32 order0 = status_res_value & 0b1;
    printf("%x\n", order0);
    switch (order0)
    {

    case 0b0:
        printf("idle Requesting 12NC from IGB and IDB\n");
        break;
    case 0b1:
        printf("busy Requesting 12NC from IGB and IDB\n");
        break;
    }
    status_res_value = status_res_value >> 1;
    //printf( std::hex << status_res_value ");
    SMEE_UINT32 order1 = status_res_value & 0b1;
    //printf( order1 );
    switch (order1)
    {

    case 0b0:
        printf("idle Setting Region of interest (ROI) on IDB\n");
        break;
    case 0b1:
        printf("busy Setting Region of interest (ROI) on IDB\n");
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order2 = status_res_value & 0b1;
    switch (order2)
    {

    case 0b0:
        printf("not Waiting for HSSL trigger\n");
        break;
    case 0b1:
        printf("Waiting for HSSL trigger\n");
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order3 = status_res_value & 0b1;
    switch (order3)
    {

    case 0b0:
        printf("idle Flushing camera pixels on IDB\n");
        break;
    case 0b1:
        printf("busy Flushing camera pixels on IDB\n");
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order4 = status_res_value & 0b1;
    switch (order4)
    {

    case 0b0:
        printf("idle Waiting for integration time (INT TIME) to expire\n");
        break;
    case 0b1:
        printf("busy Waiting for integration time (INT TIME) to expire\n");
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order5 = status_res_value & 0b1;
    switch (order5)
    {

    case 0b0:
        printf("Trig is not send within the delay time\n");
        break;
    case 0b1:
        printf("Trig is send within the delay time\n");
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order6 = status_res_value & 0b1;
    switch (order6)
    {

    case 0b0:
        printf("IDB not connected\n");
        break;
    case 0b1:
        printf("IDB connected and ready\n");
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order7 = status_res_value & 0b1;
    switch (order7)
    {

    case 0b0:
        printf("Trig is not send within the idb reset time\n");
        break;
    case 0b1:
        printf("Trig is send within the idb reset time\n");
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order8 = status_res_value & 0b11;
    switch (order8)
    {

    case 0b0:
        printf("no command response\n");
        break;
    case 0b1:
        printf("ACK command response\n");
        break;
    case 0b10:
        printf("NAK command response\n");
        break;
    }
    status_res_value = status_res_value >> 2;
    SMEE_UINT32 order10 = status_res_value & 0b1;
    switch (order10)
    {

    case 0b0:
        printf("Scan FIFO not empty  on IGB\n");
        break;
    case 0b1:
        printf("Scan FIFO empty status on IGB\n");
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order11 = status_res_value & 0b1;
    switch (order11)
    {

    case 0b0:
        printf("Scan FIFO not full on IGB\n");
        break;
    case 0b1:
        printf("Scan FIFO full on IGB\n");
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order12 = status_res_value & 0b1;
    switch (order12)
    {

    case 0b0:
        printf("OK IDB 3V3 power supply status on IGB\n");
        break;
    case 0b1:
        printf("Fail IDB 3V3 power supply status on IGB\n");
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order13 = status_res_value & 0b1;
    switch (order13)
    {

    case 0b0:
        printf("OK IDB 5V power supply status on IGB\n");
        break;
    case 0b1:
        printf("Fail IDB 5V power supply status on IGB\n");
        break;
    }
    status_res_value = status_res_value >> 3;
    SMEE_UINT32 order16 = status_res_value & 0b11;
    switch (order16)
    {

    case 0b0:
        printf("IGB QUEUE empty\n");
        break;
    case 0b1:
        printf("IGB QUEUE half full\n");
        break;
    case 0b10:
        printf("IGB QUEUE partly full\n");
        break;
    case 0b11:
        printf("IGB QUEUE full\n");
        break;
    }
    status_res_value = status_res_value >> 2;
    SMEE_UINT32 order18 = status_res_value & 0b1;
    switch (order18)
    {

    case 0b0:
        printf("IGB power fail\n");
        break;
    case 0b1:
        printf("IGB power ok\n");
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order19 = status_res_value & 0b1;
    switch (order19)
    {

    case 0b0:
        printf("IDB power fail\n");
        break;
    case 0b1:
        printf("IDB power ok\n");
        break;
    }
    return 0;
}
int get_control(SMEE_UINT32 control_res_value)
{
    printf("control_res_value: %x\n", control_res_value);
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
    //printf( std::hex << control_res_value );
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
    //printf( std::hex << control_res_value );
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
    printf("SCAN ID:0x%x\n", order5);
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

int main()
{

    control_res_value = 0x2012;
    get_control(control_res_value);

    return 0;
}