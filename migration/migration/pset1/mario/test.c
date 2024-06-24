#include <stdio.h>
#include <cs50.h>


int main()
{
	int i,j,n;
	printf("enter row size:");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=i;j++)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}

/*int main (void)
{

    int level = 8;
    for(int i=0; i<level; i++)
    {
        printf("%*.*s\n", level, i+1, "######");
    }

}
*/


/*
printf("%-9smen\n","meet");
 printf("%-8smen\n","meet");
 printf("%-7smen\n","meet");
 printf("%-6smen\n","meet");
 printf("%-5smen\n","meet");
 printf("%-4smen\n","meet");
 return(0);
*/
/*
int main()
{
	int i,j,n;
	printf("enter row size:");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=i;j++)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}
*/