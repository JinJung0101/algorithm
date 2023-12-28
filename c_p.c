#include <stdio.h>

int main() {
	int array[2][3] = { 10,20,30,40,50,60 };

	int (*p)[3] = array;
	printf("%d\n", (*p+1)[4]);
	printf("%d\n", (*(p + 1))[0]);
	return 0;
}
