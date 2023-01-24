/*Alice in Borderland - Diamond Of The King Game*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int rules()
{
    printf("All players select a number between 0 and 100 in the given time.\nThe average of the values will be multiplied by 4/5.\n The person who chooses the number closest to the calculated number wins.\n This constitutes one round.All losers will lose a point.\n A new rule is introduced for every player eliminated. On the first round and all following rounds where a new rule is introduced, players are allotted 5 minutes as a way to get used to the rules. ");
}
void bubbleSort(int arr[], int n)
{
    int i, j, temp;
    for (i = 0; i < n - 1; i++)
    {
        for (j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int game(int Keiichi_Kuzuryu, int Benzo_Yashige, int Hinako_Daimon, int Takashi_Asuma, int Shuntaro_Chishiya, int guess_pool[5], int your_guess, int sum, int average, int difference_pool[5])
{
    bool rounds = true;
    int smallest = 969;
    int winner = 4;
    char *players[5] = {"Keiichi_Kuzuryu", "Benzo_Yashige", "Hinako_Daimon", "Takashi_Asuma", "Shuntaro_Chishiya"};
    while (rounds)
    {
        printf("\nWhat is your guess between 0 and 100? ");
        scanf("%d", &your_guess);
        for (int i = 0; i < 4; i++)
        {
            guess_pool[i] = rand() % 100 + 1;
        
        }
        if(Keiichi_Kuzuryu<=-10){
            guess_pool[0]=101;
        }
        if(Benzo_Yashige<=-10){
            guess_pool[1]=101;
        }
        if(Hinako_Daimon<=-10){
            guess_pool[2]=101;
        }
        if(Takashi_Asuma<=-10){
            guess_pool[3]=101;
        }
        
        int kuzuryu = guess_pool[0];
        int yashige = guess_pool[1];
        int daimon = guess_pool[2];
        int asuma = guess_pool[3];

        guess_pool[4] = your_guess;

        sum = 0;
        for (int i = 0; i < 5; i++)
        {
            if(guess_pool[i] != 101){
            sum += guess_pool[i];
            }
        }
        int n = 5;
        for(int i=0;i<n;i++){
            if(guess_pool[i] == 101){
                n -= 1;

            }
        }
        int average = (sum / n);
        int finally = average * 0.8;
        for (int i = 0; i < 5; i++)
        {
            if(guess_pool[i] != 101){
            difference_pool[i] = abs(guess_pool[i] - finally);
            }
        }
        int m = 5;
        bubbleSort(difference_pool, m);
        for (int i = 0; i < 5; i++)
        {
            if (difference_pool[0] == abs(guess_pool[i] - finally))
            {
                winner = i;
            }
        }

        printf("Kuzuryu's guess is %d.\n", kuzuryu);
        printf("Yashige's guess is %d.\n", yashige);
        printf("Daimon's guess is %d.\n", daimon);
        printf("Asuma's guess is %d.\n", asuma);
        printf("Your guess is %d.\n", your_guess);
        printf("Average'4/5 is %d.\n", finally);
        printf("The winner is %s", players[winner]);

        if (winner == 4)
        {
            printf("\nYou won!\n");
        }
        else
        {
            printf("\nThe winner is %s", players[winner]);
        }
    
    if (players[0] == players[winner])
    {
        Keiichi_Kuzuryu = Keiichi_Kuzuryu;
        Benzo_Yashige = Benzo_Yashige - 1;
        Hinako_Daimon = Hinako_Daimon - 1;
        Takashi_Asuma = Takashi_Asuma - 1;
        Shuntaro_Chishiya = Shuntaro_Chishiya - 1;
    }
    else if (players[1] == players[winner])
    {
        Keiichi_Kuzuryu = Keiichi_Kuzuryu - 1;
        Benzo_Yashige = Benzo_Yashige;
        Hinako_Daimon = Hinako_Daimon - 1;
        Takashi_Asuma = Takashi_Asuma - 1;
        Shuntaro_Chishiya = Shuntaro_Chishiya - 1;
    }
    else if (players[2] == players[winner])
    {
        Keiichi_Kuzuryu = Keiichi_Kuzuryu - 1;
        Benzo_Yashige = Benzo_Yashige - 1;
        Hinako_Daimon = Hinako_Daimon;
        Takashi_Asuma = Takashi_Asuma - 1;
        Shuntaro_Chishiya = Shuntaro_Chishiya - 1;
    }
    else if (players[3] == players[winner])
    {
        Keiichi_Kuzuryu = Keiichi_Kuzuryu - 1;
        Benzo_Yashige = Benzo_Yashige - 1;
        Hinako_Daimon = Hinako_Daimon - 1;
        Takashi_Asuma = Takashi_Asuma;
        Shuntaro_Chishiya = Shuntaro_Chishiya - 1;
    }
    else if (players[4] == players[winner])
    {
        Keiichi_Kuzuryu = Keiichi_Kuzuryu - 1;
        Benzo_Yashige = Benzo_Yashige - 1;
        Hinako_Daimon = Hinako_Daimon - 1;
        Takashi_Asuma = Takashi_Asuma - 1;
        Shuntaro_Chishiya = Shuntaro_Chishiya;
    }
    if(Keiichi_Kuzuryu>-11){
    printf("Total point of Keiichi_Kuzuryu is %d.\n", Keiichi_Kuzuryu);}
    if(Benzo_Yashige>-11){
    printf("Total point of Benzo_Yashige is %d.\n", Benzo_Yashige);}
    if(Hinako_Daimon>-11){
    printf("Total point of Hinako_Daimon is %d.\n", Hinako_Daimon);}
    if(Takashi_Asuma>-11){
    printf("Total point of Takashi_Asuma is %d.\n", Takashi_Asuma);}
    if(Shuntaro_Chishiya>-11){
    printf("Total point of Shuntaro_Chishiya is %d.\n", Shuntaro_Chishiya);}
    

    if (Keiichi_Kuzuryu <= -10 && Benzo_Yashige <= -10 && Hinako_Daimon <= -10 && Takashi_Asuma <= -10)
    {
        rounds = false;
    }
    else if (Keiichi_Kuzuryu <= -10 && Benzo_Yashige <= -10 && Hinako_Daimon <= -10 && Shuntaro_Chishiya <= -10)
    {
        rounds = false;
    }
    else if (Keiichi_Kuzuryu <= -10 && Takashi_Asuma <= -10 && Hinako_Daimon <= -10 && Shuntaro_Chishiya <= -10)
    {
        rounds = false;
    }
    else if (Takashi_Asuma <= -10 && Benzo_Yashige <= -10 && Hinako_Daimon <= -10 && Shuntaro_Chishiya <= -10)
    {
        rounds = false;
    }
    if(Shuntaro_Chishiya==-10){
        rounds = false;
    }
    }
}

int main()
{
    int Keiichi_Kuzuryu = 0;
    int Benzo_Yashige = 0;
    int Hinako_Daimon = 0;
    int Takashi_Asuma = 0;
    int Shuntaro_Chishiya = 0;

    int average;
    int sum = 0;
    int your_guess;

    int guess_pool[5];
    int difference_pool[5];
    rules();
    game(Keiichi_Kuzuryu, Benzo_Yashige, Hinako_Daimon, Takashi_Asuma, Shuntaro_Chishiya, guess_pool, your_guess, sum, average, difference_pool);

    return 0;
}
