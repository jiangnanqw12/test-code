typedef unsigned int SMEE_UINT32;
#define BigtoLittle32(A) ((((SMEE_UINT32)(A)&0xff000000) >> 24) | (((SMEE_UINT32)(A)&0x00ff0000) >> 8) | \
                          (((SMEE_UINT32)(A)&0x0000ff00) << 8) | (((SMEE_UINT32)(A)&0x000000ff) << 24))
#include<iostream>
int main()
{
    std::cout << 0x20030004 << std::endl;
    std::cout << BigtoLittle32( 0x20030004 )<< std::endl;//0400 0320
    std::cout << BigtoLittle32(0x12345678) << std::endl;//78563214
    std::cout << BigtoLittle32(0x20000001) << std::endl; //0X0?100 0020?
    std::cout << BigtoLittle32(0x04000200) << std::endl; //?20004?
    std::cout << BigtoLittle32(0x00000004) << std::endl; //?0400 0000
    std::cout << BigtoLittle32(0x05000397) << std::endl; //?9703 0005
}
