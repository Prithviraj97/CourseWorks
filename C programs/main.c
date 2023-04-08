/*Author :      Jeevin Maharaj
                Prithvi Raj Singh
                Rajib Rijal*/
//Date:         11/06/2019
//Program:      CS417Part1.c
//Instructor:   Dr. Vipin Menon
//Theme:        To build program that will use user feedback to decipher the cipher text.
//Objective: i) To use the character function <c.type> to perform ciphering and deciphering.
//          ii) To be able to successfully deciphering the cipher text using the function we have created.
//         iii) To use the ceaser cipher function to perform deciphering.


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define MAX_STRING_LENGTH 20

void caesar_cipher(char s1[], char s2[], int key);
char s[26] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

int main(int argc, char** argv) {
    
    int key = 1;             //Key to perform the deciphering. 
    int we_are_done = 0;    
    char s1[MAX_STRING_LENGTH];
    char s2[MAX_STRING_LENGTH];
    
    printf("\n Please enter cipher text: ");
    scanf("%s", s1);
    
    while((we_are_done == 0) && (key <= 25))  
    {
        caesar_cipher(s1, s2, key);
        printf("\n The plain text is: %s", s2);
        printf("\n Is this plain text correct ? 1 for yes, 0 for no: ");
        scanf("%d", &we_are_done);
        key = key + 1;
    }
    printf("\n Cipher text = %s, Plain text = %s", s1, s2);

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

