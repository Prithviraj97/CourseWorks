/* 
 * File:   Lab 6 solution  starter code
 * Author: C Anderson
 *
 * Created on April 4, 2018, 3:10 AM
 */

/*Name: Prithvi Raj Singh
 Date: 04/22/2018
 This program will read the data from the given file and will be loading inventory to array of structure.
 This program will print out the items available in inventory in organized way */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUM_IDS 20
#define NUM_SIZES 5

int ids[NUM_IDS] = {317,325,355,376,377,380,387,398,420,430,432,437,441,444,458,459,471,479,481,496};
char sizes[NUM_SIZES][8] = {"petite", "small", "medium", "large", "X-large"};

int getSizeIndex(char size[]);
int getIDIndex(int id);
    
struct item {
    char type[7];
    char color[6];
    double price;
    int amount;
};


int main(void)
{
	// 1. Declare variables, including array of structures
	char tempType[7];
	char tempColor[6];
	char tempSize[10];
	double tempPrice;
	int tempAmount, tempID, ID_index, sizeIndex, rows, col;
	struct item description[NUM_IDS][NUM_SIZES];

	// 2. Open and test file connection
	FILE* dataStream;							
	dataStream = fopen("Lab6_data.dat", "r");
	if (dataStream == NULL)
		printf("Trouble reading the file.");

	// 3. Initialize all amount members in array of structures to zero
	for (rows = 0; rows < NUM_IDS; rows++)		
		for (col = 0; col < NUM_SIZES; col++)
			description[rows][col].amount = 0;

	// 4. Read data from file and store in proper element of the array.
	while (fscanf(dataStream, "%d %s %s %s %lf %d", &tempID, tempSize, tempType, tempColor, &tempPrice, &tempAmount) != EOF) 
	{
		ID_index = getIDIndex(tempID);
                
                
		sizeIndex = getSizeIndex(tempSize);
                

		for (col = 0; col < NUM_SIZES; col++)  
		{
			strcpy(description[ID_index][col].type, tempType);
		}
		strcpy(description[ID_index][sizeIndex].color, tempColor);
		description[ID_index][sizeIndex].price = tempPrice;
		description[ID_index][sizeIndex].amount = tempAmount;

		//printf("%d %d %s %s %.2lf %d\n", tempID, sizeIndex, description[ID_index][sizeIndex].type, description[ID_index][sizeIndex].color, description[ID_index][sizeIndex].price, description[ID_index][sizeIndex].amount);
	}
    fclose(dataStream);

	// 5. Print out the inventory table
	printf("This program will read the file lab6_data.dat and display it in good tabular form\n.The user won't have to input anything\n");
	printf("***************************************************************************************************\n");
	printf("                         Clearance items available\n");
	printf("***************************************************************************************************\n");
	printf(" ID   type    ");
	for (col = 0; col < NUM_SIZES; col++)
		printf("     %s     ", sizes[col]);
	printf("\n");
	printf("***************************************************************************************************\n");

	for (rows = 0; rows < NUM_IDS; rows++)
	{
		printf("%d ", ids[rows]);
		printf("%7s   ", description[rows][0].type); 
		for (col = 0; col < NUM_SIZES; col++)
		{
			if (description[rows][col].amount == 0) 
				printf("      N.A.      ");
			else
			{
				printf("%6s $%6.2lf  ", description[rows][col].color, description[rows][col].price); 
			}
		}
		printf("\n");
	}
	printf("***************************************************************************************************\n");
	
   
	printf("\n The program is ending. Thank you!!\n");
	return 0;
}

int getSizeIndex(char size[])
{
	int counter;
	for (counter = 0; counter < NUM_SIZES; counter++)
		if (strcmp(sizes[counter], size) == 0)
			break;
	return counter;
}

int getIDIndex(int id)
{
	int counter;
	for (counter = 0; counter < NUM_IDS; counter++)
		if (ids[counter] == id)
			break;
	return counter;
}