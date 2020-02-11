#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - a while loop
 *
 * Return: Returns nothing
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - main driver for the program
 *
 * Return: none
 */
int main(void)
{
	int i, child;

	for (i = 0; i < 5; i++)
	{
		child = fork();
		if (child == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", child);
	}
	infinite_while();
	return (0);
}
