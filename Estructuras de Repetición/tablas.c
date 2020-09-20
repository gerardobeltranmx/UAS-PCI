#include <stdio.h>

int main(){
	int i, n, a, b, c;

	scanf("%d", &n);

	for(i = 1; i <= n; i++){
		scanf("%d", &a);

		for(b = 1; b <= 10; b++){
			c = a*b;
			printf("%dx%d=%d\n", a, b, c);
		}
		printf("\n");
	}

	return 0;
}3
