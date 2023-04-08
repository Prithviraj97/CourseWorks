/*Author :       Jeevin Maharaj
                 Prithvi Raj Singh
                 Rajib Rijal*/
//Date:          11/06/2019
//Program:       CS417Project1.c
//Theme:         To decipher the cipher text using the dictionary we have created.
//Instructor:    Dr. Vipin Menon
//Objective : i) To be able to create 1000 words dictionary
//           ii) To write program that will ask user for cipher text and decipher it using only the words in dictionary.
//          iii) To be able to evaluate the program performance. 

// This program will decipher the cipher text in lower case letter.


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define MAX_STRING_LENGTH 20

void caesar_cipher(char s1[], char s2[], int key);
char s[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

int main(int argc, char** argv) {
    
    int key = 1;
    int we_are_done = 0;
    char s1[MAX_STRING_LENGTH];
    char s2[MAX_STRING_LENGTH];
    char s3[MAX_STRING_LENGTH];
      
    FILE * fp; 
    
    
    printf("\n Please enter cipher text: ");
    scanf("%s", s1);
    
    while(key <= 25)
    {
        caesar_cipher(s1, s2, key);
        fp = fopen("Dictionary.txt", "r");  
        while(! feof(fp))
        {
            fscanf(fp, "%s", s3);
            if(strcmp(s2, s3) == 0)
            {
                printf("\n Cipher text = %s, Plain text = %s", s1, s2);
                we_are_done++;
                break;
            }
        }
        fclose(fp);
        key = key + 1;
    }
    if(we_are_done == 0)
    {
        printf("\n The cipher text = %s could not be matched with a plain text in our dictionary", s1);
    }
    

    return (EXIT_SUCCESS);
}

void caesar_cipher(char s1[], char s2[], int key)
{
    int i;
    int index;
    int length = strlen(s1);
    
    for(i = 0; i <= length-1; i++)
    {
        index = s1[i] - 65;
        index = index + key;
        index = index % 26;
        s2[i] = s[index];
    }
    s2[i] = '\0';
}