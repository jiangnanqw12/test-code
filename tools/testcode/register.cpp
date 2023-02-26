#include <iostream>
#include <stdio.h>
#define SMEE_UINT32 uint32_t
SMEE_UINT32 control_res_value;
SMEE_UINT32 status_res_value;
int get_status(SMEE_UINT32 status_res_value)
{
    std::cout << std::hex << "0x" << status_res_value << std::endl;
    SMEE_UINT32 order0 = status_res_value & 0b1;
    std::cout << order0 << std::endl;
    switch (order0)
    {

    case 0b0:
        std::cout << "idle Requesting 12NC from IGB and IDB" << std::endl;
        break;
    case 0b1:
        std::cout << "busy Requesting 12NC from IGB and IDB" << std::endl;
        break;
    }
    status_res_value = status_res_value >> 1;
    //std::cout << std::hex << status_res_value << std::endl;
    SMEE_UINT32 order1 = status_res_value & 0b1;
    //std::cout << order1 << std::endl;
    switch (order1)
    {

    case 0b0:
        std::cout << "idle Setting Region of interest (ROI) on IDB" << std::endl;
        break;
    case 0b1:
        std::cout << "busy Setting Region of interest (ROI) on IDB" << std::endl;
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order2 = status_res_value & 0b1;
    switch (order2)
    {

    case 0b0:
        std::cout << "not Waiting for HSSL trigger" << std::endl;
        break;
    case 0b1:
        std::cout << "Waiting for HSSL trigger" << std::endl;
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order3 = status_res_value & 0b1;
    switch (order3)
    {

    case 0b0:
        std::cout << "idle Flushing camera pixels on IDB" << std::endl;
        break;
    case 0b1:
        std::cout << "busy Flushing camera pixels on IDB" << std::endl;
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order4 = status_res_value & 0b1;
    switch (order4)
    {

    case 0b0:
        std::cout << "idle Waiting for integration time (INT TIME) to expire" << std::endl;
        break;
    case 0b1:
        std::cout << "busy Waiting for integration time (INT TIME) to expire" << std::endl;
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order5 = status_res_value & 0b1;
    switch (order5)
    {

    case 0b0:
        std::cout << "Trig is not send within the delay time" << std::endl;
        break;
    case 0b1:
        std::cout << "Trig is send within the delay time" << std::endl;
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order6 = status_res_value & 0b1;
    switch (order6)
    {

    case 0b0:
        std::cout << "IDB not connected" << std::endl;
        break;
    case 0b1:
        std::cout << "IDB connected and ready" << std::endl;
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order7 = status_res_value & 0b1;
    switch (order7)
    {

    case 0b0:
        std::cout << "Trig is not send within the idb reset time" << std::endl;
        break;
    case 0b1:
        std::cout << "Trig is send within the idb reset time" << std::endl;
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order8 = status_res_value & 0b11;
    switch (order8)
    {

    case 0b0:
        std::cout << "no command response" << std::endl;
        break;
    case 0b1:
        std::cout << "ACK command response" << std::endl;
        break;
    case 0b10:
        std::cout << "NAK command response" << std::endl;
        break;
    }
    status_res_value = status_res_value >> 2;
    SMEE_UINT32 order10 = status_res_value & 0b1;
    switch (order10)
    {

    case 0b0:
        std::cout << "Scan FIFO not empty  on IGB" << std::endl;
        break;
    case 0b1:
        std::cout << "Scan FIFO empty status on IGB" << std::endl;
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order11 = status_res_value & 0b1;
    switch (order11)
    {

    case 0b0:
        std::cout << "Scan FIFO not full on IGB" << std::endl;
        break;
    case 0b1:
        std::cout << "Scan FIFO full on IGB" << std::endl;
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order12 = status_res_value & 0b1;
    switch (order12)
    {

    case 0b0:
        std::cout << "OK IDB 3V3 power supply status on IGB" << std::endl;
        break;
    case 0b1:
        std::cout << "Fail IDB 3V3 power supply status on IGB" << std::endl;
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order13 = status_res_value & 0b1;
    switch (order13)
    {

    case 0b0:
        std::cout << "OK IDB 5V power supply status on IGB" << std::endl;
        break;
    case 0b1:
        std::cout << "Fail IDB 5V power supply status on IGB" << std::endl;
        break;
    }
    status_res_value = status_res_value >> 3;
    SMEE_UINT32 order16 = status_res_value & 0b11;
    switch (order16)
    {

    case 0b0:
        std::cout << "IGB QUEUE empty" << std::endl;
        break;
    case 0b1:
        std::cout << "IGB QUEUE half full" << std::endl;
        break;
    case 0b10:
        std::cout << "IGB QUEUE partly full" << std::endl;
        break;
    case 0b11:
        std::cout << "IGB QUEUE full" << std::endl;
        break;
    }
    status_res_value = status_res_value >> 2;
    SMEE_UINT32 order18 = status_res_value & 0b1;
    switch (order18)
    {

    case 0b0:
        std::cout << "IGB power fail" << std::endl;
        break;
    case 0b1:
        std::cout << "IGB power ok" << std::endl;
        break;
    }
    status_res_value = status_res_value >> 1;
    SMEE_UINT32 order19 = status_res_value & 0b1;
    switch (order19)
    {

    case 0b0:
        std::cout << "IDB power fail" << std::endl;
        break;
    case 0b1:
        std::cout << "IDB power ok" << std::endl;
        break;
    }
    return 0;
}
int get_control(SMEE_UINT32 control_res_value)
{
    std::cout << std::hex << "0x" << control_res_value << std::endl;
    SMEE_UINT32 order = control_res_value & 0x7;
    switch (order)
    {

    case 0b1:
        std::cout << "get IDB 8nc" << std::endl;
        break;
    case 0b100:
        std::cout << "power Set" << std::endl;
        break;
    case 0b011:
        std::cout << "image Scan" << std::endl;
        break;
    case 0b0:
        std::cout << "get data" << std::endl;
        break;
    case 0b101:
        std::cout << "flush IGB queue" << std::endl;
        break;
    case 0b10:
        std::cout << "set ROI" << std::endl;
        break;

    default:
        std::cout << "none" << std::endl;
        break;
    }
    control_res_value = control_res_value >> 4;
    //std::cout << std::hex << control_res_value << std::endl;
    SMEE_UINT32 order2 = control_res_value & 0x1;
    switch (order2)
    {
    case 0b0:
        std::cout << "Flush N" << std::endl;
        break;
    case 0b1:
        std::cout << "Flush Y" << std::endl;
        break;

    default:
        break;
    }
    control_res_value = control_res_value >> 1;
    //std::cout << std::hex << control_res_value << std::endl;
    SMEE_UINT32 order3 = control_res_value & 0x1;
    switch (order3)
    {
    case 0b0:
        std::cout << "INTEGRATION N" << std::endl;
        break;
    case 0b1:
        std::cout << "INTEGRATION Y" << std::endl;
        break;

    default:
        break;
    }
    control_res_value = control_res_value >> 1;
    SMEE_UINT32 order4 = control_res_value & 0b11;
    switch (order4)
    {
    case 0b0:
        std::cout << "NO_TRANSFER" << std::endl;
        break;
    case 0b1:
        std::cout << "PIXEL DATA" << std::endl;
        break;
    case 0b10:
        std::cout << "TEST MODE" << std::endl;
        break;

    default:
        break;
    }
    control_res_value = control_res_value >> 2;
    SMEE_UINT32 order5 = control_res_value & 0b1111;
    std::cout << "SCAN ID:0x" << std::hex << order5 << std::endl;
    control_res_value = control_res_value >> 4;
    SMEE_UINT32 order6 = control_res_value & 0b11;
    switch (order6)
    {
    case 0b0:
        std::cout << "IDB POWER DOWN" << std::endl;
        break;
    case 0b1:
        std::cout << "IDB POWER idle" << std::endl;
        break;
    case 0b10:
        std::cout << "IDB POWER active" << std::endl;
        break;

    default:
        break;
    }
    control_res_value = control_res_value >> 2;
    SMEE_UINT32 order7 = control_res_value & 0b1;
    switch (order7)
    {
    case 0b0:
        std::cout << "none" << std::endl;
        break;
    case 0b1:
        std::cout << "Refrush HSSL register" << std::endl;
        break;

    default:
        break;
    }
    return 0;
}
int get_control2(SMEE_UINT32 control_res_value)
{
    printf("%x\n", control_res_value);
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
    printf("% x\n", order5);
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
    // control_res_value = 0x2570;
    // get_control(control_res_value);
    // control_res_value = 0x2470;
    // get_control(control_res_value);
    control_res_value = 0x473;
    get_control2(control_res_value);
    // control_res_value = 0x483;
    // get_control(control_res_value);
    // status_res_value = 0x000F0021;
    // get_status(status_res_value);
    // status_res_value = 0x000C0425;
    // get_status(status_res_value);
    return 0;
}